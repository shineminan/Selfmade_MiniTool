import numpy as np
import cv2
import os
import shutil
from shutil import copyfile



pagenr = 2
img = 2
pdfini = "pdfpage_("
picini = "17_Unamed_"
c = "./"
e = ".jpg"

while pagenr > 0:
    pagepath = c + pdfini + str(pagenr) + ").jpg"
    pdfpage = cv2.imread(pagepath, 1)
    pich, picw, _ = pdfpage.shape
    print(pagenr, pich,picw)
    mid = int(picw/2)
    a = pdfpage[:, :mid]
    b = pdfpage[:, mid:]

    cv2.imwrite(c + picini + str(img)+e, a)
    img += 1
    cv2.imwrite(c + picini + str(img)+e, b)
    img += 1
    pagenr += 1