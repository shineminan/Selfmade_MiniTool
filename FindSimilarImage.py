import numpy as np
import cv2
import os
import shutil

def return_his(pic):
    a, _ = np.histogram(pic, 64, [0,256])
    b = a/sum(a)
    return b

def diff_lists(lst1,lst2):
    a = abs(lst1 - lst2)
    return sum(a)

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
totalpicnumber = len(imageslist)

histlist = []
for image in imageslist:
    histlist.append(return_his(image))

i = 0
# while i == 0:
print("Checking " + str(i+1) + "/" + str(totalpicnumber) + " pictures")
histdifflist = list(np.sum(abs(histlist - histlist[i]), 1))

histdifflist[i] = 100
c = sorted(histdifflist)
print(c)

d = histdifflist.index(c[0])

possiblesimilarimages = np.hstack((imageslist[0], imageslist[d]))


cv2.imshow('image', possiblesimilarimages)
cv2.waitKey(0)