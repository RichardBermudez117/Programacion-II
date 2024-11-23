#Un contador binario es un dispositivo que cuenta en binario, incrementando su valor en una unidad cada vez que recibe una señal de reloj.
#Vamos a simular un contador binario de 4 bits utilizando POO en Python.#

class Contador:
    def __init__(self, bits):
        self.bits = bits
        self.valor = 0

    def incrementar(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la clase derivada")

    def mostrar(self):
        return bin(self.valor)[2:].zfill(self.bits)

class ContadorBinario(Contador):
    def __init__(self, bits):
        super().__init__(bits)

    def incrementar(self):
        self.valor = (self.valor + 1) % (2 ** self.bits)

# Ejemplo de uso
contador = ContadorBinario(4)
for _ in range(20):
    print(contador.mostrar())
    contador.incrementar()
