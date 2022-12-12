from aranorm import normalize_arabic_text
from nltk.corpus import stopwords
from nltk import word_tokenize
import pandas as pd


def normlizeComment(file1,file2):

    with open(file1, 'r') as file1:
        with open(file2, 'w',newline='') as file2:
            for row in file1:
       
       
                file2.write(normalize_arabic_text(row))
                file2.write('\n')



def removeStopWords(file1,file2):

    arabicStopWords= stopwords.words("arabic")

    with open(file1, 'r') as file1:
        with open(file2, 'w',newline='') as file2:

            for row in file1:
                tokenizedRow = word_tokenize(row)
                commentWithNoStopWords= ' '.join([i for i in tokenizedRow if i not in arabicStopWords])
                file2.write(commentWithNoStopWords)
                file2.write('\n')

normlizeComment('comments','normlizedComments')
removeStopWords('normlizedComments','commentsWithNoStopWords')
       
read_file = pd.read_csv (r'commentsWithNoStopWords')
read_file.to_csv (r'cleanComments.csv', index=None)