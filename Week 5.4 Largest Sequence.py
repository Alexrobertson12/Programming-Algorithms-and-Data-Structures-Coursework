"""This algorithm finds the longest increasing subequence in a list of subsequences"""
def biggestSequence(array):
    counter = 1 # counter counts length of each subsequence.
    outlist = []
    for i in range(0,len(array)-1): # For loop allows eaach subsequence length to be counted within the range of linngth of the list
        if array[i] < array[i+1]: # Fhecks that the element in the list is less than the nest element
            counter = counter + 1 # if true, the counter increases by 1.
        if array[i] >= array[i+1]: # If the previous element is greater than or equal the next element
            outlist.append(counter) # the value of the counter is appended to the outlist list
            counter = 1             # and the counter is reset to 1.
    outlist.append(counter)
    m = max(outlist) # maximum value in outlist list is found
    p = outlist.index(m) # index position of maximum value in outlist is then found
    sumL = 0
    for i in range(p): # builds up largest sequence in origioal list
       sumL = sumL + outlist[i] # finds beginning of largest sequence
    output = array[sumL:sumL+m] # finds largest subsequence
    return output # returns largest sequence


array = [1,2,3,4,2,6,1,8,9,10,11,12,13,2,3,5]
print("The biggest subsequence in the array is ", biggestSequence(array))
