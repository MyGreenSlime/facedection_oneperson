import cv2
import glob
import os
face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
images = glob.glob('./piam/*')
count  =0
path = './piam2'
for image in images:
    try:
        img = cv2.imread(image)
        gray_img = cv2.GaussianBlur(img,(21,21),0)
        gray_img = cv2.cvtColor(gray_img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_img,scaleFactor =1.05,minNeighbors = 5)
    #print(len(faces))
        if len(faces) == 1:
            count+=1
            cv2.imwrite(os.path.join(path,str(count)+'piam.jpg'),img)
    except:
        pass
print('finish')