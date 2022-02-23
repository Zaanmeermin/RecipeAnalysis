from packed_bubbles import *
from conversion import *

# Get the data from the selected manuscripts
def selectData(fileName, manuscripts, n):
    # TODO
    # - Go through all the words in wordFreq
    # - Overwrite total frequency with occurences only in selected manuscripts
    # - Sort words by updated total frequency
    # - Select the n top words and corresponding total frequencies

    wordFreq = CSVtoWordFreq(fileName)

    # Go through all the words
    for word in wordFreq:
        # Overwrite total frequency with occurences only in selected manuscripts
        totalFreq = 0

        for manuscript in wordFreq[word]:
            if(manuscript in manuscripts):
                totalFreq += len(wordFreq[word][manuscript])
        wordFreq[word]['total frequency'] = totalFreq
    
    # Sort words by updated total frequency
    topWords = sorted(wordFreq, key = lambda k: wordFreq[k]['total frequency'], reverse=True)[:n]
    topFrequencies = [wordFreq[word]['total frequency'] for word in topWords]
    
    return topWords, topFrequencies

# all
manuscripts = ['BTMM1427', 'BTMM0010', 'BTMM1566', 'BTMM0575', 'BTMM0011', 'BTMM0160', 'BTMM0576', 'BTMM0584', 'BTMM0225', 'BTMM0091', 'BTMM0177', 'BTMM0178', 'BTMM0176', 'BTMM0585', 'BTMM0092', 'BTMM1062']

# 1st half 19th century
# manuscripts = ['BTMM1427', 'BTMM0010', 'BTMM1566', 'BTMM0575', 'BTMM0011', 'BTMM0160', 'BTMM0576', 'BTMM0584', 'BTMM0225']

# 2nd half 19th century
# manuscripts = ['BTMM0091', 'BTMM0177', 'BTMM0178', 'BTMM0176', 'BTMM0585', 'BTMM0092', 'BTMM1062']

# manuscripts = ['BTMM0091']

colours = \
    {
        'blauwhout': '#5b1985',
        'meekrap': '#d43d0b',
        'geelhout': '#e6e610',
        'indigo': '#0a0869',
        'roodhout': '#94091d',
        'sandelhout': '#d43b20',
        'orseille': '#db357d',
        'kurkuma': '#ebd810',
        'cochenille': '#c90a34',
        'blauwhoutextract': '#5b1985',
        'auramin': '#f5e90c',
        'wouw': '#c0db0d',
        'fuchsine': '#eb13aa',
        'alizarine': '#ab001a',
        'rocceline': '#c71b08',
        'antraceen': '#945f0f',
        'tuchroth': '#e33e19',
        'aziet': '#7d2c00',
        'indigokarmijn': '#0016d9',
        'roodpot': '#b52b1b',
        'koffie': '#401e06',
        'quercitron': '#f0f041'
    }

# n specifies how many data points you want to include.
# n = 7
# topWords, topFrequencies = selectData("combinedWordFreqNoTannins.csv", manuscripts, n)


# European dyes
topWords = ['meekrap', 'wouw']
topFrequencies = [515, 47]

# International dyes
# topWords = ['blauwhout', 'geelhout', 'indigo', 'roodhout', 'sandelhout', 'orseille',
# 'kurkuma', 'cochenille', 'quercitron']
# topFrequencies = [879, 325, 163, 135, 134, 99, 88, 82, 27]

# Synthetic dyes
# topWords = ['aziet', 'maquin', 'indigokarmijn', 'auramin', 'koffie', 'rocceline', 'fuchsine', 'antraceen', 'tucroth']
# topFrequencies = [74, 73, 59, 52, 51, 33, 29, 28, 26]


hexColours = [colours[word] if word in colours else '#6e6e6e' for word in topWords]
print(topWords)
print(topFrequencies)

# Initialize bubble chart with a list of the numbers and possibly a bubble spacing
bubble_chart = BubbleChart(area=topFrequencies, bubble_spacing=0.1)

bubble_chart.collapse()

fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))

# When plotting, specify the words and the corresponding colours.
bubble_chart.plot(
    ax, topWords, hexColours)

# Some additional settings
ax.axis("off")
ax.relim()
ax.autoscale_view()

# Set the title
ax.set_title('Meest genoemde stoffen in ' + ", ".join(manuscripts))

plt.show()