import numpy as np
import cv2
import os
import ctypes
user32 = ctypes.windll.user32
screenw, screenh = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
sensitivity = 0.2


def return_his(pic):
    a, _ = np.histogram(pic, 64, [0, 256])
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
        vis[:hi, w:w+wi, :3] = lst[i]
        w += wi

    displayw = screenw
    displayh = int(screenw/sum(ws)*max(hs))
    if displayh > screenh:
        displayh = screenh
        displayw = int(screenh/max(hs)*sum(ws))

    imS = cv2.resize(vis, (displayw, displayh))
    cv2.imshow('image', imS)
    a = cv2.waitKey(0)
    return a

def single_folder_compare(folder):
    print("." * 200)
    print(folder + " is being check")
    imagesdict = load_images_from_folder(folder)
    filenamelist = list(imagesdict.keys())
    imageslist = list(imagesdict.values())
    totalpicnumber = len(imageslist)
    deletenamelst = []

    histlist = []
    for image in imageslist:
        histlist.append(return_his(image))

    for i in range(totalpicnumber):
        print("Checking " + "picture: " + filenamelist[i] + " -> (" + str(i+1) + "/" + str(totalpicnumber) + ")")

        histdifflist = list(np.sum(abs(histlist - histlist[i]), 1))
        histdifflist[i] = 100
        # c = sorted(histdifflist)
        smallhist = [x for x in histdifflist[i:] if x <= sensitivity]

        similarimages = []
        similarimages_filename = []
        if len(smallhist) == 0:
            print("Didn't find a similar image")
        else:
            a = histdifflist.index(100)
            similarimages.append(imageslist[a])
            similarimages_filename.append(filenamelist[a])
            for diff in smallhist:
                a = histdifflist.index(diff)
                similarimages.append(imageslist[a])
                similarimages_filename.append(filenamelist[a])
            print(similarimages_filename)
            index = int(show_image_h(similarimages))
            if index > 48:
                number = index - 48
                deletenamelst.append(similarimages_filename[number-1])
    for name in tuple(deletenamelst):
        os.remove(folder + "\\" + name)
    print("Totally " + str(len(deletenamelst)) + " picture(s) deleted")

def multiple_folder_compare(folder):
    subfolders = os.listdir(folder)
    paths_list = []
    for name in subfolders:
        subfolderpath = folder + '\\' + name
        paths_list.append(subfolderpath)
    for path in paths_list:
        single_folder_compare(path)


infoinput = input("Paste the folder address here seperated by a coma with indication of single folder comparision(1) or multiple comparision(2): ")
folder, index = (infoinput.split(","))
if int(index) == 1:
    single_folder_compare(folder)
elif int(index) == 2:
    multiple_folder_compare(folder)
else:
    print("Duck you, totally wrong input!!!")