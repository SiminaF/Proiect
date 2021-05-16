import cv2
import os
import numpy as np
import json

#procesarea directorului de imagine/ citirea de la tastatura
path = input("Please enter the path to folder: ")
images = os.listdir(path)
image_classifier = {'red':[],
                    'green':[],
                    'blue':[]}
for image_name in images:
    #impartirea imaginilor dupa metoda RGB si distribuirea lor in grupuri
    image_path = path + '/' + image_name
    image = cv2.imread(image_path)
    (B, G, R) = cv2.split(image.astype('float'))
    blue_mean = np.mean(B)
    green_mean = np.mean(G)
    red_mean = np.mean(R)
    if(blue_mean >= green_mean and blue_mean >= red_mean):
        image_classifier['blue'].append(image_name)
    elif(green_mean >= blue_mean and green_mean >= red_mean):
        image_classifier['green'].append(image_name)
    else:
        image_classifier['red'].append(image_name)

#salvarea in fisierul json 
with open('output.json','w') as file_handler:
    json_obj = json.dumps(image_classifier,indent=4)
    file_handler.write(json_obj)
