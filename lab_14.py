import csv
import pandas as pd
data=pd.read_csv("hello.csv")
print(data.head(1))
print(data.tail(5))