import cv2
import os
import numpy as numpy
face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
nicknames = ['kaew','kaimook','kate','korn','maysa','mind','miori','mobile','music','namneung','namsai','nink','noey','orn','piam','pupe','satchan','tarwaan','pun']
for nickname in nicknames:
    names = [nickname+'1.mp4',nickname+'2.mp4']
    num = 0
    for name in names:
        cap = cv2.VideoCapture(name)
        if (cap.isOpened()== False): 
            print("Error opening video stream or file")
        path = './'+nickname+'video'
    # Read until video is completed
        count = 0
        while(cap.isOpened()):
    # Capture frame-by-frame
            ret, frame = cap.read()
            if num > 2000:
                break
            if ret == True:
        # Display the resulting frame
                count+=1
                if(count%60 == 0):
                    try:
                        img = frame
                        gray_img = cv2.GaussianBlur(img,(21,21),0)
                        gray_img = cv2.cvtColor(gray_img,cv2.COLOR_BGR2GRAY)
                        faces = face_cascade.detectMultiScale(gray_img,scaleFactor =1.05,minNeighbors = 5)
                        #print(len(faces))
                        if len(faces) == 1:
                            #print(len(faces))
                            num+=1
                            cv2.imwrite(os.path.join(path,str(num)+nickname+'video.jpg'),frame)
                    except:
                        pass        
            #cv2.imshow('Frame',frame)
            #key = cv2.waitKey(1)
            #if key == ord('q'):
            #   break
    # Break the loop
            else: 
                break
    # When everything done, release the video capture object
        cap.release()
    # Closes all the frames
    #cv2.destroyAllWindows()