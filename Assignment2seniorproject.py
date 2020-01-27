# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:30:56 2019

@author: Steven Solis
"""

import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error 
from sklearn.linear_model import LinearRegression
import math




'''
with open ('students.csv', 'w') as csvfile:
    csv_write = csv.writer(csvfile)
    csv_write.writerow(['Name', 'Age', 'Major', 'GPA'])
    for i in range(1, 11):
        name = input('Enter name: ')
        age = input('Enter age: ')
        major = input('Enter major: ')
        gpa = float(input('Enter GPA: '))
        csv_write.writerow([name, age, major, gpa])
        print ('My name starts with the letter', name, 'and I am', age, 'years old. I study', major, 'and my GPA is:', gpa, '.')
'''        
  
      
dset = pd.read_csv('students.csv')

sns.countplot(dset['Name'])
plt.figure()

sns.countplot(dset['Age'])
plt.figure()

sns.countplot(dset['Major'])
plt.figure()

sns.countplot(dset['GPA'])
plt.figure()
     
Name = dset['Name'].values
Age = dset['Age'].values
Major = dset['Major'].values
GPA = dset['GPA'].values

print('The average age is:', np.mean(Age))
print('The average GPA is:', np.mean(GPA))


'''
y = (GPA)
reg1 = LinearRegression()
reg1.fit(GPA.reshape(1, -1), y)
y_pred1 = reg1.predict(GPA.reshape(1, -1))

#mse = math.sqrt(mean_squared_error(GPA, y_pred1))  
#print('Root mean square error ' , mse)

mse = math.sqrt(mean_squared_error(GPA, y_pred1))
'''

def rmse(observed, predicted):
    summation = 0
    n=len(observed)
    for i in range (n):
        summation+=pow(observed[i]-predicted[i],2)
    rmse=math.sqrt(summation/10)
    print("Root mean square error is ", rmse)




        
        
        
    
    




 
