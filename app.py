import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('owid-covid-data.csv')



kenya=df[df['location']=='Kenya']
print(kenya.head())

usa=df[df['location']=='USA']
print(usa.head())

df['date'] = pd.to_datetime(df['date'])
print(df['date'].dtype)

x= df['totalcases']
y=df['time']




