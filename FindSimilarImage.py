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

def combine_image_sbys(img1,img2):
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    h = max(h1, h2)
    w = w1+w2
    vis = np.zeros((h, w, 3), np.uint8)
    vis[:h1, :w1,:3] = img1
    vis[:h2, w1:w1+w2,:3] = img2
    return h, w, vis

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
smallhist = [x for x in c if x <= 0.5]
print(smallhist)

for item in smallhist:
    print(item)
    a = histdifflist.index(item)
    h, w, possiblesimilarimages = combine_image_sbys(imageslist[0], imageslist[a])
    imS = cv2.resize(possiblesimilarimages, (1000, int(1000/w*h)))

    cv2.imshow('image', imS)
    b = input("Which one you want to delete? 1 or 2? Press Enter to skip")
    cv2.waitKey(0)


    print(b)



