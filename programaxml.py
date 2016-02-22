#!/usr/bin/python
# -*- coding: utf-8 -*-

#"Pre-Enunciado"

"""1.Lista el número de partidos que aparecen en el escrutinio.

2.Muestra el nombre da cada partido y el número de electos de cada uno.

3.Pide el nombre de un partido y muestra sus datos:nombre, número de electos, porcentaje de votos.

4.Pide el número de electos y te muestra si hay, los partidos que tienen ese número.

5.Muestra la información de forma gráfica ,además de mostrar datos generales sobre las elecciones, votos totales, votos en blanco , etc.."""

#importación de librerías
#import xpath
import os
from lxml import etree

#Carga el fichero xml en una variable
arbol = etree.parse('ficheroxml.xml')


#Bucle del programa
salir = False

while salir == False:
    os.system('clear')
    print "+-------------------------------------------+"
    print "| Lector de resultados electorales.         |"
    print "|                                           |"
    print "|  Opciones disponibles:                    |"
    print "|  -Conteo de partidos - 1                  |"
    print "|  -Conteo de partidos - 2                  |"
    print "|  -Conteo de partidos - 3                  |"
    print "|  -Conteo de partidos - 4                  |"
    print "|  -Conteo de partidos - 5                  |"
    print "|                                           |"
    print "|(Para salir usal la letra 'q')             |"
    print "+-------------------------------------------+"
    respuesta = raw_input("respuesta: ")

    #Comprobador de respuesta
    if respuesta == "q":
        salir = True

    elif respuesta == 1:
        os.system('clear')
        print "+-----------------------------+"
        print "| Conteo de partidos.         |"
        print "+-----------------------------+"
        raw_input("Pulse enter para continuar")
