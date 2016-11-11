def binarySearch(A,low,high,Status):
    for i in range(len(A)):
        if A[i] > low and A[i] < high:
            Status = True
            return Status
            break
        elif high < A[0] or low > A[len(A)-1]:
            Status = False
            return Status
        else:
            Status = False


A = [1,2,3,4,5,6,7,8,9,10]
low = int(input("Please enter first number"))
high = int(input("Please entrt second number"))
Status = False
print(binarySearch(A,low,high,Status))
