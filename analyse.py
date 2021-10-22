#!/usr/bin/env python3 


# TODO: trim interpunction


import sys
import re

def printDict(dict) :
    for word in dict:
        print(word, ":", dict[word])


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

# Initialize dictionary
wordFreq = {}
pageNum = "BTMM0091_003"

# key: word
# value: list consisting of the page numbers where the word was mentioned
for word in f.read().lower().split():
    # Skip words not containing letters.
    if(not re.search('[a-z]', word)):
        continue

    print(word)
    if(word.startswith(fileName.lower())):
        pageNum = word[len(fileName):]
    if(word in wordFreq):
        wordFreq[word].append(pageNum) 
    else:
        wordFreq[word] = [pageNum]

# printDict(wordFreq)