import math

print("""MEDIDAS DISPONIBLES
                1. Metro
                2. Kilometro
                3. Centimetro
                4. Millas
                5. Pies
                6. Pulgadas
                """)
a=input("por favor que medida tiene:  ")

if(a=="1"):
    b=float(input("ingrese su valor que quiere convertir:  "))
    c=b/1000
    d=b*100
    e=b* 0.00062137
    f=b*3.28084
    g=b* 39.3701
    print(f"""RESPUESTAS
                    {c} kilometros
                    {d} Centimetros
                    {e} Millas
                    {f} Pies
                    {g} Pulgadas
                    """)
elif(a=="2"):
    b=float(input("ingrese su valor que quiere convertir:  "))
    c=b*1000
    d=b*100000
    e=b* 0.621371
    f=b*3280.84
    g=b* 39370.1
    print(f"""RESPUESTAS
                    {c} Metros
                    {d} Centimetros
                    {e} Millas
                    {f} Pies
                    {g} Pulgadas
                    """)
elif(a=="3"):
    b=float(input("ingrese su valor que quiere convertir:  "))
    c=b/100
    d=b/100000
    e=b/160900
    f=b/30.48
    g=b/2.54
    print(f"""RESPUESTAS
                    {c} Metros
                    {d} Kilometros
                    {e} Millas
                    {f} Pies
                    {g} Pulgadas
                    """)
elif(a=="4"):
    b=float(input("ingrese su valor que quiere convertir:  "))
    c=b*1609.34
    d=b*1.60934
    e=b*160934
    f=b*5280
    g=b*63360
    print(f"""RESPUESTAS
                    {c} Metros
                    {d} Kilometros
                    {e} Centimetros
                    {f} Pies
                    {g} Pulgadas
                    """)
elif(a=="5"):
    b=float(input("ingrese su valor que quiere convertir:  "))
    c=b* 0.3048
    d=b*0.0003048
    e=b*30.48
    f=b*0.000189394
    g=b*12
    print(f"""RESPUESTAS
                    {c} Metros
                    {d} Kilometros
                    {e} Centimetros
                    {f} Millas
                    {g} Pulgadas
                    """)
elif(a=="6"):
    b=float(input("ingrese su valor que quiere convertir:  "))
    c=b* 0.0254
    d=b*0.0000254
    e=b*2.54
    f=b*0.0000157828
    g=b*0.0833333
    print(f"""RESPUESTAS
                    {c} Metros
                    {d} Kilometros
                    {e} Centimetros
                    {f} Millas
                    {g} Pies
                    """)
else:
    print("No se tienen esas medidas")
    
    
