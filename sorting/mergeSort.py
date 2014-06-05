'''
Created on May 26, 2014

@author: karthik
'''

def mergeSort(listIn):
    
    size = len(listIn);
    
    if (size == 1):
        return listIn
    
    lhs = listIn[:size/2]
    rhs = listIn[size/2:]
    
    if (len(lhs) > 1):
        lhs = mergeSort(lhs)
    
    if (len(rhs) > 1):
        rhs = mergeSort(rhs)
        
    return merge(lhs, rhs)

def merge(lArr, rArr):
    
        