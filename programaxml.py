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
import sys
reload(sys)
sys.setdefaultencoding('utf8')


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
    print "|  -Número de electos por partido - 2       |"
    print "|  -Datos concretos de un partido - 3       |"
    print "|  -Conteo de partidos - 4                  |"
    print "|  -Conteo de partidos - 5                  |"
    print "|                                           |"
    print "|(Para salir usar la letra 'q')             |"
    print "+-------------------------------------------+"
    respuesta = raw_input("respuesta: ")

    #Comprobador de respuesta
    if respuesta == "q":
        salir = True

    elif respuesta == "1":
        os.system('clear')
        print "+-----------------------------+"
        print "| Conteo de partidos.         |"
        print "+-----------------------------+"
        hojas = arbol.xpath('/escrutinio_sitio/resultados/partido/nombre')
        print "El número de partidos que se han presentado es: %i " %(len(hojas))
        raw_input("Pulse enter para continuar")
        


    elif respuesta == "2":
        os.system('clear')
        print "+--------------------------------+"
        print "| Número de electos por partido. |"
        print "+--------------------------------+"
        hojas =arbol.xpath('/escrutinio_sitio/resultados/partido')
        #print hojas
        
        for h in hojas:
            print "Partido: " , h[1].text,"Electos:",h[2].text
            
        raw_input("Pulse enter para continuar")




    elif respuesta == "3":
        os.system('clear')
        print "+----------------------------------------+"
        print "| Datos concretos de un partido.         |"
        print "+----------------------------------------+"
        print "Introduzca el nombre del partido sobre le que desea buscar:"
        nonpartido = raw_input(":")

        #Creación de orden xpath:
        #orden = "escrutinio_sitio/resultados/partido/nombre[text='"+nonpartido+"']"
        #print "La orden es :" ,orden
        raiz =arbol.getroot()

        hojas = raiz.findall('escrutinio_sitio/resultados')
        print raiz
        print hojas
        for h in hojas:
            print h.text
            print h.find('partido/nombre').text
        raw_input("Pulse enter para continuar")
"""
 


   elif respuesta == "4":
        os.system('clear')
        print "+-----------------------------+"
        print "| Conteo de partidos.         |"
        print "+-----------------------------+"
        raw_input("Pulse enter para continuar")

    


elif respuesta == "5":
        os.system('clear')
        print "+-----------------------------+"
        print "| Conteo de partidos.         |"
        print "+-----------------------------+"
        raw_input("Pulse enter para continuar")
"""
