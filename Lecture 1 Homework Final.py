# Random Shuffling
import random                                        
from math import factorial
def randomSort():
    inputt = [5,3,8,6,1,9,2,7] #1
    output = []                #1
    inlength = len(inputt)     #1
    outlength = len(output)    #1
    while outlength < inlength:                  #nx1
        rand = random.randint(0, len(inputt))   #n
        if rand == len(inputt):      #n
            rand = rand - 1         #n
        else:                    #n
            rand = rand         #n
        tmp = inputt[rand]       #n
        if tmp not in output:    #n
            output.append(tmp)   #n
            outlength = len(output)     #n
        else:       #n
            pass    #n
    print(output)    #1
randomSort()

#Total = 12n + 5
# BigO = O(n) = fair


# a.  This algorithm has a defined input that is a list of numbers that have
#     been hardcoded into the algoritm.  The defined output is a veriable called
#     'output', which prints out the number of trailing zeros of the factorial.
# b.  I can gurantee that the algorithm terminates because the while loop has a conditional that
#     eventually becomes false meaning that there are no infinate loops.
# c.  it is specified in a clear and concise manner because the variables have
#     appripriate names.
# d.  This algorithm always produces the correct result because I have tested
#     this algorithm multiple times and have checked the output against the input
#     to make sure that the output length is the same as the input length, that the
#     numbers in the output are not repeated and are in a different order each
#     time the algorithm is run and that numbers have not been missed out in the
#     output.

# Number of trailing zeros in a factorial
print()
number = int(input("Please enter an interger")) #1
fact = factorial(number)           #1
element = [int(a) for a in str(fact)]#n
zero = []  #1
for i in range(len(element)): #n
    a = len(element)-1     #n
    if element[a] == 0:    #n
        zero.append(element[a])  #n
        del element[a]  #n
    else:      #n
        pass   #n
print("There are ", len(zero), "Trailing zeros in this factorial.")#1

#Total = 8n + 4
# Big O = O(n) = fair



# a.  This algorithm does have defined inputs as it asks the user to enter an
#     interger which is then assigned to a variable called 'number'.  The defined
#     output is the 'len(zero)' in the print statement.
# b.  I can gurantee that it terminates because this algorithm uses iteration
#     as a for loop which takes a trailing zero from the end of the element list
#     which contains the factorial and appends it to the zero list.  The algorithm
#     uses an if statement to delete one trailing zero from the element list per
#     iteration, when there are no more trailing zeros left in the element list,
#     the algorithm terminates.  The number of trailing zeros is then counted
#     by determining the length of the zero list.
# c.  Most of the code is in a cleae and concise manner as most variables have
#     suitable names.
# d.  This algorithm produces the correct results for all instances because I
#     have entered different numbers when running the code and got Python to
#     print out the factorial and manually count the trailing zeros to check
#     that the number of zeros is what the algorithm says it is.
