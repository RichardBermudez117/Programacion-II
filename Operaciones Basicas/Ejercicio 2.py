# Función principal del programa
import math
a=int(input('ingresar dato numerico\n'))
b=int(input('ingresar dato numerico\n'))
print('datos de las diferentes operaciones')

print('operacion suma')
suma=int(a+b)
print('la suma da: ' ,suma)

print('operacion resta')
a=int(input('ingresar dato numerico\n'))
b=int(input('ingresar dato numerico\n'))
resta=int(a-b)
print('la resta da: ' ,resta)

print('operacion multiplicacion')
a=int(input('ingresar dato numerico\n'))
b=int(input('ingresar dato numerico\n'))
multiplicacion=int(a*b)
print('la multiplicacion da: ' ,multiplicacion)

print('operacion division')
a=int(input('ingresar dato numerico\n'))
b=int(input('ingresar dato numerico\n'))
division=float(a/b)
print('la division da: ' ,division)

print('operacion raiz')
a=float(input('ingresar dato numerico\n'))
b=float(input('ingresar dato numerico\n'))
raiz1=float(round(math.sqrt(a)))
raiz2=float(round(math.sqrt(b)))
print('la raiz cuadrada es: ' ,raiz1)
print('la raiz cuadrada es: ' ,raiz2)

print('operacion potencia')
a=float(input('ingresar dato numerico\n'))
b=float(input('ingresar dato exponente\n'))
potencia1=int(a**b)
print('la potencia da: ' ,potencia1)

print('operacion porcentaje')
a=float(input('ingresar dato numerico\n'))
b=float(input('ingresar dato numerico\n'))
porcentaje1=float((a/suma)*100)
print('el porcentaje da: ' ,porcentaje1,'%')
porcentaje2=float((b/suma)*100)
print('el porcentaje da: ' ,porcentaje2,'%')
