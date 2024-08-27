import pandas as pd

data  = {
    'Names' : ["Varsha","Ruchira","Kushagra","Sambhavi","Shubham","Devashree"],
    'RollNo' : [1, 60, 23, 9, 153, 2],
    'Salary' : [50000, 100000,15000,25000, 3000,40000]
}

series_1 = pd.Series(data['Names']) # single dim
dataframe = pd.DataFrame(data) # 2D
# print(dataframe)
# print(series_1)

# print(dataframe.head())
# print(dataframe.tail())

print(dataframe.describe()) # all mathematical values for your numeric data

print(dataframe.info())

print(dataframe[['Names', 'Salary']]) # extract / slice

print(dataframe[dataframe["Salary"] > 50000]) #queries


def max_salary(dataframe):
    max_sal = dataframe['Salary'][0]
    sec_max_sal = dataframe['Salary'][0]
    for i in dataframe['Salary']:
        if i >= max_sal:
            max_sal, sec_max_sal = i, max_sal
        elif i > sec_max_sal:
            sec_max_sal = i
    return sec_max_sal

print(max_salary(dataframe))

dataframe.to_csv("data.csv")