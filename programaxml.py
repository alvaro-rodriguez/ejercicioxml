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
    print "+----------------------------------------------------------+"
    print "| Lector de resultados electorales para el senado.         |"
    print "|                                                          |"
    print "|  Opciones disponibles:                                   |"
    print "|  -Conteo de partidos - 1                                 |"
    print "|  -Número de electos por partido - 2                      |"
    print "|  -Datos concretos de un partido - 3                      |"
    print "|  -Buscador por número de electos  - 4                    |"
    print "|  -Otros datos - 5                                        |"
    print "|  -Imprimir datos en formato html -6                      |"
    print "|                                                          |"
    print "|(Para salir usar la letra 'q')                            |"
    print "+----------------------------------------------------------+"
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
        print "| -Gráficos de las elecciones -2     |"
        print "+------------------------------------+"

        resp2 = raw_input("Opción: ")
        if resp2 == "1":
            os.system('clear')
            print "+----------------------------------+"
            print "|  Datos generales de la encuesta  |"
            print "+----------------------------------+"
            raiz =arbol.getroot()
            print "Tipo de elecciones:", raiz.findtext('nombre_lugar')
            print " -Porcentaje de votos escrutado:",raiz.findtext('porciento_escrutado')
            print "Votos contabilizados:",raiz.findtext('votos/contabilizados/cantidad')
            print " -Porcentaje:",raiz.findtext('votos/contabilizados/porcentaje')+"%"
            print "Abstenciones:",raiz.findtext('votos/abstenciones/cantidad')
            print " -Porcentaje:",raiz.findtext('votos/abstenciones/porcentaje')+"%"
            print "Votos nulos:",raiz.findtext('votos/nulos/cantidad')
            print " -Porcentaje:",raiz.findtext('votos/nulos/porcentaje')+"%"
            print "Votos en blanco:",raiz.findtext('votos/blancos/cantidad')
            print " -Porcentaje:",raiz.findtext('votos/blancos/porcentaje')+"%"
            

            raw_input("Pulse enter para continuar")

        elif resp2 == "2":
            os.system('clear')
            print "+----------------------------------+"
            print "|   Gráficos de las elecciones     |"
            print "+----------------------------------+"

            raiz = arbol.getroot()
            part = raiz.findall('resultados/partido')
            nupart = int(raw_input("Diga el número de partidos que quiere que aparezcan:"))
            con =0
            print "+"+"-"*26+"+"+"---------+10-------+20-------+30-------+40-------+50-------+60-------+70"
            for p in part:
                print "|"+p.findtext('nombre') , p.findtext('electos'),
                print "|"+ str(round(float(p.findtext('electos'))*100/208,2))+"%",
                print " "*(20-(len(p.find('nombre').text)+len(p.findtext('electos'))+len(str(round(float(p.findtext('electos'))*100/208,2))))),
                print "|"+int(p.findtext('electos'))*100/208*"="

                con = con +1
                if con == nupart:
                    break
                
            print "+"+"-"*26+"+"+"---------+10-------+20-------+30-------+40-------+50-------+60-------+70"
            raw_input("Pulse enter para continuar")

    elif respuesta == "6":
        os.system('clear')
        print "+--------------------------------+"
        print "| Imprimir datos en html.        |"
        print "+--------------------------------+"
        raiz = arbol.getroot()
        hojas = raiz.findall('resultados/partido')
        print "Elija el nombre que quiere dar al fichero html."
        nomh = raw_input("Nombre: ")
        os.mknod(nomh)
        print "Muestra previa de los datos "
        for h in hojas:
            print "<h1>",h.findtext('nombre'),"</h1>"
            print "<p>",h.findtext('electos'),"</p>"
        print "<ul>"
        print "    <li>",raiz.findtext('votos/contabilizados/porcentaje')+"%","</li>"
        print "    <li>",raiz.findtext('votos/abstenciones/porcentaje')+"%","</li>"
        print "    <li>",raiz.findtext('votos/nulos/porcentaje')+"%","</li>"
        print "    <li>",raiz.findtext('votos/blancos/porcentaje')+"%","</li>"
        print "</ul>"

        print "Si desea guardad estos datos en un fichero escriba 'yes'."
        resp3 = raw_input("¿Escribir datos? ")
        if resp3 == "yes":
            fichero = open(nomh,"r+")
            for h in hojas:
                fichero.write( "<h1>"+h.findtext('nombre')+"</h1>"+"\n")
                fichero.write( "<p>"+h.findtext('electos')+"</p>"+"\n")
            
            fichero.write( "<ul>"+"\n")
            fichero.write(" <li>"+raiz.findtext('votos/contabilizados/porcentaje')+"%"+"</li>"+"\n")
            fichero.write(" <li>"+raiz.findtext('votos/abstenciones/porcentaje')+"%"+"</li>"+"\n")
            fichero.write(" <li>"+raiz.findtext('votos/nulos/porcentaje')+"%"+"</li>"+"\n")
            fichero.write(" <li>"+raiz.findtext('votos/blancos/porcentaje')+"%"+"</li>"+"\n")
            fichero.write("</ul>"+"\n")

            fichero.close()
        
                    
        raw_input("Pulse enter para continuar")
print "++-----------------++"
print "||Fin del programa.||"
print "++-----------------++"
