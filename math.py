import pandas as pd
import statistics

df = pd.read_csv('data.csv')
mathScore = df['math score'].tolist()

mean = statistics.mean(mathScore)
median = statistics.median(mathScore)
mode = statistics.mode(mathScore)
stdev = statistics.stdev(mathScore)

first_stdev_start,first_stdev_end = mean - stdev, mean + stdev
second_stdev_start,second_stdev_end = mean -(2*stdev), mean +(2*stdev)
third_stdev_start,third_stdev_end = mean -(3*stdev), mean +(3*stdev)

list_of_data_within_1_std_deviation = [result for result in mathScore if result > first_stdev_start and result < first_stdev_end]
list_of_data_within_2_std_deviation = [result for result in mathScore if result > second_stdev_start and result < second_stdev_end]
list_of_data_within_3_std_deviation = [result for result in mathScore if result > third_stdev_start and result < third_stdev_end]

print('Mean of the data is {}'.format(mean))
print('Median of the data is {}'.format(median))
print('Mode of the data is {}'.format(mode))
print('Standard Deviation of the data is {}'.format(stdev))
print('{}% of data lies within 1 standard deviation'.format(len(list_of_data_within_1_std_deviation)*100.0/len(mathScore)))
print('{}% of data lies within 2 standard deviation'.format(len(list_of_data_within_2_std_deviation)*100.0/len(mathScore)))
print('{}% of data lies within 3 standard deviation'.format(len(list_of_data_within_3_std_deviation)*100.0/len(mathScore)))