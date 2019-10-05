import numpy as np
import pandas as pd

x=pd.Series([1,2,3,4,5])

x+100   #adding 100 with each of the values of the series
x**2  # squaring each of the values of the series
x>2  #checking wheather the values of x is greater than 2 or not

larger=x>2
larger.any()  #if any value is true then it any() returns true
larger.all() #if all the values are true then all() returns true

#apply function
def fund(x):
    if x%2==0:
        return x**2
    else:
        return x**3
x.apply(fund)  

x.astype(np.float) #convert data type

#copy
y=x
y[0]=100
y #change can be visible
x #the first value of x is also changed

y=x.copy()
y[0]=100
y #now change can also visible
x #nothing changes because of y

#Datafarme
data=[9,8,7,6,5,4,3,2,1]
df=pd.DataFrame(data,columns=["x"])

#One column as Series
dataSeries=df["x"]

#adding more columns
df["square"]=df["x"]**2
df["factorial"]=df["x"].apply(np.math.factorial)
df["true"]=df["x"]>4

#dropping a column
df.drop("square",1)

#selecting multiple column
df[["x","true"]]

#describe
df.describe()