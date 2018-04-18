#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv

c=[]

def load():
    global c
    with open("preguntas.csv","r") as a:
        for x in a:
            c.append(x.split(":"))	#genera una tupla de elementos, con subtuplas de elementos
    

def pregunta(nm):
    global c
    a = c[nm-1]
    if (c[nm-1]):
        print("Pregunta {0}: '{1}'".format(a[0],a[1]))
        c[nm-1] = ""
    else:
        print("Pregunta ya evaluada y quitada del listado")
    
def main():
    condicion = True
    load()
    print("Para la actividad de pregúntas por tómbola hay {} preguntas disponibles".format(len(c)))
    while (condicion):
        numero = int(input("Ingrese el numero de la pregunta: "))
        while (numero<0 or numero>(len(c))):
            print("Ingreso incorrecto, favor intentar dentro de las preguntas disponibles")
            numero = int(input("Ingrese el numero de la pregunta: "))
            
        pregunta(numero)
        condicion = input("Desea preguntar otravez?: ")
        
main()
    