import pandas as pd

import constants as const
from baseNLP.word import Word

corpus = pd.read_csv(const.CORPUS_CSV)

def main():
    print(corpus)

if __name__ == "__main__":
    main()