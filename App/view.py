﻿"""
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
from DISClib.DataStructures import mapentry as me
import time

default_limit = 1000 
sys.setrecursionlimit(default_limit*10)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def obrasNacionalidades(catalogo):
    return controller.obrasNacionalidades(catalogo)

def artistasNacidosEnRango(catalogo,fechaInicio,fechaFin):
    return controller.artistasNacidosEnRango(catalogo,fechaInicio,fechaFin)

def obrasPorDateAcquired(catalogo,fechaInicio,fechaFin):
    return controller.obrasPorDateAcquired(catalogo,fechaInicio,fechaFin)

def transportarObrasDepartamento(catalogo,departamento):
    return controller.transportarObrasDepartamento(catalogo,departamento)

def precioObrasMasCostosas(catalogo,departamento):
    return controller.precioObrasMasCostosas(catalogo,departamento)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Artistas nacidos en un rango de años especifico")
    print("3- Obras adquiridas por el museo en un rango de años especifico")
    print("5- Nacionalidad con mas obras")
    print("6. Consultar costo de transporte de las obras de un departamento especifico")

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
    j=lt.size(sortedArtist)-2
    artistas=True
    print("Los primeros y últimos tres artistas dentro de ese rango son: \n_________________________________________________________________________________________________________________________\n")
    while artistas:
        if i!=4:
            artista=lt.getElement(sortedArtist,i)
            i+=1
        else:
            artista=lt.getElement(sortedArtist,j)
            j+=1
            if j==lt.size(sortedArtist)+1:
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
        print("- Nombre: "+nombre+"\n- Genero: "+genero+"\n- Fecha de nacimiento: "+nacido+"\n- Nacionalidad: "+nacionalidad+"\n- Fecha de fallemiento: "+fallece+"\n_________________________________________________________________________________________________________________________\n")

def printArtworksResults(sortedArtworks):
    compradas=0
    for ob in lt.iterator(sortedArtworks):
        credit=ob["CreditLine"]
        if credit!="":
            if "purchase" in (str(credit)).lower():
                compradas+=1
    i=1
    j=lt.size(sortedArtworks)-2
    obras=True
    print("El número de obras que fueron compradas por el museo son ",compradas)
    print("Las primeras y últimas tres obras dentro de ese rango son: \n_________________________________________________________________________________________________________________________\n")
    while obras:
        if i!=4:
            obra=lt.getElement(sortedArtworks,i)
            i+=1
        else:
            obra=lt.getElement(sortedArtworks,j)
            j+=1
            if j==lt.size(sortedArtworks)+1:
                obras=False
        nombresArtista=[]
        idArtistasActual=obra["ConstituentID"].replace("[","").replace("]","").replace(" ","").split(",")
        q=0
        while q!=len(idArtistasActual):
            nombre=me.getValue(mp.get(catalogo['artistas'],idArtistasActual[q]))['DisplayName']
            nombresArtista.append(nombre)
            q+=1
            nombres=", ".join(nombresArtista)
        titulo,fecha,medio,dimensiones,dateAc=obra["Title"],obra["Date"],obra["Medium"],obra["Dimensions"],obra['DateAcquired']
        if fecha=="":
            fecha="No se conoce la fecha de creación"
        if medio=="":
            medio="No se conoce el medio"
        if dimensiones=="":
            dimensiones="No se conocen las dimensiones de la obras"
        print("- Titulo: "+titulo+"\n- Artistas: "+nombres+"\n- Fecha: "+fecha+"\n- Medio: "+medio+"\n- Dimensiones: "+dimensiones+"\n- Fecha de Adquisicion: "+dateAc+"\n_________________________________________________________________________________________________________________________\n")


def printMasNacionalidadTop10(natioNumDict,natioObrasMap):
    i=1
    print("\nEl TOP 10 nacionalidades con mas obras es el siguiente: \n")
    while i!=11:
        nac,num=lt.getElement(natioNumDict,i)[0],lt.getElement(natioNumDict,i)[1]
        print(nac+": "+str(num)+" obras\n")
        i+=1
    masNac=lt.getElement(natioNumDict,1)[0]
    obrasMasNac=me.getValue(mp.get(natioObrasMap,masNac))
    a=1
    b=lt.size(obrasMasNac)-2
    obras=True
    print("Las primeras y últimas tres obras dentro de ese rango son: \n_________________________________________________________________________________________________________________________\n")
    while obras:
        if a!=4:
            obra=lt.getElement(obrasMasNac,a)
            a+=1
        else:
            obra=lt.getElement(obrasMasNac,b)
            b+=1
            if b==lt.size(obrasMasNac)+1:
                obras=False
        titulo,date,medio,dimensiones=obra['Title'],obra['Date'],obra['Medium'],obra['Medium']
        nombresArtista=[]
        idArtistasActual=obra["ConstituentID"].replace("[","").replace("]","").replace(" ","").split(",")
        q=0
        while q!=len(idArtistasActual):
            nombre=me.getValue(mp.get(catalogo['artistas'],idArtistasActual[q]))['DisplayName']
            nombresArtista.append(nombre)
            q+=1
            nombres=", ".join(nombresArtista)
        if date=="":
            date="No se conoce la fecha de creación"
        if medio=="":
            medio="No se conoce el medio"
        if dimensiones=="":
            dimensiones="No se conocen las dimensiones de la obras"
        print("- Titulo: "+titulo+"\n- Artistas: "+nombres+"\n- Fecha: "+date+"\n- Medio: "+medio+"\n- Dimensiones: "+dimensiones+"\n_________________________________________________________________________________________________________________________\n")

def print5ObrasPorFecha(listaOrdenada,catalogo):
    i=1
    print("Las 5 obras mas antiguas de este departamento son: \n_________________________________________________________________________________________________________________________\n")
    while i!=6:
        obra=lt.getElement(listaOrdenada,i)
        titulo,clasificacion,fecha,medio,dimensiones,precio=obra['Title'],obra['Classification'],obra['Date'],obra['Medium'],obra['Dimensions'],obra['Precio']
        nombresArtista=[]
        idArtistasActual=obra["ConstituentID"].replace("[","").replace("]","").replace(" ","").split(",")
        q=0
        while q!=len(idArtistasActual):
            nombre=me.getValue(mp.get(catalogo['artistas'],idArtistasActual[q]))['DisplayName']
            nombresArtista.append(nombre)
            q+=1
            nombres=", ".join(nombresArtista)
        if fecha=="":
            fecha="No se conoce la fecha de creación"
        if medio=="":
            medio="No se conoce el medio"
        if dimensiones=="":
            dimensiones="No se conocen las dimensiones de la obras"
        print("- Titulo: "+titulo+"\n- Artistas: "+nombres+"\n- Clasificacion: "+clasificacion+"\n- Fecha: "+fecha+"\n- Medio: "+medio+"\n- Dimensiones: "+dimensiones+"\n- Costo de transporte: "+str(precio)+"\n_________________________________________________________________________________________________________________________\n")
        i+=1

def obrasMasCoste(precios,catalogo):
    j=1
    print("Las 5 obras de este departamento mas costosas para transportar son: \n_________________________________________________________________________________________________________________________\n")
    while j!=6:
        obra=lt.getElement(precios,j)
        titulo,clasificacion,fecha,medio,dimensiones,precio=obra['Title'],obra['Classification'],obra['Date'],obra['Medium'],obra['Dimensions'],obra['Precio']
        nombresArtista=[]
        idArtistasActual=obra["ConstituentID"].replace("[","").replace("]","").replace(" ","").split(",")
        a=0
        while a!=len(idArtistasActual):
            nombre=me.getValue(mp.get(catalogo['artistas'],idArtistasActual[a]))['DisplayName']
            nombresArtista.append(nombre)
            a+=1
            nombres=", ".join(nombresArtista)
        if fecha=="":
            fecha="No se conoce la fecha de creación"
        if medio=="":
            medio="No se conoce el medio"
        if dimensiones=="":
            dimensiones="No se conocen las dimensiones de la obras"
        print("- Titulo: "+titulo+"\n- Artistas: "+nombres+"\n- Clasificacion: "+clasificacion+"\n- Fecha: "+fecha+"\n- Medio: "+medio+"\n- Dimensiones: "+dimensiones+"\n- Costo de transporte: "+str(precio)+"\n_________________________________________________________________________________________________________________________\n")
        j+=1

#Catalogo vacio 

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
        start_time = time.process_time()
        lista=artistasNacidosEnRango(catalogo,fechaInicio,fechaFin)
        print("\nEl numero de artistas nacidos en ese rango de fechas son "+str(lt.size(lista))+'\n')
        printArtistasEnRango(lista)
        stop_time= time.process_time()
        timeSort= (stop_time-start_time)*1000
        print(str(timeSort)+'milisegundos')
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
        start_time = time.process_time()
        obrasSorted=obrasPorDateAcquired(catalogo,fecha1,fecha2)
        print("Entre "+fecha1+" y "+fecha2+" el museo adquirió ",lt.size(obrasSorted)," obras")
        printArtworksResults(obrasSorted)
        stop_time= time.process_time()
        timeSort= (stop_time-start_time)*1000
        print(str(timeSort)+'milisegundos')
    elif int(inputs[0]) == 5:
        start_time = time.process_time()
        lista=obrasNacionalidades(catalogo)
        printMasNacionalidadTop10(lista[1],lista[0])
        stop_time= time.process_time()
        timeSort= (stop_time-start_time)*1000
        print(str(timeSort)+'milisegundos')
    elif int(inputs[0]) == 6:
        departamento=input("Ingrese el departamento a consultar\n")
        start_time = time.process_time()
        lista=transportarObrasDepartamento(catalogo,departamento)
        print("\nEl numero de obras que pertenecen a este departamento son "+str(lt.size(lista[0]))+"\n")
        print("El peso estimado de las obras a transportar es de "+str(lista[1])+" kg\n")
        print("El costo estimado para transportar las obras es de "+str(round(lista[3],3))+" dolares\n")
        print5ObrasPorFecha(lista[2],catalogo)
        obrasCostosas=precioObrasMasCostosas(catalogo,departamento)
        obrasMasCoste(obrasCostosas,catalogo)
        stop_time= time.process_time()
        timeSort= (stop_time-start_time)*1000
        print(str(timeSort)+'milisegundos')
    elif int(inputs[0]) == 7:
        print(mp.keySet(catalogo['fechaAdquisicion']))
    else:
        sys.exit(0)
sys.exit(0)
