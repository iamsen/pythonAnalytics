__author__ = 'sen.li'

import pandas


housing_2013 = pandas.read_csv("thads2013n.txt")


# How many columns of the matrix?
num_columns = len(housing_2013.columns)
# print("Number of columns:  " + str(num_columns))


# How to filter the columns
filtered_housing_2013 = housing_2013[['AGE1', 'FMR', 'TOTSAL']]
filtered_housing_2013.hist(column='FMR', bins=20)


# How to clean the data by removing non-existing rows
evaluated_row_numbers = []
evaluated_row_numbers = filtered_housing_2013['AGE1'] > 0
# print(evaluated_row_numbers)
cleaned_housing_2013 = filtered_housing_2013[evaluated_row_numbers]
print cleaned_housing_2013.head(10)

# Calculating the Difference in DataFrames
filtered_count = len(filtered_housing_2013)
cleaned_count = len(cleaned_housing_2013)
print(filtered_count - cleaned_count)

# Verify the cleanup
negative_row_numbers = cleaned_housing_2013['AGE1'] < 0
negative_housing_2013 = cleaned_housing_2013[negative_row_numbers]
print(len(negative_housing_2013))