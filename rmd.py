import numpy as np 
import csv
import pandas as pd 
import plotly.express as px
with open("rmd.csv") as f:
    df = csv.DictReader(f)
    fig = px.line(df, x="Marks In Percentage", y="Days Present")
    fig.show()
def getDataSource(data_path):
    marks = []
    days = []
    with open(data_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return {"x":marks, "y":days}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation is", correlation[0,1])
def setUp():
    data_path = "rmd.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
setUp()