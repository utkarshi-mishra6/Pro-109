import random
import statistics
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("StudentPerformance.csv")
data = df["reading score"].tolist()
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_dev = statistics.stdev(data)


first_std_dev_start,first_std_dev_end = mean-std_dev,mean+std_dev
second_std_dev_start,second_std_dev_end = mean-(2*std_dev),mean+(2*std_dev)
third_std_dev_start,third_std_dev_end = mean-(3*std_dev),mean+(3*std_dev)

#fig = ff.create_distplot([dice_result],["Result"],show_hist=False)
#fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "MEAN"))

list_1_std_dev = [result for result in data if result>first_std_dev_start and result<first_std_dev_end]
list_2_std_dev = [result for result in data if result>second_std_dev_start and result<second_std_dev_end]
list_3_std_dev = [result for result in data if result>third_std_dev_start and result<third_std_dev_end]
print("{}% of data lies within 1 standard deviation".format(len(list_1_std_dev)*100.0/len(data)))
print("{}% of data lies within 2 standard deviation".format(len(list_2_std_dev)*100.0/len(data)))
print("{}% of data lies within 3 standard deviation".format(len(list_3_std_dev)*100.0/len(data)))