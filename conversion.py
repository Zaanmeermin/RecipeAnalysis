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