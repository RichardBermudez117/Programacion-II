d="si"
f=d.lower()
while f=="si" :
    c=0
    a=input("ingresa una frase: ")
    for b in a:
        if b.isupper():
            c += 1
    print(f"La cantidad de letras mayúsculas en la cadena es: {c}")
    d=input("desea escribir otra frase?: ")
