import os
import cv2

path = "Images"
Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.png', '.jpg']:
        file_name = path+"/"+file

        print(file_name)
               
        Images.append(file_name)
        
print(len(Images))
count = len(Images)
frame= cv2.imread(Images[0])
height,width,channels= frame.shape
size= (width,height)
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
out = cv2.VideoWriter('project.mp4',fourcc, 20.0, (640,480))


for i in range(len(Images)):
    frame= cv2.imread(Images[i])
    out.write(frame)

out.release()
print("Video Complete")



