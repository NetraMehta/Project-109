import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv('StudentsPerformance.csv')
data = df['reading score'].tolist()

mean = sum(data)/len(data)
print('Mean is', mean)

median = statistics.median(data)
print('Median is', median)

mode = statistics.mode(data)
print('Mode is', mode)

std_dev = statistics.stdev(data)
print('Standard Deviation is', std_dev)

first_std_dev_start, first_std_dev_end = mean - std_dev, mean + std_dev
second_std_dev_start, second_std_dev_end = mean - (2*std_dev), mean + (2*std_dev)
third_std_dev_start, third_std_dev_end = mean - (3*std_dev), mean + (3*std_dev)

print('First standard deviation is', first_std_dev_start, 'and', first_std_dev_end)
print('Second standard deviation is', second_std_dev_start, 'and', second_std_dev_end)
print('Third standard deviation is', third_std_dev_start, 'and', third_std_dev_end)

fig = ff.create_distplot([data], ['result'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.03], mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [first_std_dev_start, first_std_dev_start], y = [0, 0.03], mode = 'lines', name = 'Standard deviation 1'))
fig.add_trace(go.Scatter(x = [first_std_dev_end, first_std_dev_end], y = [0, 0.03], mode = 'lines', name = 'Standard deviation 1'))
fig.add_trace(go.Scatter(x = [second_std_dev_start, second_std_dev_start], y = [0, 0.03], mode = 'lines', name = 'Standard deviation 2'))
fig.add_trace(go.Scatter(x = [second_std_dev_end, second_std_dev_end], y = [0, 0.03], mode = 'lines', name = 'Standard deviation 2'))
fig.add_trace(go.Scatter(x = [third_std_dev_start, third_std_dev_start], y = [0, 0.03], mode = 'lines', name = 'Standard deviation 3'))
fig.add_trace(go.Scatter(x = [third_std_dev_end, third_std_dev_end], y = [0, 0.03], mode = 'lines', name = 'Standard deviation 3'))
fig.show()

list_of_data_within_1_std_dev = [result for result in data if result > first_std_dev_start and result < first_std_dev_end]
list_of_data_within_2_std_dev = [result for result in data if result > second_std_dev_start and result < second_std_dev_end]
list_of_data_within_3_std_dev = [result for result in data if result > third_std_dev_start and result < third_std_dev_end]

print('{}% of data lies within 1 standard deviation'.format(len(list_of_data_within_1_std_dev)*100.0/len(data)))
print('{}% of data lies within 2 standard deviation'.format(len(list_of_data_within_2_std_dev)*100.0/len(data)))
print('{}% of data lies within 3 standard deviation'.format(len(list_of_data_within_3_std_dev)*100.0/len(data)))