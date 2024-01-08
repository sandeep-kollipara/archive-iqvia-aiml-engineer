# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:10:27 2022

@author: ksandeep
"""

import os
import math


def linear_search(array, range, key):
    idx = 0
    while idx < range:
        if array[idx] == key:
            return idx
        idx+=1
    return -1


def binary_search(array, range, key):
    start = 0
    end = range # Adding +1 since floor never gives the higher end as output 
    while start != end:
        idx = math.floor((start + end)/2)
        if array[idx] < key:
            start = idx
        elif array[idx] > key:
            end = idx
        elif array[idx] == key:
            return idx
        else:
            return -1


def binary_search_recursion(array, start, end, key):
    idx = math.floor((start + end + 1)/2)
    if array[idx] < key:
        start = idx
    elif array[idx] > key:
        end = idx
    elif array[idx] == key:
        return idx
    else:
        return -1
    return binary_search_recursion(array, start, end, key)


def linearsearch(A, key):
    index = 0
    while index < len(A):
        if A[index] == key:
            return index
        index = index + 1
    return -1

def binarysearch_iterative(A, key):
    L = 0
    R = len(A) - 1
    while L <= R:
        mid = (L + R)//2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            R = mid - 1
        elif key > A[mid]:
            L = mid + 1
    return -1


def binarysearch_recursive(A, key, L, R):
    if L > R:
        return -1
    else:
        mid = (L+R)//2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binarysearch_recursive(A, key, L, mid-1)
        elif key > A[mid]:
            return binarysearch_recursive(A, key, mid+1, R)

if '__main__'.__eq__(__name__):
    
    arr = list(range(13, 35, 2))
    index_1 = linear_search(arr, 7, 23)
    print(index_1)
    index_2 = binary_search(arr, 7, 23)
    print(index_2)
    index_3 = binary_search_recursion(arr, 0, 7, 23)
    print(index_3)
    found_1 = linearsearch(arr, 23)
    print('Result: ', found_1)
    found_2 = binarysearch_iterative(arr, 23)
    print('Result: ', found_2)
    found_3 = binarysearch_recursive(arr, 23, 0 , 7)
    print('Result: ', found_3)

