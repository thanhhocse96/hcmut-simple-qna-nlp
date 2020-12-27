import enum

CORPUS_CSV = "corpus/corpus.csv"
INPUT_QUESTION_NUMBER = 4

class SENTENCE_TYPE(enum.Enum):
    ASSERT = 1
    COMMAND = 2
    YNQUERY = 3
    WHQUERY = 4