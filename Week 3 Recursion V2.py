"""This function reverses the order of words in the string "This is awsome"."""
def reverse(lst,output,index):   # Reverse function takes in 3 parameters - lst, output and index.  It reverses the order of words in a sentence.
    if index >= 0: #1 # the recursive function can only be executed if the index value is greater than or equal to zero.
        output.append(lst[index] + " ") #1 # the index of the origional list is appended to the output list
        index = index - 1 #1 # value of index decreases by 1.
        reverse(lst,output,index) #n # the function is recalled
        return ''.join(map(str, output)) #1 # the reversed order of words is returned as a string.

#O(n)
string = "This is awesome"
lst = string.split() # string is converted into a list
output = [] # output list is currently empty
index = len(lst)-1 # index for last word in list is found by measuring the length of the list
print(reverse(lst,output,index)) # function is called

#Pseudocode
""" REVERSE(lst,output,index)
       IF index >=0
          append index of lst to output and add a whitespace after each element
          index <- index - 1
          REVERSE(lst,output,index)
          RETURN output as a string
       ENDIF
"""

#Big O notation
#4 + n
#O(n)

"""This algorithm determines if a number that the user enters is a prime number
or not a prime number."""

def prime(n,t):  # recursive function to determine wether a number is prime or not.
    if n < 2:   #1  # if a number is less than 2, it is not prime as 1,0 and negative numbers are not prime.
        print("Not a Prime Number")#1 
    else:#1 
        x = n % t #1 # calculates the modulus of the number the user enters with the number below.
        if t == 1: #1 # If the number less than the user enters becomes 1, the number is prime
            print ("Prime Number")#1
        elif x == 0: #1 # if the modulus is ever 0, the number is not prime as it can be divided by a number other than itsself and one.
            print ("Not a Prime Number")#1
        else: #1
            t = t - 1 #1 # The number t counts down every time the function is recalled to see if the entered number is divisible by it.
            prime(n,t) #n
        
n = int(input("Please enter a number"))
t = n - 1 # this is the number that decreases from the number the user enters and is divided by.
prime(n,t)

#Big O notation
#10 + n
#O(n)


#Pseudocode
""" PRIME(n,t)
       IF n < 2:
          print "Not a Prime Number"
       ELSE
           x <- n mod t
           IF t = 1
              print "Prime Number"
           ELIF x = 0
              print "Not a prime Number"
           ELSE
              t <- t - 1
              PRIME(n,t)"""

"""This algorithm removes all of the vowles from the words in an sentence
that the user enters and only returns the consinents."""

def noVowels(lst,newlst,lenlst): # This function removes vowels from a string the user enters.
    try: #1 # Try-except statement catches index errors.
        index = lenlst #1
        lstindex = lst[index]#1 # the index of the origional list is found, derrived from value of lenlst
        if lstindex == "A" or lstindex == "E" or lstindex == "I" or lstindex == "O" or lstindex == "U" or lstindex == "a" or lstindex == "e" or lstindex == "i" or lstindex == "o" or lstindex == "u": #1
            del lst[index] #1 # line above - if statement to see if the selected element in the list is a vowel.  If this is true, it is deleted.
            noVowels(lst,newlst,lenlst) #n
        else: #1
            newlst.append(lst[index]) #1 # if the list is not a string, consinents are appended to the newlist
            del lst[index] #1            # then deleted from the origional list.
            print(''.join(map(str, newlst))) #1 # list of consinents is printed as a string
            print() #1
        if lenlst < len(lst)+1: #1 # this code makes sure that all consinents are printed by recalling the function as long as the value of lenlst is less than the length of  origional list + 1
            noVowels(lst,newlst,lenlst) #n
        else: #1
            pass #1
    except IndexError: #1
        pass #1

string = str(input("Please enter a string")) # user enters a string
lst = list(string) # string is converted into a list
lenlst = 0 #index at start of list
newlst = [] #new empty list
noVowels(lst,newlst,lenlst) # function is called

#Pseudocode
""" NOVOWELS(lst,newlst,lenlst)
       index <- lenlst
       lstindex <- lst[index]
       IF lstindex = "A" OR lstindex = "E" OR lstindex = "I" OR lstindex = "O" OR lstindex = "U" OR lstindex = "a" OR lstindex = "e" OR lstindex = "i" OR lstindex = "o" OR lstindex = "u"
          DELETE lst[index]
          NOVOWLES(lst,newlst,int)
       ELSE
          append index of list to newlst
          DELETE lst[index]
          print newlst as a string
       IF lenlst is less than length of lst + 1
          NOVOWLES(lst,newlst,lenlst)
       ELSE
          PASS
"""
# Big O notation
# 15 + n
# O(n)
