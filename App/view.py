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

def artistasNacidosEnRango(catalogo,fechaInicio,fechaFin):
    return controller.artistasNacidosEnRango(catalogo,fechaInicio,fechaFin)

def obrasPorDateAcquired(catalogo,fechaInicio,fechaFin):
    return controller.obrasPorDateAcquired(catalogo,fechaInicio,fechaFin)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Artistas nacidos en un rango de años especifico")
    print("3- Obras adquiridas por el museo en un rango de años especifico")
    print("5- Nacionalidad con mas obras")

def printObrasMasNacionalidad(catalogo):
    nacionalidades=mp.keySet(catalogo)
    i=0
    while i!=lt.size(nacionalidades):
        nacActual=lt.getElement(nacionalidades,i)
        num=mp.get(catalogo,nacActual)['value']
        print("\n"+nacActual+": ",(num))
        i+=1

def printArtistasEnRango(sortedArtist):
    i=1
    j=-4
    artistas=True
    print("Los primeros y últimos tres artistas dentro de ese rango son: \n_______________________________\n")
    while artistas:
        if i!=4:
            artista=lt.getElement(sortedArtist,i)
            i+=1
        else:
            artista=lt.getElement(sortedArtist,j)
            j+=1
            if j==-1:
                artistas=False
        nombre,genero,nacionalidad,nacido,fallece=artista["DisplayName"],artista["Gender"],artista["Nationality"],artista["BeginDate"],artista["EndDate"]
        if nacido=="0":
            nacido="Desconocida"
        if fallece=="0":
            fallece="Desconocida o aún vive"
        if genero=="":
            genero="No reporta"
        if nacionalidad=="":
            nacionalidad="Desconocida"
        print("Nombre: "+nombre+"\nGenero: "+genero+"\nFecha de nacimiento: "+nacido+"\nNacionalidad: "+nacionalidad+"\nFecha de fallemiento: "+fallece+"\n_______________________________\n")
'''
def printArtworksResults(sortedArtworks):
    compradas=0
    z=1
    while z!=lt.size(sortedArtworks):
        credit=lt.getElement(sortedArtworks,z)["CreditLine"]
        if credit!="":
            if "purchase" in (str(credit)).lower():
                compradas+=1
        z+=1
    i=1
    j=-4
    obras=True
    print("El número de obras que fueron compradas por el museo son ",compradas)
    print("Las primeras y últimas tres obras dentro de ese rango son: \n_______________________________\n")
    while obras:
        if i!=4:
            obra=lt.getElement(sortedArtworks,i)
            i+=1
        else:
            obra=lt.getElement(sortedArtworks,j)
            j+=1
            if j==-1:
                obras=False
        nombresArtista=[]
        idArtistasActual=obra["ConstituentID"].replace("["," ").replace("]"," ").replace(","," ,").split(",")
        q=0
        while q!=len(idArtistasActual):
            g=1
            while g!=lt.size(ids):
                iD=lt.getElement(ids,g)[0]
                name=lt.getElement(ids,g)[1]
                if iD == idArtistasActual[q]:
                    nombresArtista.append(name)
                    nombres = ", ".join(nombresArtista)
                g+=1
            q+=1
        titulo,fecha,medio,dimensiones=obra["Title"],obra["Date"],obra["Medium"],obra["Dimensions"]
        if fecha=="":
            fecha="No se conoce la fecha de creación"
        if medio=="":
            medio="No se conoce el medio"
        if dimensiones=="":
            dimensiones="No se conocen las dimensiones de la obras"
        print("Titulo: "+titulo+"\nArtistas: "+nombres+"\nFecha: "+fecha+"\nMedio: "+medio+"\nDimensiones: "+dimensiones+"\n_______________________________\n")
'''







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
        fechaInicio=int(input("Ingrese la fecha inicial del rango:\n"))
        fechaFin=int(input("Ingrese la fecha final del rango:\n"))
        lista=artistasNacidosEnRango(catalogo,fechaInicio,fechaFin)
        print("\nEl numero de artistas nacidos en ese rango de fechas son "+str(lt.size(lista))+'\n')
        printArtistasEnRango(lista)
    elif int(inputs[0]) == 3:
        anioInicio,mesInicio,diaInicio,anioFin,mesFin,diaFin=True,True,True,True,True,True
        print("Ingrese el año inicial en formato de 4 dígitos:")
        anio1=input("")
        while anioInicio:
            if len(anio1)!=4:
                print("El número ingresado tiene un formato invalido")
                anio1=input("")
            else:
                anioInicio=False
        print("Ingrese el mes inicial en formato de 2 dígitos:")
        mes1=input("")
        while mesInicio:
            if len(mes1)!=2:
                print("El número ingresado tiene un formato invalido")
                mes1=input("")
            else:
                mesInicio=False
        print("Ingrese el dia inicial en formato de 2 dígitos:")
        dia1=input("")
        while diaInicio:
            if len(dia1)!=2:
                print("El número ingresado tiene un formato invalido")
                dia1=input("")
            else:
                diaInicio=False
        print("Ingrese el año final en formato de 4 dígitos:")
        anio2=input("")
        while anioFin:
            if len(anio2)!=4:
                print("El número ingresado tiene un formato invalido")
                anio2=input("")
            else:
                anioFin=False
        print("Ingrese el mes final en formato de 2 dígitos:")
        mes2=input("")
        while mesFin:
            if len(mes2)!=2:
                print("El número ingresado tiene un formato invalido")
                mes2=input("")
            else:
                mesFin=False
        print("Ingrese el dia inicial en formato de 2 dígitos:")
        dia2=input("")
        while diaFin:
            if len(dia2)!=2:
                print("El número ingresado tiene un formato invalido")
                dia2=input("")
            else:
                diaFin=False
        fecha1=anio1+"-"+mes1+"-"+dia1
        fecha2=anio2+"-"+mes2+"-"+dia2
        obrasSorted=obrasPorDateAcquired(catalogo,fecha1,fecha2)
        print(obrasSorted)
        print("Entre "+fecha1+" y "+fecha2+" el museo adquirió ",lt.size(obrasSorted)," obras")
        #printArtworksResults(obrasSorted,catalogo)
    elif int(inputs[0]) == 5:
        #lista=masNacionalidad(catalogo)
        #print(mp.get(catalogo["obras"],"78101"))
        lista=obrasNacionalidades(catalogo)
        #printObrasMasNacionalidad(lista)
        print(lista[1])
    elif int(inputs[0]) == 6:
        print(catalogo['fechaAdquisicion'])
    else:
        sys.exit(0)
sys.exit(0)
