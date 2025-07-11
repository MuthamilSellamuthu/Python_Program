/*Write a Python program to create a Pandas DataFrame from the given dictionary and display the data in a tabular format.

Input Format:
There is no user input required for this task. The dictionary provided in the problem statement should be used to create the DataFrame.

Output Format:
The program should display the Pandas DataFrame in a tabular format.
*/

import pandas as pd
data={
      'Name':['Alice','Bob','Charlie','David'],
      'Age':[24,27,22,32],
       'City':['New York','Los Angeles','Chicago','Miami']
}
ds=pd.DataFrame(data)
print(ds)
  
