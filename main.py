import pandas as pd
from collections import namedtuple

from data.student import Student
from utils.students_loader import loadStudents

import constants as const
from baseNLP.word import Word

corpus = pd.read_csv(const.CORPUS_CSV)

def main():
    #Load list of Students
    students = loadStudents(const.STUDENTS_CSV)

if __name__ == "__main__":
    main()