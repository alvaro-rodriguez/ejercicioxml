#!/usr/bin/python
# -*- coding: utf-8 -*-

#"Pre-Enunciado"

"""1.Lista el número de partidos que aparecen en el escrutinio.

2.Muestra el nombre da cada partido y el número de electos de cada uno.

3.Pide el nombre de un partido y muestra sus datos:nombre, número de electos, ide de partido (porcentaje de votos),no se puede, no aparece realmente).

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
    print "| Lector de resultados electorales pare el senado.         |"
    print "|                                           |"
    print "|  Opciones disponibles:                    |"
    print "|  -Conteo de partidos - 1                  |"
    print "|  -Número de electos por partido - 2       |"
    print "|  -Datos concretos de un partido - 3       |"
    print "|  -Buscador por número de electos  - 4     |"
    print "|  -Otros datos - 5                         |"
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
        raiz =arbol.getroot()
        hojas = raiz.findall('resultados/partido')
        for h in hojas:
            if h.find('nombre').text == nonpartido :
                #Las dos líneas poco comprensibles que envuelven los datos sirven para que el encuadre se adapte al largo de los mismos datos.

                print "+-------"+(len(h.findtext('id_partido')))*"-"+"-+-----------"+(len(h.findtext('nombre')))*"-"+"+---------"+(len(h.findtext('electos')))*"-"+"-+"

                print "|Código:"+h.findtext('id_partido'), "|Partido: ", h.find('nombre').text, "|Electos: ", h.find('electos').text+"|"

                print "+-------"+(len(h.findtext('id_partido')))*"-"+"-+-----------"+(len(h.findtext('nombre')))*"-"+"+---------"+(len(h.findtext('electos')))*"-"+"-+"
        raw_input("Pulse enter para continuar")

 


    elif respuesta == "4":
        os.system('clear')
        print "+-------------------------------------+"
        print "| Buscador por número de electos      |"
        print "+-------------------------------------+"
        print "Introduzca el número de electos por el que quiere buscar el partido."
        numel = raw_input("Número de electos: ")
        raiz =arbol.getroot()
        hojas = raiz.findall('resultados/partido')
        banpart = False
        lpart = []
        for h in hojas :
            if h.findtext('electos') == numel:
                lpart.append(h.findtext('nombre'))
                banpart = True
        if banpart == True:
            print "Partidos con %s electos:" % (numel)
            for l in lpart:
                print l

        if banpart == False:
            print "Ningun partido tiene ese número de electos"

        raw_input("Pulse enter para continuar")


    elif respuesta == "5":
        os.system('clear')
        print "+------------------------------------+"
        print "| Otros datos.                       |"
        print "| -Datos generales de la encuesta -1 |"
        print "+------------------------------------+"

        resp2 = raw_input("Opción: ")
        if resp2 == "1":
            os.system('clear')
            print "+----------------------------------+"
            print "| -Datos generales de la encuesta  |"
            print "+----------------------------------+"
            raiz =arbol.getroot()
            print "Tipo de elecciones:", raiz.findtext('nombre_lugar')
            print "Porcentaje de votos escrutado:",raiz.findtext('porciento_escrutados')
            print "Votos contabilizados:",findtext('votos/contabilizados/cantidad')
            print "Porcentaje:",findtext('votos/contabilizados/porcentaje')+"%"
            print "Abstenciones:",findtext('votos/abstenciones/cantidad')
            print "Porcentaje:",findtext('votos/abstenciones/porcentaje')+"%"
            print "Votos nulos:",findtext('votos/nulos/cantidad')
            print "Porcentaje:",findtext('votos/nulos/porcentaje')+"%"
            print "Votos en blanco:",findtext('votos/blanco/cantidad')
            print "Porcentaje:",findtext('votos/blanco/porcentaje')+"%"
            

            raw_input("Pulse enter para continuar")

