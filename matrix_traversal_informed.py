import numpy

def matrix_sum(a):
    s=0
    for i in range(n):
        for j in range(n):
            s=s+a[i][j]

    return s


def printMat(a,x,y):
    for i in range(n):
        for j in range(n):
            if (i==x and j==y):
                print("V", end =" ")
            else:
                print(int(a[i][j]), end = " ")
        print()

def cleanRoom(a, x, y):
    if (a[x][y]==0):
        printMat(a,x,y)
        print("Deja curat")
    else:
        a[x][y]=0
        printMat(a,x,y)
        print("Murdar!...Curatare...Curat!")


def step(a,b):
    if (a>b): 
        return -1
    else: 
        return 1

from random import randint

n=int(input("Introduceti dimensiunea matricei "))

a=numpy.zeros((n, n))


for i in range(n):
    for j in range(n):
        a[i][j]=randint(0,1)



dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x=0
y=0

pasi=1
actiuni=0

print("Aspiratorul va fi plasat la " + str(x) + " si " + str(y))
printMat(a, -1, -1)

if (a[x][y]==0):
    print("Deja curat")
else:
    actiuni=actiuni+1
    a[x][y]=0
    print("Murdar!...Curatare...Curat!")
    printMat(a,x,y)

dX=0
dY=0
distanta=n*n+1

while (matrix_sum(a)!=0):
    distanta=n*n+1
    actiuni=actiuni+1
    for i in range(n):
        for j in range(n):
            if (a[i][j] == 1):
                if ( (abs(i-x)+abs(j-y)) <  distanta):
                    distanta=abs(i-x)+abs(j-y)
                    dX=i
                    dY=j


    print("-------------")
    print(str(dX) + " " + str(dY))
    print("-------------")


    for p in range(x,dX, step(x, dX)):
        pasi=pasi+1
        cleanRoom(a,p,y)
        print("----------------------------------")
    x=dX

    for p in range(y,dY, step(y, dY) ):
        cleanRoom(a,x,p)
        pasi=pasi+1
        print("----------------------------------")
    y=dY
    a[x][y]=0
    cleanRoom(a,x,y)

print("In final avem pasi:" + str(pasi) + " si actiuni: " + str(actiuni)) 
print("Eficienta algoritmului este de " + str(actiuni/pasi))