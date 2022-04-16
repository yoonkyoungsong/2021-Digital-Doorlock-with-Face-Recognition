import cv2
import numpy as np
import os

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_extractor(img):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return None

    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face


Face_ID = -1 
pev_person_name = ""

Face_Images = os.path.join(os.getcwd(), "Face_Images") #이미지 폴더 지정
print (Face_Images)

for root, dirs, files in os.walk(Face_Images) : #파일 목록 가져오기
    for file in files :
        if file.endswith("jpeg") or file.endswith("jpg") or file.endswith("png") : #이미지 파일 필터링
            path = os.path.join(root, file)
            person_name = os.path.basename(root)
            print(path, person_name)
 
            if pev_person_name != person_name : #이름이 바뀌었는지 확인
                Face_ID=Face_ID+1
                pev_person_name = person_name
                count = 0

            img = cv2.imread(path) #이미지 파일 가져오기

            if face_extractor(img) is not None:
                count+=1
                face = cv2.resize(face_extractor(img),(200,200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                file_name_path = 'faces/'+person_name+'/'+person_name+str(count)+'.jpg'
                cv2.imwrite(file_name_path,face)

            else:
                print("Face not Found")
                pass

print('Colleting Samples Complete!!!')
