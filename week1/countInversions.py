'''
Created on May 18, 2014

@author: karthik
'''
inFileName = "e:/IntegerArray.txt"

inArr = []
#inArr = [1, 3, 5 ,2, 4, 6]
#inArr = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]

global count
global fo
count = 0

def countInvUsingMergeSort(arrIn):
    size = len(arrIn)
    
    if size == 1:
        return arrIn
    
    lArr = arrIn[:size/2]
    rArr = arrIn[size/2:]
    
    if (len(lArr) > 1):
        lArr = countInvUsingMergeSort(lArr)
    
    if (len(rArr) > 1):
        rArr = countInvUsingMergeSort(rArr)

    oArr = merge(lArr, rArr) 
    return oArr

def merge(leftArr, rightArr):
    outArr = []
    i = 0
    j = 0
    global count
    global fo
    
    length = (len(leftArr)+len(rightArr))    
    for k in range(length):
        if (i >= len(leftArr)):
            outArr.append(rightArr[j])
            j+=1
        elif (j >= len(rightArr)):
            outArr.append(leftArr[i])
            i+=1
        else:
            if (leftArr[i] < rightArr[j]):
                outArr.append(leftArr[i])
                i+=1
            elif (rightArr[j] < leftArr[i]):
                outArr.append(rightArr[j])
                j+=1
                count = count+(len(leftArr) - i)
    
    return (outArr)

    
with open(inFileName) as inFile:
    for line in inFile:
        inArr.append(int(line))
    
countInvUsingMergeSort(inArr)
print count
fo.close()



    
    
    
    