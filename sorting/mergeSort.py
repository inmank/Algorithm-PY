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
    outArr = []
    leftIndex = 0
    rightIndex = 0
    
    for k in range(len(lArr) + len(rArr)):
        if (leftIndex >= len(lArr)):
            outArr.append(rArr[rightIndex])
            rightIndex = rightIndex + 1
        elif (rightIndex >= len(rArr)):
            outArr.append(lArr[leftIndex])
            leftIndex = leftIndex + 1
        else:
            if (lArr[leftIndex] < rArr[rightIndex]):
                outArr.append(lArr[leftIndex])
                leftIndex = leftIndex + 1
            elif (rArr[rightIndex] < lArr[leftIndex]):
                outArr.append(rArr[rightIndex])
                rightIndex = rightIndex + 1
    
    return outArr     
input = [3,4,8,9,2,5,7,6]
print mergeSort(input)         
        