#!/bin/bash
# a)

cod_pucp=$1
nombre="Nilo Rikel Cori Ramos"
echo "$nombre  $cod_pucp"

# b)
mkdir Pregunta1 
mkdir Pregunta2
chmod 777 Pregunta1
chmod 777 Pregunta2

# c)
cp pregunta1.c pregunta1 Pregunta1/

# d)
cp pregunta2.py Pregunta2/
chmod 111 Pregunta2/pregunta2.py

# e)
gcc pregunta1.c -o pregunta1
time ./pregunta1 1 100 4

# f)
time python3 pregunta2.py 1 100 4

# g)
if [ $# -lt 3 ]; then
    echo "Debe ingresar 3 argumentos de entrada"
fi
