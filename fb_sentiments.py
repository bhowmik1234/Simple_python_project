import pandas as pd
import nltk
from nltk.sentiment.vadar import SentimentIntensityAnalyzer
nltk.downloader.download('vadar_lexicon')

file = "data_file.xlsml"
xl = pd.ExcelFile(file)
data_frame = xl.parse(xl.sheet_names[0])
data_frame = list(data_frame['Timeline'])
print(data_frame)

sid = SentimentIntensityAnalyzer()
str1 = "UTC+07:56"

for data in data_frame:
    a = data.find(str1)

    if(a == -1):
        ss = sid.polarity_scores(data)
        print(data)
        for i in ss:
            print(i, ss[i])
            