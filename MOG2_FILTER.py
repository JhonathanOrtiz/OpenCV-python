import cv2
import numpy as np

#initialize


camera = cv2.VideoCapture(0)
video = cv2.VideoCapture('car.avi')
mask2 = cv2.createBackgroundSubtractorMOG2()


while True:


    #Initialize the frames from camera and video

    ret, frame_cam = camera.read()
    ret, frame_video = video.read()
  
    #Both frame should has the same size

    dsize = frame_cam.shape[:-1]
    image = cv2.resize(frame_video, (640,480))
    
    print('Frame cam size {}, Frame video size {}'.format(dsize, image.shape[:-1]))
    
    #apply the mask

    mask = mask2.apply(image)
    black_mask = cv2.bitwise_not(mask)
    
    #apply bitwise and sum images.
 
    frame_cam = cv2.bitwise_and(frame_cam, frame_cam, mask=mask)
    image = cv2.bitwise_and(image, image, mask=black_mask)
    final_img = cv2.add(frame_cam, image)
    cv2.imshow('mask_cam', final_img)
    cv2.imshow('mask', mask)
    cv2.imshow('invertedmask', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
camera.release()
cv2.destroyAllWindows()
