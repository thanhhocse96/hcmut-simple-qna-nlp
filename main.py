import pandas as pd
from collections import namedtuple

#Data
from data.student import Student
#Utils
from utils.students_loader import loadStudents
#Const
import constants as const
#NLP Base
from baseNLP.word import Word


#Load list of Students
students = loadStudents(const.STUDENTS_CSV)
#Load corpus
corpus = pd.read_csv(const.CORPUS_CSV)

def main():
    print(students)

if __name__ == "__main__":
    main()