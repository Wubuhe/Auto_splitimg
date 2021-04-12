# 将图片分成了mxn块
# -*- coding:utf-8 -*-
import os
import matplotlib.pyplot as plt
import cv2
import numpy as np


def divide_img(img_path, img_name, save_path):
    imgg = img_path + img_name
    img = cv2.imread(imgg)
    #   img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    h = img.shape[0]
    w = img.shape[1]
    n = int(np.floor(h * 1.0 / 1000)) + 1
    m = int(np.floor(w * 1.0 / 1000)) + 1
    print('h={},w={},n={},m={}'.format(h, w, n, m))
    dis_h = int(np.floor(h / n))
    dis_w = int(np.floor(w / m))
    num = 0
    for i in range(n):
        for j in range(m):
            num += 1
            print('i,j={}{}'.format(i, j))
            sub = img[dis_h * i:dis_h * (i + 1), dis_w * j:dis_w * (j + 1), :]
            cv2.imwrite(save_path + '{}_{}.jpg'.format(name, num), sub)


if __name__ == '__main__':

    save_path = './img03/'  # 输入图片地址
    img_path = './images/JPEGImages/'  # 输出图片的地址

    img_list = os.listdir(img_path)
    for name in img_list:
        divide_img(img_path, name, save_path)
