#!/usr/bin/env python3 

import sys
import re
import os
from pathlib import Path

def getIngredientList(dict, ingredient):
    if(ingredient in dict):
        temp =  sorted(dict[ingredient], key = lambda k: len(dict[ingredient][k]), reverse=True)
        return [(x, dict[ingredient][x]) for x in temp]

def getFileList(dict, file):
    return sorted([(key, dict[key][file]) for key in dict if file in dict[key]], key=lambda k: len(k[1]), reverse=True)    

def get(dict, ingredient, file):
    if(ingredient in dict and file in dict[ingredient]):
        return dict[ingredient][file]

# Print the frequency dictionary, to reduce output the minimal frequency 
# required can be specified (default is 2) 
def printDict(pairFreq, minFreq=2):
    pairSorted = sorted(pairFreq, key=lambda k: len(pairFreq[k]), reverse=True)
    for pair in pairSorted:
        if(len(pairFreq[pair]) >= minFreq):
            print(str(pair) + ": " + str(pairFreq[pair]))

def analyseFile(f, fileName):
    pageNum = "0001"
    prevWord = ""

    for word in f.read().lower().split():
        # Skip words not containing letters.
        # Also skip common words to denote weight, to avoid matching pairs with these.
        if(not re.search('[a-z]', word) or word == "pond"):
            prevWord = ""
            continue

        word = word.strip('.!?:;,()')
        # print(word)
        if(word.startswith(fileName.lower())):
            pageNum = word[len(fileName) + 1:]
        if(word in wordFreq):
            if(fileName in wordFreq[word]):
                wordFreq[word][fileName].append(pageNum) 
            else:
                wordFreq[word][fileName] = [pageNum]
        else:
            wordFreq[word] = {fileName: [pageNum]}

        pair = (prevWord, word)
        if(not(pair[0] == "" or pair[1] == "")):
            if(pair in pairFreq):
                if(fileName in pairFreq[pair]):
                    pairFreq[pair][fileName].append(pageNum)
                else:
                    pairFreq[pair][fileName] = [pageNum]
            else:
                pairFreq[pair] = {fileName: [pageNum]}

        prevWord = word


# Try to open file
if(len(sys.argv) < 2):
    print("Please specify a folder to analyse.")
    sys.exit()

folderName = sys.argv[1]
folder = Path(folderName)

# Initialize dictionary
wordFreq = {}
pairFreq = {}

for(dirpath, _, fileNames) in os.walk(folder):
    for fileName in fileNames:
        with open(os.path.join(dirpath, fileName)) as f:
            # print(dirpath, fileName) 
            path = os.path.join(dirpath, fileName)
            try:
                f = open(path)
            except FileNotFoundError:
                print("File not found.")
                sys.exit()

            analyseFile(f, fileName)


# [print(x) for x in getFileList(pairFreq, 'BTMM0091') if len(x[1]) > 6]
[print(x) for x in getIngredientList(wordFreq, 'galnoten')]
# print(get(pairFreq, ('indigo', 'carmin'), 'BTMM0091'))

