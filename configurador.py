'''
Programa Python que lee los datos del router y equipos terminales de una red y lanza
los comandos necesarios para modificar las IPs, Máscaras de red y Puertas de enlace.

@author: Javier García González
'''

import os
import numpy as np
from io import StringIO
import telnetlib



archivo = open("fichero.txt")
archivo.seek(0)
datos = archivo.read()
archivo.close()
host = "localhost"
tn = telnetlib.Telnet(host)

def menu():
    
    os.system('cls')
    
    print("Opciones")
    print("\t1 - Leer configuración")
    print("\t2 - Lanzar Configuración")
    print("\t9 - Salir")
    

'''
Función que lanza un menú que nos muestra 3 opciones:
    1. Ver el fichero que contiene los datos para la configuración.
    2. Lanzar las configuraciones a realizar.
    3. Salir del menú
'''
while True:
    menu()
    opcionMenu = input("Inserta numero -> ")
    if opcionMenu == "1":
        #Esta función nos permite guardar los datos leidos del fichero en un array de arrays.
        array = np.genfromtxt(StringIO(datos), delimiter=",", dtype="|U20", autostrip=True)
        print(array[0][0])
        print(array[0][6])
        print(array[0][7])
        
        break
                
        
    elif opcionMenu == "2":
        print("")
        input("Lanzando configuración...\n pulsa enter para continuar")
        if array[0][0] == "Router":
            print("OK")
            
        tn.write("enable")
        
        print("Configuración realizada correctamente.")
        
        break
    
        
        
    elif opcionMenu == "9":
        break
    
    else: 
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para volver al menú")