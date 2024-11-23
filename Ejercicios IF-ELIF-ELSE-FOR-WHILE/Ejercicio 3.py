L=("a","e","i","o","u","A","E","I","O","U")
a=input("ingresar un caracter: ")
if len(a) !=1:
    print("error no mas de dos caracteres")
if(a in L):
    print("Es una vocal")
else:
    print("No es una vocal")
    
