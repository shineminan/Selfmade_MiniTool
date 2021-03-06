import numpy as np
import cv2
import os
import shutil
from shutil import copyfile

def pic_crop_para(picture):
    pich, picw, _ = picture.shape
    pichc = int(pich/3)
    picwc = int(picw/3)
    return pichc, pichc*2, pich, picwc, picwc*2, picw

def ninecrop(picture):
    a, b, c, d, e, f = pic_crop_para(picture)

    a1 = picture[0:a, 0:d]
    a2 = picture[a:b, 0:d]
    a3 = picture[b:c, 0:d]

    b1 = picture[0:a, d:e]
    b2 = picture[a:b, d:e]
    b3 = picture[b:c, d:e]

    c1 = picture[0:a, e:f]
    c2 = picture[a:b, e:f]
    c3 = picture[b:c, e:f]

    return a1, a2, a3, b1, b2, b3, c1, c2, c3

def return_his(pad):
    a, _ = np.histogram(pad, 54, [0,256])
    b = a/sum(a)
    return b

def diff_lists(lst1,lst2):
    a = abs(lst1 - lst2)
    return sum(a)

def similar_hist_order(referencelst, originallst):
    refhist = []
    orghist = []
    num_order = []

    for refpad in referencelst:
        refhist.append(return_his(refpad))
    for orgpad in originallst:
        orghist.append(return_his(orgpad))
    for r in refhist:
        a = []
        for o in orghist:
            a.append(diff_lists(r,o))
        smallest_idx = a.index(min(a))
        num_order.append(smallest_idx)
    return num_order

def main_per_image(ref,org):
    a, b, c, d, e, f = pic_crop_para(org)
    orgh, orgw, _ = org.shape
    ref9lst = list(ninecrop(ref))
    org9lst = list(ninecrop(org))
    blank_image = np.zeros((c, f, 3), np.uint8)
    num_order = similar_hist_order(ref9lst, org9lst)

    blank_image[0:a, 0:d] = org9lst[num_order[0]]
    blank_image[a:b, 0:d] = org9lst[num_order[1]]
    blank_image[b:c, 0:d] = org9lst[num_order[2]]

    blank_image[0:a, d:e] = org9lst[num_order[3]]
    blank_image[a:b, d:e] = org9lst[num_order[4]]
    blank_image[b:c, d:e] = org9lst[num_order[5]]

    blank_image[0:a, e:f] = org9lst[num_order[6]]
    blank_image[a:b, e:f] = org9lst[num_order[7]]
    blank_image[b:c, e:f] = org9lst[num_order[8]]

    cv2.imwrite(r"C:\Users\shine\Desktop\aa\test\OUT\sample.jpg", blank_image)
    cv2.imshow('image', blank_image)
    cv2.waitKey(0)

    # return blank_image


c1 = "./REF/"
c2 = "./ORG/"
e = ".jpg"

for i in range(127):
    refstring = c1 + str(i) + e
    orgstring = c2 + str(i) + e
    newname = "./OUT/" + str(i) + e

    ref = cv2.imread(refstring, 1)
    org = cv2.imread(orgstring, 1)
    a = main_per_image(ref, org)

    os.rename("./OUT/sample.jpg", newname)
    shutil.copy(r"C:\Users\shine\Desktop\sample.jpg", "./out")
