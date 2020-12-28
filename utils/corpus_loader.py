import pandas as pd

from utils.no_accent_vietnamese import no_accent_vietnamese

from baseNLP.corpus import Corpus
from baseNLP.word import Word

import constants as const

def category_define(cat_string):
    if cat_string == "N":
        return const.WORD_CAT.NOUN
    if cat_string == "V":
        return const.WORD_CAT.VERB
    if cat_string == "PREP":
        return const.WORD_CAT.PREP
    if cat_string == "NUM":
        return const.WORD_CAT.NUM
    if cat_string == "ADV":
        return const.WORD_CAT.ADV
    if cat_string == "PRO":
        return const.WORD_CAT.PRO
    if cat_string == "NAME":
        return const.WORD_CAT.NAME
    return const.WORD_CAT.OTHER

def corpus_loader(corpus_file, name_entity_file):
    corpus_df = pd.read_csv(corpus_file, header = 0, names = const.CORPUS_HEADER_LIST).sort_values(const.CORPUS_HEADER_LIST[1])
    name_df = pd.read_csv(name_entity_file, header = 0, names = const.STUDENTS_HEADER_LIST)

    corpus_list = list([
        Corpus(list([]), const.N_GRAM.ONE_GRAM),
        Corpus(list([]), const.N_GRAM.TWO_GRAM),
        Corpus(list([]), const.N_GRAM.MORE_GRAM)
    ])

    # Add word from corpus.csv file
    for row in corpus_df.to_dict('records'):
        
        corpus_word = Word(
            no_accent_vietnamese(row[const.CORPUS_HEADER_LIST[0]]).upper() + str(row[const.CORPUS_HEADER_LIST[3]]),
            row[const.CORPUS_HEADER_LIST[0]].lower(),
            category_define(row[const.CORPUS_HEADER_LIST[2]])
        )

        if row[const.CORPUS_HEADER_LIST[1]] == 1:
            corpus_list[0].word_list.append(corpus_word)
        if row[const.CORPUS_HEADER_LIST[1]] == 2:
            corpus_list[1].word_list.append(corpus_word)

    # Add word from students.csv file
    name_list = []
    for ele in name_df[const.STUDENTS_HEADER_LIST[0:5]].values.flatten():
        if ele not in name_list:
            name_list.append(ele)
    
    for ele in name_list:
        if ele not in corpus_list[2].word_list:
            corpus_word = Word(
                "NAME",
                ele.lower(),
                const.WORD_CAT.NAME
            )
            corpus_list[2].word_list.append(corpus_word)

    return corpus_list