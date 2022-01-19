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

manuscripts = ['BTMM0576', 'BTMM0575', 'BTMM0011', 'BTMM1427', 'BTMM0225', 'BTMM0092', 'BTMM0091', 'BTMM0585', 'BTMM0177']
# manuscripts = ['BTMM0585']

colours = \
    {
        'blauwhout': '#5b1985',
        'water': '#048eb8',
        'koper(II)sulfaat': '#1db6e0',
        'wijnsteen': '#b03813',
        'meekrap': '#d43d0b',
        'sumak': '#7a1507',
        'galnoten': '#73615e',
        'potas': '#bf5b28',
        'geelhout': '#e6e610',
        'aluin': '#e3e5e6'
    }

# n specifies how many data points you want to include.
n = 15
topWords, topFrequencies = selectData("combinedWordFreq.csv", manuscripts, n)
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