"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp
import time

default_limit = 1000 
sys.setrecursionlimit(default_limit*10)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def masNacionalidad(catalogo):
    return controller.masNacionalidad(catalogo)

def obrasNacionalidades(catalogo):
    return controller.obrasNacionalidades(catalogo)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar obras cuyos autores sean de una nacionalidad especifica")
    print("5- Nacionalidad con mas obras")

def printObrasMasNacionalidad(catalogo):
    nacionalidades=mp.keySet(catalogo)
    i=0
    while i!=lt.size(nacionalidades):
        nacActual=lt.getElement(nacionalidades,i)
        num=mp.get(catalogo,nacActual)['value']
        print("\n"+nacActual+": ",(num))
        i+=1
catalogo = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalogo = controller.initCatalog()
        start_time = time.process_time()
        controller.addAuthors(catalogo)
        controller.addArtworks(catalogo)
        stop_time= time.process_time()
        timeSort= (stop_time-start_time)*1000
        print(str(timeSort)+'milisegundos')
    elif int(inputs[0]) == 2:
        nac=input("Ingrese la nacionalidad a consultar:\n")
        obrasMas=controller.nacionalidadMasObras(catalogo,nac)
        print(obrasMas)
    elif int(inputs[0]) == 5:
        #lista=masNacionalidad(catalogo)
        #print(mp.get(catalogo["obras"],"78101"))
        lista=obrasNacionalidades(catalogo)
        #printObrasMasNacionalidad(lista)
        print(lista[1])
    else:
        sys.exit(0)
sys.exit(0)
