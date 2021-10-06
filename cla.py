import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv
import pandas as pd

df=pd.read_csv("data.csv")
data=df["temp"].tolist()
population_mean=statistics.mean(data)
std_dev=statistics.stdev(data)
print("mean->",population_mean)
print("std_dev->",std_dev)

def show_fig(mean_list):
  df=mean_list
  fig=ff.create_distplot([data],["temp"],show_hist=False)
  fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
  fig.show()
