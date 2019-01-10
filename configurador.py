import os
import numpy as np
from io import StringIO

archivo = open("fichero.txt")
archivo.seek(0)
datos = archivo.read()
archivo.close()

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
        array = np.genfromtxt(StringIO(datos), delimiter=",", dtype="|U20", autostrip=True)
        print(array)
        print("")
        
        break
        
        '''
        for linea in archivo:
            for palabra in linea.split(","):
                print(palabra)
        '''
                
        
    elif opcionMenu == "2":
        print("")
        input("Lanzando configuración...\n pulsa enter para empezar")
        
        break
    
        
        
    elif opcionMenu == "9":
        break
    
    else: 
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")