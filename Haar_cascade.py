import cv2
import numpy as np

face_file = 'haarcascade_frontalface_default.xml'
eyes_file = 'frontalEyes.xml'
smile_file = 'haarcascade_smile.xml'
glasses_file = 'glasses2.png'
mustache_file = 'mustache.png'


#Initialize Cascade Classifier
face_cascade = cv2.CascadeClassifier(face_file)
smile_cascade = cv2.CascadeClassifier(smile_file)

#Read image to apply effects
glasses = cv2.imread(glasses_file, -1)
mustache = cv2.imread(mustache_file, -1)





#This function is optional

#################################Define resize function#########################

def resize_image(image, h=None, w=None, inter=cv2.INTER_AREA):
    dim=None

    _h,_w = image.shape[:2]

    if w is None and h is None:
        return image
    if w is None:
        r = h / float(_h)
        dim = (int(_w*r), h)
    else:
        r = w / float(_w)
        dim = (w, int(_h*r))

    resized = cv2.resize(image, dim, interpolation=inter)
    
    return resized
        

##############################start the show####################################



#Initialize Fvideo reader class
cap = cv2.VideoCapture(0)
image = cv2.imread('images.jpg')

#Inifity loop to show all frames like video
while True:

#Initialize frame to show
    _, frame = cap.read()
#To the algorithm HaarCascade is more easy works with gray images
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#Apply alpha channel to image to overlay
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    
#NOW lets detect the faces on frames
    face = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
   

#Unpack the coordiantes with for loop
    for x, y, w, h in face:
           facesG = gray_frame[y:y+h, x:x+w]
           facesC = image[y:y+h, x:x+w]
           #facesC = cv2.cvtColor(facesC, cv2.COLOR_BGR2BGRA)
           #cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0))
           
           
#Resize effect image to our frame scale
           glasses2  = cv2.resize(glasses.copy(), (h,w))
           _w, _h, _c = glasses2.shape
           print(glasses2.shape)
           
#Now, this for loop slices each image effect pixel and now arround our eyes are the glasses
           for i in range(0, _w):
               for j in range(0, _h):
                   if glasses2[i,j][3] != 0:
                       image[i+y, j+x] = glasses2[i,j]

#The same steps to detect the smile and put a mustache

           smile = smile_cascade.detectMultiScale(facesG, 1.5, 5)
          
           
           for sx, sy, sw, sh in smile:
               smileG = facesG[sy:sy+sh, sx:sx+sw]
               
               

               mustache2 = resize_image(mustache.copy(),w=sw)
               _mw, _mh, _mc = mustache2.shape

               for i in range(0, _mw):
                   for j in range(0, _mh):
                       if mustache2[i, j][3] != 0:
                           facesC[sy+i, sx+20+j] = mustache2[i,j]

           

    frame = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    cv2.imshow('frame', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
      
cap.release()
cv2.destroyAllWindows()
   


    
                                             
            
        
        
    
    


    
