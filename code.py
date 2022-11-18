import statistics
import pandas as pd
import csv

df = pd.read_csv("StudentsPerformance.csv")
math_score_list = df["math score"].to_list()
math_score_mean = statistics.mean(math_score_list)
math_score_median = statistics.median(math_score_list)
math_score_mode = statistics.mode(math_score_list)

print("Mean, Median and Mode of math score is {}, {} and {} respectively".format(math_score_mean,math_score_median,math_score_mode))
print("``")

math_score_standard_deviation = statistics.stdev(math_score_list)
math_score_first_standard_deviation_start, math_score_first_standard_deviation_end = math_score_mean-math_score_standard_deviation, math_score_mean+math_score_standard_deviation
math_score_second_standard_deviation_start, math_score_second_standard_deviation_end = math_score_mean-math_score_standard_deviation*2, math_score_mean+math_score_standard_deviation*2
math_score_third_standard_deviation_start, math_score_third_standard_deviation_end = math_score_mean-math_score_standard_deviation*3, math_score_mean+math_score_standard_deviation*3

math_score_data_within_first_standard_deviation = [result for result in math_score_list if result> math_score_first_standard_deviation_start and result< math_score_first_standard_deviation_end]
math_score_data_within_second_standard_deviation = [result for result in math_score_list if result> math_score_second_standard_deviation_start and result< math_score_second_standard_deviation_end]
math_score_data_within_third_standard_deviation = [result for result in math_score_list if result> math_score_third_standard_deviation_start and result< math_score_third_standard_deviation_end]

print("{}% of data for math score lies between first standered deviation".format(len(math_score_data_within_first_standard_deviation)*100/len(math_score_list)))
print("{}% of data for math score lies between second standered deviation".format(len(math_score_data_within_second_standard_deviation)*100/len(math_score_list)))
print("{}% of data for math score lies between third standered deviation".format(len(math_score_data_within_third_standard_deviation)*100/len(math_score_list)))
print("``")

reading_score_list = df["reading score"].to_list()
reading_score_mean = statistics.mean(reading_score_list)
reading_score_median = statistics.median(reading_score_list)
reading_score_mode = statistics.mode(reading_score_list)

print("Mean, Median and Mode of reading score is {}, {} and {} respectively".format(reading_score_mean,reading_score_median,reading_score_mode))
print("``")

reading_score_standard_deviation = statistics.stdev(reading_score_list)
reading_score_first_standard_deviation_start, reading_score_first_standard_deviation_end = reading_score_mean-reading_score_standard_deviation, reading_score_mean+reading_score_standard_deviation
reading_score_second_standard_deviation_start, reading_score_second_standard_deviation_end = reading_score_mean-reading_score_standard_deviation*2, reading_score_mean+reading_score_standard_deviation*2
reading_score_third_standard_deviation_start, reading_score_third_standard_deviation_end = reading_score_mean-reading_score_standard_deviation*3, reading_score_mean+reading_score_standard_deviation*3

reading_score_data_within_first_standard_deviation = [result for result in reading_score_list if result> reading_score_first_standard_deviation_start and result< reading_score_first_standard_deviation_end]
reading_score_data_within_second_standard_deviation = [result for result in reading_score_list if result> reading_score_second_standard_deviation_start and result< reading_score_second_standard_deviation_end]
reading_score_data_within_third_standard_deviation = [result for result in reading_score_list if result> reading_score_third_standard_deviation_start and result< reading_score_third_standard_deviation_end]

print("{}% of data for reading score lies between first standered deviation".format(len(reading_score_data_within_first_standard_deviation)*100/len(reading_score_list)))
print("{}% of data for reading score lies between second standered deviation".format(len(reading_score_data_within_second_standard_deviation)*100/len(reading_score_list)))
print("{}% of data for reading score lies between third standered deviation".format(len(reading_score_data_within_third_standard_deviation)*100/len(reading_score_list)))
print("``")

written_score_list = df["writing score"].to_list()
written_score_mean = statistics.mean(written_score_list)
written_score_median = statistics.median(written_score_list)
written_score_mode = statistics.mode(written_score_list)

print("Mean, Median and Mode of writing score is {}, {} and {} respectively".format(written_score_mean,written_score_median,written_score_mode))
print("``")

written_score_standard_deviation = statistics.stdev(written_score_list)
written_score_first_standard_deviation_start, written_score_first_standard_deviation_end = written_score_mean-written_score_standard_deviation, written_score_mean+written_score_standard_deviation
written_score_second_standard_deviation_start, written_score_second_standard_deviation_end = written_score_mean-written_score_standard_deviation*2, written_score_mean+written_score_standard_deviation*2
written_score_third_standard_deviation_start, written_score_third_standard_deviation_end = written_score_mean-written_score_standard_deviation*3, written_score_mean+written_score_standard_deviation*3

written_score_data_within_first_standard_deviation = [result for result in written_score_list if result> written_score_first_standard_deviation_start and result< written_score_first_standard_deviation_end]
written_score_data_within_second_standard_deviation = [result for result in written_score_list if result> written_score_second_standard_deviation_start and result< written_score_second_standard_deviation_end]
written_score_data_within_third_standard_deviation = [result for result in written_score_list if result> written_score_third_standard_deviation_start and result< written_score_third_standard_deviation_end]

print("{}% of data for writing score lies between first standered deviation".format(len(written_score_data_within_first_standard_deviation)*100/len(written_score_list)))
print("{}% of data for writing score lies between second standered deviation".format(len(written_score_data_within_second_standard_deviation)*100/len(written_score_list)))
print("{}% of data for writing score lies between third standered deviation".format(len(written_score_data_within_third_standard_deviation)*100/len(written_score_list)))
print("``")
