#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
A module that can be used to compare two json files.
It does the following:
(1)  Find the common key, which have different values.
(2) Keys present only in File1.
(3) Keys present only in File2. 
"""
_author_="ARJUN PANDEY"
_License_="None"
_Version_="1.0.0"
import json
import os
import argparse

FILE1_PATH = "" # Path of first file,default is current path
FILE2_PATH = "" # path of second file,default is current path
COMM_KEY = {*{}} # place holder to hold unique keys with different values
FILE1_ADDITIONAL = {*{}} # place holder to hold additional key in FILE1
FILE2_ADDITIONAL = {*{}} # place holder to hold additional key in FILE2
FLAG = 0# TO check if there is any difference
parser = argparse.ArgumentParser(description='JSON DIFF')
parser.add_argument('-f1','--FILE1_PATH', help='First Json File')
parser.add_argument('-f2','--FILE2_PATH', help='Second Json file')
args = parser.parse_args()
FILE1_PATH = args.FILE1_PATH
FILE2_PATH = args.FILE2_PATH

class JsonDiff:
    def __init__(self, FILE1_PATH, FILE2_PATH):
        self.FILE1_PATH = FILE1_PATH
        self.FILE2_PATH = FILE2_PATH
        self.__diff()
    
    @staticmethod
    def json_diff(FILE1_PATH, FILE2_PATH):
        #Validating file is non-empty
        try:
            if os.path.getsize(FILE1_PATH) > 0 and os.path.getsize(FILE2_PATH) > 0:
                print ("INFO: Files exists and non-empty")
            elif os.path.getsize(FILE1_PATH) ==0:
                print ("File: {0} is empty". format(FILE1_PATH))     
                raise OSError("FILE: {0} is empty". format(FILE1_PATH)) 
            elif os.path.getsize(FILE2_PATH) ==0:
                print ("file: {0} is empty". format(FILE2_PATH))
                raise OSError("FILE: {0} is empty". format(FILE2_PATH))
        except OSError as e:
            print("Invalid file input: {0}".format(e))
        return JsonDiff(FILE1_PATH, FILE2_PATH)
        
    def __diff(self):
        diff_list = []
        with open(self.FILE1_PATH, 'r') as json1:
            json_dict1 = json.load(json1)
        with open(self.FILE2_PATH, 'r') as json2:
            json_dict2 = json.load(json2)
        if json_dict1.items() - json_dict2.items():
            diff_list = list(json_dict1.items() - json_dict2.items())
            if json_dict2.items() - json_dict1.items():
                diff_list.extend(list(json_dict2.items() - json_dict1.items()))
                for item in diff_list:
                    if item[0] in json_dict1 and item[0] in json_dict2:
                        COMM_KEY.add(item[0])
                    elif item[0] in json_dict1:
                        FILE1_ADDITIONAL.add(item[0])
                    elif item[0] in json_dict2:
                        FILE2_ADDITIONAL.add(item[0])
                
if __name__ == "__main__" :
    JsonDiff.json_diff(FILE1_PATH, FILE2_PATH)
    if COMM_KEY:
        print ("Key is common with different value: {0}".format(COMM_KEY))
    if FILE1_ADDITIONAL:
        print("Key present only in file: {0}- {1}".format(FILE1_PATH, FILE1_ADDITIONAL))
    if FILE2_ADDITIONAL:
        print ("Key present only in file: {0}- {1}".format(FILE2_PATH, FILE2_ADDITIONAL))
        FLAG = 1
    if FLAG == 0:
        print("JSON files are same")

            
        
    
