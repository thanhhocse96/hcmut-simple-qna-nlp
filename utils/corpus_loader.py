import pandas as pd

from utils.no_accent_vietnamese import no_accent_vietnamese

from baseNLP.corpus import Corpus
from baseNLP.word import Word

import constants as const

def category_define(cat_string):
    pass

def corpus_loader(corpus_file, name_entity_file):
    corpus_df = pd.read_csv(corpus_file, header = 0, names = const.CORPUS_HEADER_LIST).sort_values(const.CORPUS_HEADER_LIST[1])
    name_df = pd.read_csv(name_entity_file, header = 0, names = const.STUDENTS_HEADER_LIST)

    # corpus_list = list(Corpus(list , const.N_GRAM.ONE_GRAM))
    for row in corpus_df.to_dict('records'):
        if row[const.CORPUS_HEADER_LIST[1]] == 1:
            
            print()
            corpus_word = Word(
                no_accent_vietnamese(row[const.CORPUS_HEADER_LIST[0]]).upper() + str(row[const.CORPUS_HEADER_LIST[3]]),
                
            )
        print(row)
