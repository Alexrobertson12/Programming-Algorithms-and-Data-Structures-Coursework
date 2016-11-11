def biggestSequence(array):
    counter = 1
    outlist = []
    for i in range(0,len(array)-1):
        if array[i] < array[i+1]:
            counter = counter + 1
        if array[i] >= array[i+1]:
            outlist.append(counter)
            counter = 1
    outlist.append(counter)
    m = max(outlist)
    p = outlist.index(m)
    sumL = 0
    for i in range(p):
       sumL = sumL + outlist[i]
    output = array[sumL:sumL+m]
    return output


array = [1,2,3,4,2,6,1,8,9,10,11,12,13,2,3,5]
print("The biggest subsequence in the array is ", biggestSequence(array))
