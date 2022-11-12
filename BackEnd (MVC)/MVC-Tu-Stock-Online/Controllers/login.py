 #Ingresar cuenta()
 # Importacion de Librerias
# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""from sys import path
path.append('..\\modules') # lo que esta entre parentesis el la ruta o estructura de carpetas que contiene al modulo a importar.
import module"""
import getpass
import os
import sqlite3
import sys
import time

#declaracion de variables
 
usuariosRegistrados = ('KathyDally','KimCol','GuestUser')
passRegistradas = ('code2016')
 
#declaracion de funciones
def login(usuario,contraseña):
    if usuario in usuariosRegistrados:
        if contraseña in passRegistradas:
            return 1
        else:
            print("\n\tCONTRASEÑA NO COINCIDE...\n")
    else:
        return 2
 
 #inicializacion de procesos
usuario=input('Usuario: ')
contraseña = getpass.getpass('Contraseña: ')
 
if login(usuario,contraseña)==1:
    print('BIENVENIDO ',usuario)
else:
    print('ERROR! USUARIO NO REGISTRADO.')

#Cerrar sesión()

#Recuperar contraseña()



#Ingresar cuenta()

#Cerrar sesión()

#Recuperar contraseña()

