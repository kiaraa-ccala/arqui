import sys 
import math 

pi=math.pi 


def aproximacion_sumatoria(referencia,precision):
    
    suma = 0
    i = 0
    
    while(abs(referencia - suma) > precision):
        
        suma = suma + (pow(-1,i)/(2*i + 1))
        i = i + 1
    return suma 


if __name__== "__main__":
    referencia = pi/4
    precision = pow(10,-4)
    sumatoria = aproximacion_sumatoria(referencia, precision)
    precision_obtenida = referencia - sumatoria
    
    print("la aproximacion para pi/4 es: ", sumatoria)
    print("valor real de pi/4 : ", pi/4)
    print("la precision obtenida es: ", precision_obtenida)

