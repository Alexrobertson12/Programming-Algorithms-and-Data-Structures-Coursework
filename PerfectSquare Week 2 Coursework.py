def highestPerfectSquare(A):
    Squares = []
    b = 1
    for i in range(A):
        c = b**2
        b = b + 1
        if c <= A:
            Squares.append(c)
            perfectSquare = Squares[len(Squares)-1]
        else:
            pass
    return perfectSquare

A = int(input("Please Enter a Number"))
print(highestPerfectSquare(A))

#Pseudo Code            
"""HIGHEST-PERFECT-SQUARE(A)
       Squares <- []
       b <- 1
       FOR i <- 1 to A
            c <- b**2
            b <- b + 1
            IF c < A
            	   append c to Squares
                   perfectSquare <- Squares[Length[Squares] – 1]
            ENDIF
        return perfectSquare   """


# Matrices
""" x <-INPUT matrix #1
    y <-INPUT matrix #1
    ADD_MATRICES(x,y) 
       FOR i <- 1 to n #N
          FOR j <- 1 to n #N*N
             r[i][j] <- x[i][j] + y[i][j] #N*N
       RETURN r #1
    SUBTRACT_MATRICES(x,y)
       FOR i <- 1 to n #N*N
          FOR j <- 1 to n #N*N
             r[i][j] <- x[i][j] - y[i][j] #N*N
        RETURN r #1
    MULTIPLY_MATRICES(x,y)
       FOR i <- 1 to n #N
          FOR j <- 1 to n #N*N
             r1 <- x[i][j] * y[i][j] #N*N
             r2 <- x[i+1][j] * y[i][j+1] #N*N
             r3 <- x[i+2][j] * y[i][j+2] #N*N
             r = r1 + r2 + r3 #N*N
             r[i][j] <- r #N*N
        RETURN r #1
"""


# Runtime
#ADD 2N**2+N+1  O(N^2)
#SUBTRACT 2N**2+N+1  O(N^2)
#MULTIPLY 2N**2+N+1  O(N^2)
