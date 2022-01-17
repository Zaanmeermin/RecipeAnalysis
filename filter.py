import csv
from conversion import *

# ingredients = {}

# with open('wordFrequenciesClean.csv', mode='r') as inp:
#     reader = csv.reader(inp)
#     for row in reader:
#         print(row)

# print(dict_from_csv)

# TODO:
# - convert wordFreq and synonyms to dicts
# - (initialize combinedWordFreq to be a dict filled with only the chosen synonyms) not sure if necessary
# - go through all words in wordFreq
#   - for every word, check if the word is in synonyms, 
#       - if yes use the 'main' spelling, if no use regular spelling
#       - for every manuscript
#           - if already in combinedWordFreq, combine and sort lists
#           - if not, just add manuscript to word dict

def combineSynonyms(wordFreq, synonyms):
    combinedWordFreq = {}

    for word in wordFreq:
        print("word: ", word)
        main = ""
        # Get corresponding 'main' spelling, if it exists
        for synonym in synonyms:
            if(word in synonyms[synonym]):
                main = synonym
                break
        if(main == ""): main = word
        print(word, " should be written as ", main)

        if(main in combinedWordFreq):
            for fileName in wordFreq[word]:
                print(fileName)
                if fileName in combinedWordFreq[main]:
                    print("known filename")
                    combinedWordFreq[main][fileName] += wordFreq[word][fileName]
                    combinedWordFreq[main][fileName] = sorted(combinedWordFreq[main][fileName])
                else:
                    print("new filename")
                    combinedWordFreq[main][fileName] = wordFreq[word][fileName]
        else:
            combinedWordFreq[main] = wordFreq[word]
    return combinedWordFreq
 
# practice wordFreq
wordFreq = \
{
    'alluijn': 
    {
        'BTMM0576': [9, 11, 11, 12, 12, 15, 17, 19, 19],
        'BTMM0575': [8, 8]
    },
    'aluiijn': 
    {
        'BTMM0575': [32, 32, 33]
    },
    'aluijn':
    {
        'BTMM0575': [5, 8, 9, 11, 11, 11, 12, 12, 12, 13, 14, 14, 14, 15, 16, 16, 16, 18, 19, 19, 20, 21, 22, 22, 22, 24, 24, 25, 25, 26, 26, 27, 27, 27, 28, 28, 30, 30, 31, 31],
        'BTMM0011': [4, 4, 5, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16],
        'BTMM0576': [4],
        'BTMM1427': [17]
    },
    'aluin':
    {
        'BTMM1427': [3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 15, 15, 15, 16, 17, 17, 19, 19, 20, 20, 24, 30, 30, 30, 32, 33, 33, 33, 33, 34, 34, 35, 18, 18, 37, 37, 38, 39, 39, 44, 46, 47, 47, 47, 48, 48, 48, 48, 49, 49, 49, 50, 50, 54, 57, 57, 59, 59, 59, 59, 59, 62, 69, 70, 71, 71, 71, 74],
        'BTMM0225': [3, 5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 9, 9, 10, 10, 11, 11, 12, 12, 13],
        'BTMM0092': [2, 3, 4, 4, 4, 4, 5, 5, 7, 16, 16, 20, 22, 23],
        'BTMM0091': [3, 4, 4, 4, 4, 5, 6, 6, 7, 7, 9, 10, 10],
        'BTMM0575': [11, 11, 27, 33, 33],
        'BTMM0585': [2, 3, 5, 5],
        'BTMM0177': [15, 15, 23, 23],
        'BTMM0576': [23]
    }
}

# practice synonyms
synonyms = {'aluin': ['alluijn', 'aluiijn', 'aluijn']}


combinedWordFreq = combineSynonyms(wordFreq, synonyms)
print(combinedWordFreq)
columns = ['word', 'total frequency', 'BTMM0576', 'BTMM0575', 'BTMM0011', 'BTMM1427', 'BTMM0225', 'BTMM0092', 'BTMM0091', 'BTMM0585', 'BTMM0177']
makeCSV('combinedWordFreq.csv', combinedWordFreq, columns)