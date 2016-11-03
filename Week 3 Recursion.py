def reverse(string):   #1
    if string == "":   #1
        return string  #1
    else:#1
        return reverse(string[1:]) + string[0] #n

#O(n)
string = "This is awsome"
print(reverse(string))

#Pseudocode
""" REVERSE(string)
       IF string = ""
          RETURN string
       ELSE
          RETURN reverse(string[all except first element]) + string[0]
"""


def prime(n,t):  
    if n < 2:   #1
        print("Not a Prime Number")#1
    else:#1
        x = n % t #1
        if t == 1: #1
            print ("Prime Number")#1
        elif x == 0: #1
            print ("Not a Prime Number")#1
        else: #1
            t = t - 1 #1
            prime(n,t) #n
        
n = int(input("Please enter a number"))
t = n - 1
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

def noVowels(lst,newlst,lenlst):
    try:
        index = lenlst
        lstindex = lst[index]
        if lstindex == "A" or lstindex == "E" or lstindex == "I" or lstindex == "O" or lstindex == "U" or lstindex == "a" or lstindex == "e" or lstindex == "i" or lstindex == "o" or lstindex == "u":
            del lst[index]
            noVowels(lst,newlst,lenlst)
        else:
            newlst.append(lst[index])
            del lst[index]
            print(''.join(map(str, newlst)))
            print()
        if lenlst < len(lst)+1:
            noVowels(lst,newlst,lenlst)
        else:
            pass
    except IndexError:
        pass

string = str(input("Please enter a string"))
lst = list(string)
lenlst = 0
newlst = []
noVowels(lst,newlst,lenlst)

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

