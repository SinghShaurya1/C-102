import os 
import shutil

from_dir = 'C:/Users/catha/Downloads/C102_assets-main/C102_assets-main'
to_dir = "C:/Users/catha/OneDrive/Desktop/images"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extention = os.path.splitext(file_name)
    if extention == '':
        continue
    if extention in ['.jpg', '.jpeg', '.png', '.gif', '.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'image_files'
        path3 = to_dir + '/' + file_name
        if os.path.exists(path2):
            print('moving' + file_name + '....')
            shutil.move(path1, path3)
        else: 
           # os.makedirs(path2)    
            print('moving' + file_name + '....')
            shutil.move(path1, path3)