import pandas as pd

df=pd.read_csv("Test1/employees.csv")

print(df.head())
print(df.info())
print(df.describe())

print(df["name"])

print(df[["name","salary"]])

print(df[df["city"]=="Chennai"]["name"])
print("salary above 50000: ",len(df[(df["salary"]>5000) & (df["department"]=="IT")]))
print("IT Department: ",df[df["department"] == "IT"]["name"])
print(df[(df["department"]=="IT" )& (df["city"]=="Bangalore")]["name"])