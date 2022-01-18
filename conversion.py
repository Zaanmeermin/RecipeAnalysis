import csv
import ast

# Function to convert from dict to CSV.
def wordFreqtoCSV(fileName, dict, columns):
    with open(fileName, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()

        for word in dict:
            freq = sum([len(dict[word][f]) for f in dict[word]])
            row = {'word': word, 'total frequency': freq}
            row.update(dict[word])
            writer.writerow(row)

# Convert from csv to dictionary.
def CSVtoWordFreq(fileName):
    wordFreq = {}
    with open(fileName, mode='r') as inp:
        reader = csv.reader(inp)
        columns = reader.__next__()
        for row in reader:
            wordFreq[row[0]] = {}
            for i, item in enumerate(row[2:]):
                if(not item == ""):
                    wordFreq[row[0]][columns[i + 2]] = ast.literal_eval(item)

    return wordFreq

def CSVtoSynonyms(fileName):
    synonyms = {}
    with open(fileName, mode='r') as inp:
        reader = csv.reader(inp)
        for row in reader:
            synonyms[row[0]] = row[1]
    
    return synonyms

if __name__ == "__main__":
    synonyms = CSVtoSynonyms("synonyms.csv")
    # print(synonyms)
    CSVtoWordFreq('wordFrequencies.csv')