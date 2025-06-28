import os
import time

FOLDER="C:/Users/Ghamani/Downloads/ghamani"
age=10

for i in os.listdir(FOLDER):
    path=os.path.join(FOLDER,i)
    if time.time()-os.path.getmtime(path)>age:
        os.remove(path)
        print("File deleted")