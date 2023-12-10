# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:06:04 2023

@author: ASUS
"""

def quick_sort(arr,level=0):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    sorted_arr = quick_sort(left, level + 1) + middle + quick_sort(right, level + 1)
    
    print("第{}次遍歷後排序結果{}".format(level, sorted_arr))
    
    return sorted_arr

def merge_sort(arr, level=0):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left, level+1)
    right = merge_sort(right, level+1)
    
    sorted_arr = merge(left, right)
    
    print("第{}次遍歷後排序結果{}".format(level, sorted_arr))
    
    return sorted_arr

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
    
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
        print("第{}次遍歷後排序結果{}".format(i,arr))
        
    print("Bubble sort後的數列: ")
    print(arr)
    
    
def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1,n):
        key = arr[i]
        j=i-1
        
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = key
        print("第{}次遍歷後排序結果{}".format(i,arr))
        
    print(" insertion_sort後的數列: ")
    print(arr)
    
def main():
    arr = [100,64,34,25,12,11,90]
    quick_sorted = quick_sort(arr)
    print("Quick sort:", quick_sorted)
    print()
    arr = [100,64,34,25,12,11,90]
    merge_sorted = merge_sort(arr)
    print("Merge sort", merge_sorted)
    print()
    arr = [100,64,34,25,12,11,90]
    insertion_sort(arr)
    print()
    arr = [100,64,34,25,12,11,90]
    bubble_sort(arr)

if __name__ == "__main__":
    main()