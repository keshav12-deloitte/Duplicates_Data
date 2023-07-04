import pandas
import math
import pandas as pd



#  https://github.com/blingenf/copydetect
# repo link

class HomeScreen:

    def sum_two_numbers(self, a, b):
        c = a + b
        return c

    def csv_reader(self):
        # reading the CSV file
        csvFile = pandas.read_csv('Giants.csv')
        # displaying the contents of the CSV file
        print(csvFile)

    def read_excelSheet_local(self, path):
        dataframe1 = pd.read_excel(path)
        print(dataframe1)
