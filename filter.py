from conversion import *

# Goes though the wordFreq dictionary and combines all the synonyms as specified 
# in the synonyms dictionary. Stores and returns this in a new dictionary.
def combineSynonyms(wordFreq, synonyms):
    combinedWordFreq = {}

    for word in wordFreq:
        main = ""
        # Get corresponding 'main' spelling, if it exists
        for synonym in synonyms:
            if(word in synonyms[synonym]):
                main = synonym
                break
        if(main == ""): main = word

        if(main in combinedWordFreq):
            for fileName in wordFreq[word]:
                if fileName in combinedWordFreq[main]:
                    print(combinedWordFreq[main][fileName], " + ", wordFreq[word][fileName])
                    combinedWordFreq[main][fileName] += wordFreq[word][fileName]
                    combinedWordFreq[main][fileName] = sorted(combinedWordFreq[main][fileName])
                    print(" = ", combinedWordFreq[main][fileName])
                    print()
                else:
                    combinedWordFreq[main][fileName] = wordFreq[word][fileName]
        else:
            combinedWordFreq[main] = wordFreq[word]
    return combinedWordFreq

wordFreq = CSVtoWordFreq("combinedWordFreq.csv")
synonyms = CSVtoSynonyms("synonyms.csv")

print(wordFreq)
print()
print(synonyms)
print()

combinedWordFreq = combineSynonyms(wordFreq, synonyms)
print(combinedWordFreq)
# data 1
# columns = ['word', 'total frequency', 'BTMM0576', 'BTMM0575', 'BTMM0011', 'BTMM1427', 'BTMM0225', 'BTMM0092', 'BTMM0091', 'BTMM0585', 'BTMM0177']

# data 2
# columns = ['word', 'total frequency', 'BTMM0010', 'BTMM0160', 'BTMM0178', 'BTMM0584', 'BTMM1062', 'BTMM1566']

# All data
columns = ['word', 'total frequency', 'BTMM1427', 'BTMM0010', 'BTMM1566', 'BTMM0575', 'BTMM0011', 'BTMM0160', 'BTMM0576', 'BTMM0584', 'BTMM0225', 'BTMM0091', 'BTMM0177', 'BTMM0178', 'BTMM0176', 'BTMM0585', 'BTMM0092', 'BTMM1062']

wordFreqtoCSV('combinedWordFreq.csv', combinedWordFreq, columns)