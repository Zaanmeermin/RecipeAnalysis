from conversion import *

# Combine two wordfrequency dictionaries. 
# May contain the same words, but both feature different files.
def combineDicts(wordFreq1, wordFreq2):
    combinedWordFreq = wordFreq1

    for word in wordFreq2:
        # Word is in dict, add additional books
        if word in combinedWordFreq:
            for book in wordFreq2[word]:
                combinedWordFreq[word][book] = wordFreq2[word][book]
        # Word not in dict, can add everything at once
        else:
            combinedWordFreq[word] = wordFreq2[word]

    return combinedWordFreq

wordFreq1 = CSVtoWordFreq("data1.csv")
wordFreq2 = CSVtoWordFreq("data2.csv")

combinedWordFreq = combineDicts(wordFreq1, wordFreq2)

print(combinedWordFreq)
# columns = ['word', 'total frequency', 'BTMM0576', 'BTMM0575', 'BTMM0011', 'BTMM1427', 'BTMM0225', 'BTMM0092', 'BTMM0091', 'BTMM0585', 'BTMM0177']
columns = ['word', 'total frequency', 'BTMM1427', 'BTMM0010', 'BTMM1566', 'BTMM0575', 'BTMM0011', 'BTMM0160', 'BTMM0576', 'BTMM0584', 'BTMM0225', 'BTMM0091', 'BTMM0177', 'BTMM0178', 'BTMM0176', 'BTMM0585', 'BTMM0092', 'BTMM1062']
wordFreqtoCSV('combinedWordFreq.csv', combinedWordFreq, columns)