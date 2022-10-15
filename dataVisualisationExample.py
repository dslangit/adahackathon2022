import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    borisJohnsonData = pd.read_csv("@BorisJohnson.csv")
    keirStarmerData = pd.read_csv("@Keir_Starmer.csv")
    bdf = pd.DataFrame(borisJohnsonData)
    kdf = pd.DataFrame(keirStarmerData)


    plt.scatter(bdf['Subjectivity'], bdf['Polarity'])
    plt.scatter(kdf['Subjectivity'], kdf['Polarity'])

    plt.show()

