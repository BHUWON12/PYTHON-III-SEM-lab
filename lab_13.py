import pandas as pd
one=pd.DataFrame({'name':['teju','gouri'],'age':[19,20]},index=[1,2])
two=pd.DataFrame({'name':['manisha','arpit'],'age':[23,24]},index=[3,4])
print(pd.concat([one,two]))