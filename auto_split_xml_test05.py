# -*- coding: utf-8 -*-
#批量处理img和xml文件，根据xml文件中的坐标把img中的目标标记出来，并保存到指定文件夹，方便自己查看目标标记的是否准确。
import xml.etree.ElementTree as ET
import os, cv2
from tqdm import tqdm

"""annota_dir = '/home/dlut/网络/make_database/数据集处理/Annotations_xml'
origin_dir = '/home/dlut/网络/make_database/数据集处理/JpGImages_img'
target_dir1='/home/dlut/网络/make_database/数据集处理/123456'"""

annota_dir = 'images/Annotations/'
origin_dir = 'images/JPEGImages/'
target_dir1= 'img05/'

def divide_img(oriname):
    img_file = os.path.join(origin_dir, oriname + '.jpg')
    im = cv2.imread(img_file)

    xml_file = os.path.join(annota_dir, oriname + '.xml')  # 读取每个原图像的xml文件
    tree = ET.parse(xml_file)
    root = tree.getroot()
#im = cv2.imread(imgfile)
    for object in root.findall('object'):
        object_name = object.find('name').text
        Xmin = int(object.find('bndbox').find('xmin').text)
        Ymin = int(object.find('bndbox').find('ymin').text)
        Xmax = int(object.find('bndbox').find('xmax').text)
        Ymax = int(object.find('bndbox').find('ymax').text)
        color = (4, 250, 7)
        cv2.rectangle(im, (Xmin, Ymin), (Xmax, Ymax), color, 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(im, object_name, (Xmin, Ymin - 7), font, 0.5, (6, 230, 230), 2)
        cv2.imshow('01', im)

    img_name = oriname + '.jpg'
    to_name = os.path.join(target_dir1, img_name)
    cv2.imwrite(to_name, im)

img_list = os.listdir(origin_dir)
for name in img_list:
    divide_img(name.rstrip('.jpg'))
