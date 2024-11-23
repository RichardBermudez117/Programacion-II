import math
def Separar(L):
    imp=[ ]
    par=[ ]
    for i in L:
        if  i % 2 == 0:
            par.append(i)
        else:
            imp.append(i)
    imp.sort()
    par.sort()
    return(imp,par)
L=[7, 2, 9, 4, 1, 8, 6, 3]
par,imp=Separar(L)
print("los pares son: ",par," y los impares son: ",imp)


