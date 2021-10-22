#!/usr/bin/env python3 

import sys
import re

# Print the frequency dictionary, to reduce output the minimal frequency 
# required can be specified (default is 2) 
def printDict(pairFreq, minFreq=2):
    pairSorted = sorted(pairFreq, key=lambda k: len(pairFreq[k]), reverse=True)
    for pair in pairSorted:
        if(len(pairFreq[pair]) >= minFreq):
            print(str(pair) + ": " + str(pairFreq[pair]))

# Try to open file
if(len(sys.argv) < 2):
    print("Please specify a filename.")
    sys.exit()

fileName = sys.argv[1]

try:
    f = open(fileName)
except FileNotFoundError:
    print("File not found.")
    sys.exit()

# Shorten filename
fileName = fileName[len("data/"):]

# Initialize dictionary
wordFreq = {}
pairFreq = {}
pageNum = "0001"
prevWord = ""

# key: word
# value: list consisting of the page numbers where the word was mentioned
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
        wordFreq[word].append(pageNum) 
    else:
        wordFreq[word] = [pageNum]

    pair = (prevWord, word)
    if(not(pair[0] == "" or pair[1] == "")):
        if(pair in pairFreq):
            pairFreq[pair].append(pageNum)
        else:
            pairFreq[pair] = [pageNum]

    prevWord = word

printDict(wordFreq, 3)
printDict(pairFreq, 3)
