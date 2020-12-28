import enum

CORPUS_CSV = "corpus/corpus.csv"

STUDENTS_CSV = "input/students.csv"
STUDENTS_HEADER_LIST = list(["full_name", "id", "subject", "room", "day", "start_time", "class_length"])

INPUT_QUESTION_NUMBER = 4
INPUT_QUESTION_PATH_PREFIX = "input/question"
INPUT_QUESTION_PATH_POSTFIX = ".txt"

class SENTENCE_TYPE(enum.Enum):
    ASSERT = 1
    COMMAND = 2
    YNQUERY = 3
    WHQUERY = 4

