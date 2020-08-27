import pandas as pd 

dataframe = pd.read_csv('UserData.csv')
#print (dataframe)

df1 = pd.DataFrame({"User":["Ananya"], 
                         "Range":[5],
                         "Avg": [1],
                         "Smallest":[4],
                         "Good":[3],
                         "Bad":[1],
                         "Acceptable":[5],
                         "Angles":["[7,6,9,10]"]}) 

dataframe = dataframe.append(df1, ignore_index = True)
print (dataframe)
dataframe.to_csv('UserData.csv', index=False)