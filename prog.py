# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 00:15:19 2023

@author: Administrator
"""

import pandas as pd
print("Hello, World!")

# Python program to find factors of a number

# take inputs
num = int(input('Enter number: '))

# find factor of number
if num > 1 and num < 10:
    print('correct number entered is between 1 and 10 \n', num)
    print('The factors of', num, 'are:')
    for z in range(2, num+1):
        if(num % z) == 0:
            print(z,'is factor of ', num, '\n')
elif  num < 1 :
    print('Number less than 1 \n', num, 'Please enter the between 1 and 10 ')
else:
    print('number is greater than 10')
  ##  print('number is between 1 and 10 \n', num)
    
##print('The factors of', num, 'are:')
##for z in range(2, 10):
 ##   if(num % z) == 0:
   ##     print(z,'is factor of ', num, '\n')