/*You are given a dataset containing measurements of iris flowers. The dataset includes various attributes related to the flowers' sepals and petals, such as their length and width, along with the species 
of the flowers. Your task is to load, analyze, and visualize the data using Python libraries such as pandas for data manipulation and matplotlib for visualization.

The dataset is provided in CSV format, and you are required to perform the tasks related to data inspection, analysis, and plotting.

Dataset Structure:
The dataset consists of the following columns:
Id: An identifier for the iris flower (integer).
SepalLengthCm: The length of the sepal (float).
SepalWidthCm: The width of the sepal (float).
PetalLengthCm: The length of the petal (float).
PetalWidthCm: The width of the petal (float).
Species: The species of the iris flower (categorical values: Iris-setosa, Iris-versicolor, Iris-virginica).
                                                                                                           
Task 1:
Write a Python program that:
Loads the dataset from the file iris_csv.csv into a pandas DataFrame.
Displays the first five rows of the dataset using the appropriate pandas function.
*/
                                                                                                           

import pandas as pd
ds=pd.read_csv('iris_csv.csv')
print(ds.head())
