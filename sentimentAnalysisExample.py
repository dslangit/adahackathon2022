import nltk
from textblob import TextBlob

if __name__ == '__main__':

    #Simple sentiment analysis of text
    text = "this is  good"
    print("The polarity is: " + str(TextBlob(text).sentiment.polarity) + ", The subjectivity is: " + str(
        TextBlob(text).sentiment.subjectivity) + "\n")

    # nltk.download('brown')
    # nltk.download('punkt')
    # nltk.download('averaged_perceptron_tagger')

    lines = open("@BorisJohnson.csv", encoding="utf-8").readlines()

    tweets = []
    for line in lines:
        row = line.split(",")
        tweet = row[0]
        tweets.append(tweet)

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
    print(nounFrequencies)

    print(TextBlob("Python is a high-level language.").noun_phrases)
