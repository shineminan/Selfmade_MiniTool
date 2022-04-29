import numpy as np
import shutil
import os
import ctypes
user32 = ctypes.windll.user32
# screenw, screenh = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


# C:\Users\shine\iCloudDrive\Others_stuff\5_Celebrities\Jack_Laugher,D:\iCloud_other_stuff\5_Celebrities\Jack_Laugher

infoinput = input("Please enter the folder path of two folders where folder New push to folder Old, separated by comma: ")
folderpathN, folderpathO = (infoinput.split(","))
print(folderpathN)
picnamesN = [picname for picname in os.listdir(folderpathN)]
picnamesO = [picname for picname in os.listdir(folderpathO)]
pushlist = []
for picname in picnamesN:
    if picname not in picnamesO:
        pushlist.append(picname)
for file in pushlist:
    shutil.copy(folderpathN + "\\" + file, folderpathO + "\\" + file)