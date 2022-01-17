import csv

# Function to convert from dict to CSV.
def makeCSV(fileName, dict, columns):
    with open(fileName, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()

        for word in dict:
            freq = sum([len(dict[word][f]) for f in dict[word]])
            row = {'word': word, 'total frequency': freq}
            row.update(dict[word])
            writer.writerow(row)

# Convert from csv to dictionary.
def readCSV(fileName):
    wordFreq = {}
    with open(fileName, mode='r') as inp:
        reader = csv.reader(inp)
        columns = reader.__next__()
        for row in reader:
            wordFreq[row[0]] = {}
            print(row)
            for i, item in enumerate(row[1:]):
                if(not item == ""):
                    wordFreq[row[0]][columns[i + 1]] = item 

    print(wordFreq)

readCSV('wordFrequenciesClean.csv')