'''
Programa Python que lee los datos del router y equipos terminales de una red y lanza
los comandos necesarios para modificar las IPs, Máscaras de red y Puertas de enlace.

Autor: Javier García González
Organización: Universidad de Burgos
Versión: 3.1
Fecha última versión: 04/02/2019
'''

import os
import numpy as np
from io import StringIO
import telnetlib
import time



archivo = open("fichero.txt")
archivo.seek(0)
datos = archivo.read()
archivo.close()



'''
menu()
Funciona que nos muestra una serie de opciones para ver leer el fichero de configuración
o lanzar las configuraciones.

Autor: Javier García González
'''
def menu():
    
    os.system('cls')
    
    print("Opciones")
    print("\t1 - Leer configuración")
    print("\t2 - Lanzar Configuración")
    print("\t9 - Salir")
    

while True:
    menu()
    opcionMenu = input("Inserta numero -> ")
    if opcionMenu == "1":
        #Esta función nos permite guardar los datos leidos del fichero en un array de arrays.
        array = np.genfromtxt(StringIO(datos), delimiter=",", dtype="|U20", autostrip=True)
        print(array[0][0])
        print(array[0][5])
        print(array[0][7])
        
        break
                
        
    elif opcionMenu == "2":
        print("")
        input("Lanzando configuración...\n pulsa enter para continuar")
        telnet()
        if array[0][0] == "Router":
            print("OK")
            
        
        print("Configuración realizada correctamente.")
        
        break
    
        
        
    elif opcionMenu == "9":
        print("Cerrando conexión...")
        break
    
    else: 
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para volver al menú")
        
        
        

'''
telnet(ip)
Funcion que recibe una dirección IP y realiza una conexión mediante telnet para configurar las interfaces
del componente.

Autor: Javier García González
'''

def telnet(ip):
    wait = 2
    con = telnetlib.Telnet(ip, 23, 5)
    
    con.write("configure terminal" + "\n")
    time.sleep(wait)
    
    con.write("int f2/0" + "\n")
    time.sleep(wait)
    con.write("ip address 192.168.0.1 255.255.255.0" + "\n")
    
    
    
    
    
    
    