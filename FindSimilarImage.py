import numpy as np
import cv2
import os
import ctypes
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
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images_dict[filename] = img
    return images_dict

# def show_image_sbys(img1,img2):
#     h1, w1 = img1.shape[:2]
#     h2, w2 = img2.shape[:2]
#     h = max(h1, h2)
#     w = w1+w2
#     vis = np.zeros((h, w, 3), np.uint8)
#     vis[:h1, :w1,:3] = img1
#     vis[:h2, w1:w1+w2,:3] = img2
#     return h, w, vis

def show_image_h(lst): #show images horizontally
    hs = []
    ws = []
    for i in range(len(lst)):
        a, b = lst[i].shape[:2]
        hs.append(a)
        ws.append(b)
    vis = np.zeros((max(hs), sum(ws), 3), np.uint8)

    w = 0
    for i in range(len(lst)):
        hi = hs[i]
        wi = ws[i]
        # print("imagesgaoe",hi,wi)
        vis[:hi, w:w+wi, :3] = lst[i]
        w += wi

    displayw = screenw
    displayh = int(screenw/sum(ws)*max(hs))
    if displayh > screenh:
        displayh = screenh
        displayw = int(screenh/max(hs)*sum(ws))

    imS = cv2.resize(vis, (displayw, displayh))


    cv2.imshow('image', imS)
    cv2.waitKey(0)








user32 = ctypes.windll.user32
screenw, screenh = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)






folder = input("Paste the folder address here: ")
imagesdict = load_images_from_folder(folder)
imageslist = list(imagesdict.values())
totalpicnumber = len(imageslist)
histlist = []
for image in imageslist:
    histlist.append(return_his(image))

for i in range(totalpicnumber):
    print("Checking " + str(i+1) + "/" + str(totalpicnumber) + " pictures")

    histdifflist = list(np.sum(abs(histlist - histlist[i]), 1))
    histdifflist[i] = 100

    c = sorted(histdifflist)
    # print("sorted hist", c)

    smallhist = [x for x in histdifflist if x <= 0.3]

    similarimages = []
    if len(smallhist) == 0:
        print("Didn't find a similar image")
    else:
        similarimages.append(imageslist[histdifflist.index(100)])
        for diff in smallhist:
            similarimages.append(imageslist[histdifflist.index(diff)])
        show_image_h(similarimages)