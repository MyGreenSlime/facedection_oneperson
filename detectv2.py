import cv2
import glob
import os
face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
names = ['can','cherprang','izutarina','jaa','jane','jennis','jib','kaew','kaimook','kate','korn','maysa','mind','miori','mobile','music','namneung','namsai','nink','noey','orn','pun','pupe','satchan','tarwaan']
for name in names:
    images = glob.glob('./'+name+'/*')
    count  =0
    path = './'+name+'2'
    for image in images:
        try:
            img = cv2.imread(image)
            gray_img = cv2.GaussianBlur(img,(21,21),0)
            #gray_img = cv2.medianBlur(gray_img,7)
            gray_img = cv2.cvtColor(gray_img,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_img,scaleFactor =1.05,minNeighbors = 5)
            #print(len(faces))
            if len(faces) == 1:
                count+=1
                cv2.imwrite(os.path.join(path,str(count)+name+'.jpg'),img)
        except:
            pass
    print('finish',name)