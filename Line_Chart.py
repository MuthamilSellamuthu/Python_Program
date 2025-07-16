/*Write a Python program using the matplotlib library to plot a simple line chart that shows the trend of a dataset. The dataset represents the years and corresponding values for a particular metric.

You need to plot the line chart based on the following information:
The x-axis represents the years: [1989, 1991, 1996, 1998, 2000].
The y-axis represents the corresponding values: [9.8, 12, 8, 7.2, 6.9].

Chart Details:
The x-axis will show the years: [1989, 1991, 1996, 1998, 2000].
The y-axis will show the values: [9.8, 12, 8, 7.2, 6.9].
The line chart should be labeled as "Line Chart".
Set X label = 'Year' , Y label = 'Unemployment rate' and Title = 'Economy'.
*/


import matplotlib.pyplot as plt
x = [1989,1991,1996,1998,2000]
y = [9.8,12,8,7.2,6.9]
#Type your content here
plt.plot(x,y,linestyle='-',label='Line Chart')
plt.xlabel('Year')
plt.ylabel('Unemployment rate')
plt.title('Economy')
plt.show()
