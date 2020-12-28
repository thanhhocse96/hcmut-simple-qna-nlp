import pandas as pd
from collections import namedtuple

from data.student import Student
import constants as const

# Load CSV => List(Student)
def loadStudents(students_csv_path):
    # CSV => Pandas Dataframe
    students_df = pd.read_csv(students_csv_path, header = 0, names = const.STUDENTS_HEADER_LIST)

    # PandasDF => List(Student)
    # Ref_1 - convert dict => object [namedtuple]: https://www.kite.com/python/answers/how-to-convert-a-dictionary-into-an-object-in-python
    # Ref_2 - pandas to list: https://stackoverflow.com/a/40788179
    # Ref_3 - Using short name for 'orient' is deprecated => https://stackoverflow.com/a/64695691
    students_list = [(namedtuple("Student", row.keys())(*row.values())) for row in students_df.to_dict('records')]
    return students_list