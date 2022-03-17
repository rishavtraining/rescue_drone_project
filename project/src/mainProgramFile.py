'''
* Project Name: Unmanned Aerial System for flood disaster emergency response 
                and rescue management

* Author List: Krishna Nimbalkar

* Filename: mainProgramFile.py

* Functions: process()

* Global Variables: NA

'''
#########################################################################
#   Project Name  : Unmanned Aerial System for flood disaster emergency #
#                  response and rescue management                       #
#                                                                       #
#   Author Name   : Krishna Nimbalkar                                   #
#   Last Modified : 13/01/2021                                          #
#                                                                       #
#   Discription   : This program is main program to execute             #
#                                                                       #
#########################################################################

import sys
import os
import time
import multiprocessing

import main
import waypoint_navigation

import threading


def process():

    t1 = threading.Thread(target=waypoint_navigation.mission)
    t1.start()
    # with inp and out
    os.system("python main.py --model ../model_data/yolov2.weights --config ../model_data/yolov2.cfg --classes ../model_data/coco_classes.txt --input ../media/sample_video.mp4 --output ../out/sample_output.avi")

    # inp from cam write out
    #os.system("python main.py --model ../model_data/yolov2.weights --config ../model_data/yolov2.cfg --classes ../model_data/coco_classes.txt --output ../out/sample_output.avi")


    # inp from cam do not write out
    #os.system("python main.py --model ../model_data/yolov2.weights --config ../model_data/yolov2.cfg --classes ../model_data/coco_classes.txt")

    t1.join()


if __name__ == '__main__':

    process()
    sys.exit("exit the sys main program")

