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

#Esta función nos permite guardar los datos leidos del fichero en un array de arrays.
array = np.genfromtxt(StringIO(datos), delimiter=",", dtype="|U20", autostrip=True)
#Numero de interfaces a configurar
numConfigs = len(array)
numFila=0



'''
telnet(ip,numFila)
Funcion que recibe una dirección IP y el número de fila del fichero en que se encuentra la ejecución
 y realiza una conexión mediante telnet para configurar las interfaces del componente.

Autor: Javier García González
'''

def telnet(ip,numFila):
    wait = 2
    con = telnetlib.Telnet(ip, 23, 5)

    
    #Se comprueba si es DHCP, en caso afirmativo no se cambia nada.
    if array[numFila][3] == 1:
        print("Es DHCP, no se configura" + "\n")
    else:
        #Se comprueba el tipo de equipo que es, Router o PC
        if array[numFila][0] == 'Router':
        
            con.write("configure terminal" + "\n")
            time.sleep(wait)
            con.write("int " + array[numFila][2] + "\n")
            time.sleep(wait)
            con.write("ip address " + array[numFila][7] + array[numFila][8] + "\n")
            time.sleep(wait)
            con.write("no shutdown" + "\n")
            time.sleep(wait)
            con.write("exit" + "\n")
            time.sleep(wait)
            
            
        if array[numFila][0] == 'PC':
            
            con.write("ifconfig " + array[numFila][2] + " " + array[numFila][7] + " netmask " 
                      + array[numFila][8] + " broadcast " + array[numFila][9] + " up" + "\n")
            time.sleep(wait)        
    
            

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
        
        print("ifconfig " + array[6][2] + " " + array[6][7] + " netmask " + array[6][8] + " broadcast " + array[6][9] + " up" + "\n")

        
        break
                
        
    elif opcionMenu == "2":
        print("")
        input("Lanzando configuración...\n pulsa enter para continuar")
        j=0
        while j <= numConfigs-1:
            telnet(array[j][4],j)
            j+=1
        print("Configuración realizada correctamente.")
        
        break
    
        
        
    elif opcionMenu == "9":
        print("Cerrando conexión...")
        break
    
    else: 
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para volver al menú")
        

    