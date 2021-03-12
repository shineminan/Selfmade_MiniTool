import numpy as np
import cv2
import os
import shutil

def load_images_from_folder(folder):
    images_dict = {}
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images_dict[filename] = img
    return images_dict

folder = "C:\\Users\\shine\\Desktop\\Tom_Daley"
imagesdict = load_images_from_folder(folder)
imageslist = list(imagesdict.values())

cv2.imshow('image', imageslist[0])
cv2.waitKey(0)