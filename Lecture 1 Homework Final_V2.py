# Random Shuffling
import random            #Imports the random module                           
from math import factorial #Imports the factorial function from the math mosule
def randomSort():

    inputt = [5,3,8,6,1,9,2,7] #1 # origional list of numbers to be sorted
    output = []                #1 # output list is currently an empty list
    inlength = len(inputt)     #1 # length of origional list is measured
    outlength = len(output)    #1 # length of output list is measured
    while outlength < inlength:                  #nx1 #loop continues while the length of the output list is shorter then the input list
        rand = random.randint(0, len(inputt))   #n # random number is generated between 0 and length of origional list
        if rand == len(inputt):      #n # if the random number is equal to the length of the origional list,
            rand = rand - 1         #n    the random number decreases by one to prevent an index error.  if this condition is not met, random number stays the same.
        else:                    #n
            rand = rand         #n
        tmp = inputt[rand]       #n  #the random number is then used to select a element from the list that corresponds to the index value of the origional list
        if tmp not in output:    #n     # this if statement makes sure that the same element in the origional list is not appended more than once to the output list
            output.append(tmp)   #n     # output randomly selected element is appended to the output list.
            outlength = len(output)     #n #this increases the value of the length of the output list to prevent an infinate loop when all elements have been randomly sorted.
        else:       #n
            pass    #n
    print(output)    #1 #Output list is then printed with the randomly sorted elements
randomSort()

#Total = 12n + 5
# BigO = O(n) = fair


""" a.  This algorithm has a defined input that is a list of numbers that have
     been hardcoded into the algoritm.  The defined output is a veriable called
     'output', which prints out the number of trailing zeros of the factorial.
 b.  I can gurantee that the algorithm terminates because the while loop has a conditional that
     eventually becomes false meaning that there are no infinate loops.
 c.  it is specified in a clear and concise manner because the variables have
     appripriate names.
 d.  This algorithm always produces the correct result because I have tested
     this algorithm multiple times and have checked the output against the input
     to make sure that the output length is the same as the input length, that the
     numbers in the output are not repeated and are in a different order each
     time the algorithm is run and that numbers have not been missed out in the
     output."""

# Number of trailing zeros in a factorial
print()
number = int(input("Please enter an interger")) #1  # user enters a number
fact = factorial(number)           #1       # factorial of number is generated using factorial function
element = [int(a) for a in str(fact)]#n  # the factorial result is converted from an interger into a list using a for loop
zero = []  #1   # this will be the list of trailing zeros, currently empty
for i in range(len(element)): #n  # this for loop will append the zeros to the trailing zero list
    a = len(element)-1     #n  # the last indicie of the list is found and assigned to variable a
    if element[a] == 0:    #n  # the element that variable a corresponds to is 0, it is appended to the list.
        zero.append(element[a])  #n
        del element[a]  #n # this element is then deleted, so the next element can be appended to the output list if it is zero.
    else:      #n
        pass   #n
print("There are", len(zero), "Trailing zeros in this factorial.")#1  # the length of the zero is then printed. 

#Total = 8n + 4
# Big O = O(n) = fair



""" a.  This algorithm does have defined inputs as it asks the user to enter an
     interger which is then assigned to a variable called 'number'.  The defined
     output is the 'len(zero)' in the print statement.
 b.  I can gurantee that it terminates because this algorithm uses iteration
     as a for loop which takes a trailing zero from the end of the element list
     which contains the factorial and appends it to the zero list.  The algorithm
     uses an if statement to delete one trailing zero from the element list per
     iteration, when there are no more trailing zeros left in the element list,
     the algorithm terminates.  The number of trailing zeros is then counted
     by determining the length of the zero list.
 c.  Most of the code is in a cleae and concise manner as most variables have
     suitable names.
 d.  This algorithm produces the correct results for all instances because I
     have entered different numbers when running the code and got Python to
     print out the factorial and manually count the trailing zeros to check
     that the number of zeros is what the algorithm says it is."""
