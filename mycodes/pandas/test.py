import pandas as pd

df = pd.read_csv('~/Desktop/random_test/deep_learning/udemy_course/pytorch_test/course_mat/00-Crash-Course-Topics/01-Crash-Course-Pandas/bank.csv')

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df)
    
