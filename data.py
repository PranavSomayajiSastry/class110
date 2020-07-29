import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df= pd.read_csv("data.csv")
data = df["temp"].to_list()
def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0, len(data)-1)
        value = data[random_index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
def showFig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df], ["temp"], show_list= False)
    fig.add_trace(go.Scatter(x=[mean, mean],y=[0,1], mode="lines", name="MEAN"))
    fig.show()
def setup():
    mean_list=[]
    for i in range(0, 1000):
        setOfMeans= randomSetOfMean(100)
        mean_list.append(setOfMeans)
    showFig(mean_list)
    mean= statistics.mean(mean_list)
    print("Mean of the Sampling Distribution: ", mean)
setup()
temp_mean= statistics.mean(data)
print("Mean of the Temperature: ",temp_mean)

def std_dev():
    mean_list=[]
    for i in range(0, 1000):
        setOfMeans= randomSetOfMean(100)
        mean_list.append(setOfMeans)
    showFig(mean_list)
    standDev= statistics.stdev(mean_list)
    print("Standard Deviation of the Sampling Distribution: ", standDev)
std_dev()