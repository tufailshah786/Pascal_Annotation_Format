import numpy as np
import cv2
import math  
import os
import xml.etree.ElementTree as ET
i=0
for filename in os.listdir("C:/Pascal_Annotation_Format-master/Pascal_Format/results/"): 
    filename=os.path.splitext(os.path.basename(filename))[0]
    print(filename)
    tree = ET.parse("C:/Pascal_Annotation_Format-master/Pascal_Format/results/"+filename+'.xml')
    root = tree.getroot()
    for objects in tree.iter('object'):
      #robndbox = objects.find('robndbox')
       #robndbox = objects.find('type').text
       #print(robndbox)
       for doc in objects.findall('robndbox'):
        xc=float(doc.find('cx').text)
        yc=float(doc.find('cy').text)
        width=float(doc.find('w').text)
        height=float(doc.find('h').text)
        angle=float(doc.find('angle').text)
        xmin= (xc-(width/2))
        ymin = (yc-(height)/2)
        xmax= (xc+(width/2))
        ymax = (yc+(height)/2)
        #print(xmin)
        #print(ymin)
        #print(xmax)
        #print(ymax)
       for doc in objects.findall('robndbox/cx'):
           doc.tag="xmin"
           doc.text=str(xmin)
       for doc in objects.findall('robndbox/cy'):
           doc.tag="ymin"
           doc.text=str(ymin)
       for doc in objects.findall('robndbox/w'):
           doc.tag="xmax"
           doc.text=str(xmax)
       for doc in objects.findall('robndbox/h'):
           doc.tag="ymax" 
           doc.text=str(ymax)           
    tree.write("C:/Pascal_Annotation_Format-master/Pascal_Format/results/"+filename+'.xml')
        
    i +=1
