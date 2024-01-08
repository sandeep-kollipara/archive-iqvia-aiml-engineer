# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:10:27 2022

@author: ksandeep
"""

import os
import random
import math

def selection_sort(array_original): # Same as explained in course.
    try:
        array = list(array_original.copy())
    except:
        array = list(array_original)
    size_of_array = len(array)
    for main_idx in range(size_of_array):
        min_idx = main_idx
        for replacable_idx in range(main_idx+1, size_of_array):
            if array[min_idx] > array[replacable_idx]:
                min_idx = replacable_idx
                #temp = array[main_idx]
                #array[main_idx] = array[replacable_idx]
                #array[replacable_idx] = temp
        temp = array[main_idx]
        array[main_idx] = array[min_idx]
        array[min_idx] = temp
    return array


def insertion_sort(array_original):
    try:
        array_remaining = list(array_original.copy())
    except:
        array_remaining = list(array_original)
    size_of_array = len(array_remaining)
    array_insertion = []
    for i in range(size_of_array):
        array_insertion.append(array_remaining.pop(0))
        for j in range(len(array_insertion)-1, 0, -1):
            #if j == 0:
            #    break
            #else:
                if array_insertion[j-1] < array_insertion[j]:
                    break
                else:
                    temp = array_insertion[j-1]
                    array_insertion[j-1] = array_insertion[j]
                    array_insertion[j] = temp
    return array_insertion


def insertionsort(A):
    n = len(A)
    for i in range(1, n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position-1] > cvalue:
            A[position] = A[position-1]
            position-=1
        A[position] = cvalue
    #return A


def bubble_sort(array_original): # Same as explained in course
    try:
        array = list(array_original.copy())
    except:
        array = list(array_original)
    size_of_array = len(array)
    for i in range(size_of_array, 0, -1):
        for j in range(i-1):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array


def shell_sort(array_original):
    try:
        array = list(array_original.copy())
    except:
        array = list(array_original)
    size_of_array = len(array)
    gap = size_of_array // 2
    for i in range(int(math.log2(size_of_array))):
    #while gap != 0:
        for j in range(size_of_array - gap):
            if array[j] > array[j+gap]:
                temp = array[j]
                array[j] = array[j+gap]
                array[j+gap] = temp
            if j >= gap: # The following conditions are required for proper sorting.
                if array[j-gap] > array[j]:
                    temp = array[j-gap]
                    array[j-gap] = array[j]
                    array[j] = temp
        gap //= 2
    return array


def shellsort(A):
    n = len(A)
    gap = n // 2
    while gap > 0:
        i = gap
        while i < n:
            temp = A[i]
            j = i-gap
            while j >=0 and A[j] > temp:
                A[j+gap] = A[j]
                j = j-gap
            A[j+gap] = temp
            i+=1
        gap //= 2


def merge_sort(array, left, right):
    #try: # Original array needs to be modified as this is a recursive function.
    #    array = list(array_original.copy())
    #except:
    #    array = list(array_original)
    if left < right:
        mid = (left + right) // 2
        array = merge_sort(array, left, mid)
        array = merge_sort(array, mid+1, right)
        array = merge(array, left, mid, right)
    return array


def merge(array, left, mid, right):
    #try:
    #    sorted_array = list(array.copy())
    #except:
    #    sorted_array = list(array)
    #sorted_array = [0]*len(array)
    sorted_array = [0]*(right+1) # No need to copy the entire array, only the subset limits.
    i = left
    j = mid + 1
    k = left
    while i <= mid and j <= right:
        if array[i] > array[j]:
            sorted_array[k] = array[j]
            j+=1
            k+=1
        else:
            sorted_array[k] = array[i]
            i+=1
            k+=1
    while i <= mid: # Either this runs...
        sorted_array[k] = array[i]
        i+=1
        k+=1
    while j <= right: # or this runs but not both.
        sorted_array[k] = array[j]
        j+=1
        k+=1
    #for l in range(len(array)):
    for l in range(left, right+1): # No need to copy the entire array, only the subset limits.
        array[l] = sorted_array[l]
    return array


def quick_sort(array, i=0, j=2):
    pvt = i
    if j > i+1:
        i_init = i
        j_init = j
        while j > pvt and j > i:
            i+=1
            while array[i] <= array[pvt] and i < j:
                i+=1
            j-=1
            while array[j] >= array[pvt] and i <= j:
                j-=1
            if j > i:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
            #i+=1
            #j-=1
        temp = array[j]
        array[j] = array[pvt]
        array[pvt] = temp
        print(pvt, i, j)
        array = quick_sort(array, i=i_init, j=j)
        array = quick_sort(array, i=j+1, j=j_init)
    return array


def quicksort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quicksort(A, low, pi-1)
        quicksort(A, pi+1, high)


def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high
    while True:
        while i <= j and A[i] <= pivot:
            i+=1
        while i <= j and A[j] > pivot:
            j-=1
        if i <= j:
            A[i], A[j] = A[j], A[i]
        else:
            break
    A[low], A[j] = A[j], A[low]
    return j


def count_sort(array): # The input array has to have positive integers.
    size_of_array = len(array)
    max_of_array = max(array)
    count_array = [0]*(max_of_array+1)
    for idx in range(size_of_array):
        count_array[array[idx]]+=1
    sorted_array = []
    for idx in range(max_of_array+1):
        while count_array[idx] != 0: # (No, it doesn't) This increases the time complexity to O(n^2).
            count_array[idx]-=1
            sorted_array.append(idx)
    return sorted_array


def countsort(A):
    n = len(A)
    maxsize = max(A)
    carray = [0]*(maxsize+1)
    for i in range(n):
        carray[A[i]]+=1
    i = 0
    j = 0
    while i < maxsize+1:
        if carray[i] > 0:
            A[j]=i
            j+=1
            carray[i]-=1
        else:
            i+=1


def radix_sort(array):
    max_digits_in_array = int(math.log10(max(array)))+1
    buckets = [[]]*10
    for decimal in range(max_digits_in_array):
        new_array = []
        # loading...
        for element in array:
            buckets[element//10**decimal%10] = buckets[element//10**decimal%10] + [element]
        # unloading...
        for i in range(10):
            while buckets[i].__ne__([]):
                new_array.append(buckets[i].pop(0))
        array = new_array
    return new_array


def radixsort(A):
    n = len(A)
    maxelement = max(A)
    digits = len(str(maxelement))
    l = []
    bins = [l]*10
    for i in range(digits):
        for j in range(n):
            e = int((A[j] / pow(10, i)) % 10)
            if len(bins[e]) > 0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]
        k = 0
        for x in range(10):
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)
                    k+=1


if '__main__'.__eq__(__name__):
    
    list_1 = []
    random.seed(35)
    for i in range(13):
        list_1 = list_1 + [random.randint(35, 65)]
    list_2 = [random.randint(35,65) for x in range(13)]
    list_3 = [eval('random.randint(35,65)') for x in range(13)]
    list_4 = [int(35+30*random.random()) for x in range(13)]
    list_5 = [int(random.normalvariate(mu=50.5, sigma=7.5)) for x in range(13)]
    list_6 = [int(15*random.betavariate(alpha=2, beta=2))+50 for x in range(13)]
    list_7 = [int(15*random.expovariate(lambd=1.65))+35 for x in range(13)]
    list_8 = [int(15*random.gammavariate(alpha=2, beta=2))+50 for x in range(13)]
    list_9 = [int(random.gauss(mu=50.5, sigma=7.5)) for x in range(13)]
    sorted_list_1 = selection_sort(list_1)
    print(sorted_list_1)
    sorted_list_2 = insertion_sort(list_2)
    print(sorted_list_2)
    insertionsort(list_2)
    print(list_2)
    sorted_list_3 = bubble_sort(list_3)
    print(sorted_list_3)
    sorted_list_4 = shell_sort(list_4)
    print(sorted_list_4)
    shellsort(list_4)
    print(list_4)
    sorted_list_5 = merge_sort(list_5.copy(), 0 ,12)
    print(list_5)
    print(sorted_list_5)
    sorted_list_6 = quick_sort(list_6.copy(), 0, 13)
    print(list_6)
    print(sorted_list_6)
    quicksort(list_6, 0, 12)
    print(list_6)
    sorted_list_7 = count_sort(list_7)
    print(list_7)
    print(sorted_list_7)
    countsort(list_7)
    print(list_7)
    print(list_8)
    sorted_list_8 = radix_sort(list_8.copy())
    print(sorted_list_8)
    radixsort(list_8)
    print(list_8)
    print(list_9)
    sorted_list_9 = sorted(list_9, reverse=True)
    print(sorted_list_9)
    list_9.sort(reverse=True)
    print(list_9)


