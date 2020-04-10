# coding=utf-8
import os
import shutil

#目标文件夹，此处为相对路径，也可以改为绝对路径
determination = r'C:\Users\lza\Documents\Python Scripts\homework_game_images\\'
if not os.path.exists(determination):
    os.makedirs(determination)
count = 0
#源文件夹路径
path = r'C:\Users\lza\Documents\Python Scripts\homework_game\images'
files= os.listdir(path)
foreNameList = []

for file in files:
    filename = str(file)
    if filename.endswith('gif'):
        count += 1
        source = path + '\\' + filename
        newname = filename.split
        deter = determination + 
        shutil.copyfile(source, deter)
        print(count)
    else:
        continue
