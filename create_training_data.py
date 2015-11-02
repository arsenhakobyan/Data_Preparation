#!/usr/bin/env python
# This tool helps to generate training data set of an images croped from the ones located under './images' directory.
# create_training_data.py <dirname> <xml file>
import cv2
import math
import os
import os.path
import sys
import subprocess
import xml.etree.ElementTree as ET

dirname = sys.argv[1]
xmlfile = sys.argv[2]
origimgdir = sys.argv[3]
def cmd_exists(cmd):
    return subprocess.call("type " + cmd, shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE) == 0

if not cmd_exists("imglab"):
    print ("the program 'imglab' does not exist. Please install Dlib/tools/imglab.")

print ("imglab -c " + xmlfile + " " + origimgdir + "/*")

os.system("imglab -c " + xmlfile + " " + origimgdir + "/*")
os.system("imglab " + xmlfile)

if not os.path.exists(dirname):
        os.makedirs(dirname)

tree = ET.parse(xmlfile)
root = tree.getroot()
filenum = 1
for image in root.iter('image'):
    for box in image:
        image_name = image.get('file')
        top = box.get('top')
        left = box.get('left')
        width = box.get('width')
        height = box.get('height')
        img = cv2.imread(image_name)
        x = int(top) + int(height)
        y = int(left) + int(width)
        croped_img = img[int(top):int(x), int(left):int(y)]
        filename = str(dirname) + "/" + str(dirname) + "_" + str(filenum) + ".jpg"
        while os.path.exists(filename):
            filenum += 1
            filename = str(dirname) + "/" + str(dirname) + "_" + str(filenum) + ".jpg"
        cv2.imwrite(filename, croped_img)
        filenum += 1
