import cv2
import numpy as np


camera = cv2.VideoCapture(0)
video = cv2.VideoCapture('car.avi')
mask2 = cv2.createBackgroundSubtractorMOG2(200, 16, True)
mask = cv2.createBackgroundSubtractorMOG2(300, 400, True)

while True:

    ret, frame_cam = camera.read()
    ret, frame_video = video.read()
  
    dsize = frame_cam.shape[:-1]
    image = cv2.resize(frame_video, (640,480))
    
    print('Frame cam size {}, Frame video size {}'.format(dsize, image.shape[:-1]))

    mask = mask2.apply(image)
    black_mask = cv2.bitwise_not(mask)
    black_mask =  cv2.GaussianBlur(black_mask,(5,5),cv2.BORDER_DEFAULT)
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
