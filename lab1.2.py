import sys
import math

# Módulo para verificar si un número es primo
def detecta_primo(num):
    if num <= 1:
        return False  # no es primo
    for i in range(2, num):
        if num % i == 0:
            return False  # no es primo
    return True  # es primo

# Módulo para contar las potencias de cualquier base
def contar_potencias(num, base):
    cuentap = 0
    potencia = 1
    while potencia <= num:
        potencia *= base  # se itera hasta encontrar todas las potencias
        cuentap = cuentap + 1
    return cuentap - 1  # la cuenta estaba aumentada en 1 al final de la iteración

# Módulo principal

if __name__ == "__main__":

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])

    cuenta = 0

    if c == 1:
        for num in range(a, b + 1):
            if detecta_primo(num):
                cuenta += 1
        print("Hay", cuenta, "números primos en este rango")
    else:
        k = c
        cuenta = contar_potencias(b, k) - contar_potencias(a - 1, k)  # restamos la cantidad de potencias en los extremos para calcular el total en el intervalo
        print("Hay", cuenta, "potencias de", k, "en este rango")
