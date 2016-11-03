def BinarySearch2(A,lowRange,highRange,low,high):
    if high < low:
        return False
    mid = (low + high) // 2
    if A[mid] >= highRange:
        return BinarySearch2(A,lowRange,highRange,low,mid-1)
    elif A[mid] <= lowRange:
        return BinarySearch2(A,lowRange,highRange,mid+1,high)
    else:
        return True

A = [1,2,3,4,5,6,7,8,9,10]
lowRange =int(input("Low number"))
highRange = int(input("High Range"))
low = 0
high = len(A)-1
print(BinarySearch2(A,lowRange,highRange,low,high))

#Pseudocode
"""BINARYSEARCH(A,lowRange,highRange,low,high)
       IF high < low   #1
           RETURN FALSE   #1
       mid <- (low + high) floor_divide 2 #1
       if A[mid] >= highRange #1
           RETURN BINARYSEARCH(A,lowRange,highRange,low,mid-1) #n
       ELSE IF A[mid] <= lowrange: #1
           RETURN BINARYSEARCH(A,lowRange,highRange,mid+1,high)#n
       ELSE #1
           RETURN TRUE  #1"""

#Big O notation
#7 + 2n
#O(n)
