#!/usr/bin/env python3 
"""""
Semma Raadschelders
Textielmuseum Tilburg
2021
"""

import sys
import re
import os
from pathlib import Path
from conversion import *

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
    pageNum = 1
    prevWord = ""

    text = f.read().lower()
    # Removes hyphens and lines of -
    text = re.sub("-+[\t ]*\n\s*", "", text)

    for word in text.split():
        # print(word)
        # Skip words not containing letters.
        # Also skip common words to denote weight, to avoid matching pairs with these.
        if(not re.search('[a-z]', word) or word == "pond"):
            prevWord = ""
            continue

        word = word.strip('.!?:;,()\"\'‘')
        # print(word)
        if(word.startswith(fileName.lower())):
            pageNum = int(word[len(fileName) + 1:].lstrip('0'))
        elif(word in wordFreq):
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

def analyseFolder(folder):
    for(dirpath, _, fileNames) in os.walk(folder):
        columns = ['word', 'total frequency'] + fileNames
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

    # sortedWords = sorted(wordFreq, key=lambda k: sum([len(wordFreq[k][f]) for f in wordFreq[k]]), reverse=True)
    
    # return sortedWords
    return columns

# Try to open file
if(len(sys.argv) < 2):
    print("Please specify a folder to analyse.")
    sys.exit()

folderName = sys.argv[1]
folder = Path(folderName)

wordFreq = {}
pairFreq = {}

columns = analyseFolder(folder)
wordFreqtoCSV('wordFrequencies.csv', wordFreq, columns)
wordFreqtoCSV('pairFrequencies.csv', pairFreq, columns)

# [print(x) for x in getFileList(pairFreq, 'BTMM0091') if len(x[1]) > 6]
# [print(x) for x in getIngredientList(wordFreq, 'galnoten')]
# print(get(pairFreq, ('indigo', 'carmin'), 'BTMM0091'))

