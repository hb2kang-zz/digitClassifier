
import numpy as np
import PIL
import os
import json
import shutil

import time

#lABELS

Label = [
    {
        'filename': 'Sample001',
        'label': 0
    },
    {
        'filename': 'Sample002',
        'label': 1
    },
    {
        'filename': 'Sample003',
        'label': 2
    },
    {
        'filename': 'Sample004',
        'label': 3
    },
    {
        'filename': 'Sample005',
        'label': 4
    },
    {
        'filename': 'Sample006',
        'label': 5
    },
    {
        'filename': 'Sample007',
        'label': 6
    },
    {
        'filename': 'Sample008',
        'label': 7
    },
    {
        'filename': 'Sample009',
        'label': 8
    },
    {
        'filename': 'Sample010',
        'label': 9
    },

]

#Create Total Dictionary Data Structure

def createDictionary(path):

    #Dictionary
    d = {}

    #iterate over length of labels

    parentDir = os.path.abspath(path)

    for n in range(len(Label)):
        #sample number
        folder_name = Label[n]['filename']
        #new path directory of sample
        new_path = parentDir + "/" + folder_name

        for subdir, dirs, files in os.walk(new_path):
            for file in files:
                # filename of image
                filename =  new_path + "/" + file
                # append to dictionary
                d[filename] = n

    return d

def createDirectory(dictionary, dir_name):

    path = "./digits"

    #new path of camera dir
    parentDir = os.path.abspath(path)
    new_dir = parentDir + "/" + dir_name

    #create new dir
    if not os.path.isdir(new_dir):
        os.makedirs(new_dir)

    #creates txt file
    txt_file = open(new_dir + "/labels", "w")

    count = 0

    #add images to new directory and creates ordered label txt file
    for key in dictionary:
        #copy images into new directory and renames for order
        shutil.copy2(key, new_dir + "/img" + str(count) + ".png")

        #write label in txt file
        txt_file.write(str(dictionary[key]) + "\n")

        #name of image
        count = count + 1

    txt_file.close()

    return


def main():

    start_time = time.time()

    d = createDictionary("./digits")

    createDirectory(d, "images2")

    elapsed_time = time.time() - start_time

    print(elapsed_time)

if __name__ == "__main__":
    main()
