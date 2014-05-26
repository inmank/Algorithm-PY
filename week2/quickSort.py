'''
Created on May 19, 2014

@author: karthik
'''

def quickSort(inList, start, end):
    
    if len(inList) == 1:
        return inList
    
    pivotIndex = start
    pivotElem = inList[pivotIndex]

    for k in range(start+1, end):
        if inList[k] < pivotElem:
            temp = inList[pivotIndex+1]
            inList[pivotIndex+1] = inList[k]
            inList[k] = temp
            pivotIndex+=1
    
    inList[start] = inList[pivotIndex]
    inList[pivotIndex] = pivotElem

    if (len(inList[start:pivotIndex]) > 1):
        quickSort(inList, start, pivotIndex)
    
    if (len(inList[pivotIndex+1:end]) > 1):
        quickSort(inList, pivotIndex+1, len(inList))
           
    return inList
   
#valuesIn = [11, 3, 2, 16, 6, 9, 13, 5, 1, 12, 4, 15, 7, 14, 8, 10]
valuesIn = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
inFileName = "e:/IntegerArray.txt"
'''
with open(inFileName) as inFile:
    for line in inFile:
        valuesIn.append(int(line))
'''
print quickSort(valuesIn, 0, len(valuesIn))
    