import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

def data_v():
    tweets = ["I love Boris. I do not like Lizz", "I love Lizz. I do not like Boris", "I Like strawberries. I do not like bananas", "Covid 19 is made by Bill Gates",
    "I love Apples but I think dentists actually hate them", "Democracy is the best form of government", "He loves Boris and Apples", "Covie 19 is a conspiracy theory"]
    allNouns = []
    for tweet in tweets:
        for (word, partOfSpeech) in TextBlob(tweet).pos_tags:
            if partOfSpeech[0] == 'N' and not (word == "@"):
                allNouns.append(word)
    nounFrequencies = {}
    for noun in allNouns:
        if noun in nounFrequencies:
            nounFrequencies[noun] += 1
        else:
            nounFrequencies[noun] = 1
    df = pd.DataFrame.from_dict(nounFrequencies, orient='index')
    df.reset_index(inplace=True)
    df.columns = ['Noun', 'Frequency']
    df.sort_values(by='Frequency', inplace=True, ascending=False)
    df = df.head(10)
    print(df)

    fig1, ax1 = plt.subplots()
    ax1.pie(df['Frequency'], labels=df['Noun'], autopct='%1.1f%%',)
    ax1.axis('equal')
    plt.show()

if __name__ == "__main__":
    data_v()



    





