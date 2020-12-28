import pandas as pd
from collections import namedtuple

#Data
from data.student import Student
#Utils
from utils.students_loader import loadStudents
from utils.corpus_loader import corpus_loader
#Const
import constants as const
#NLP Base
from baseNLP.word import Word


#Load list of Students
students = loadStudents(const.STUDENTS_CSV)
#Load corpus
corpus_list = corpus_loader(const.CORPUS_CSV, const.STUDENTS_CSV)

def main():
    # print(students)
    print(corpus_list)
    pass

if __name__ == "__main__":
    main()