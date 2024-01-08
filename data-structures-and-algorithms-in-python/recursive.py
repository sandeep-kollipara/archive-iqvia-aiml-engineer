# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:10:27 2022

@author: ksandeep
"""

import os

def recursion_sum_of_n_natural_numbers(n):
    if n > 0:
        return recursion_sum_of_n_natural_numbers(n-1) + n
    else:
        return 0 

def recursion_factorial(n):
    if n > 0:
        return recursion_factorial(n-1)*n
    else:
        return 1 

if '__main__'.__eq__(__name__):
    
    sum_of_10_natural_numbers = recursion_sum_of_n_natural_numbers(10)
    print(sum_of_10_natural_numbers)
    factorial_of_10 = recursion_factorial(10)
    print(factorial_of_10)