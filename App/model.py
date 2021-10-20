"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def initCatalog():
    catalog={'artistas':None,'obras':None,"obrasArtista":None,'medio':None,'nacionalidad':None}
    catalog['artistas']=mp.newMap(1949,maptype="PROBING",loadfactor=0.5)
    catalog['obras']=mp.newMap(837,maptype="PROBING",loadfactor=0.5)
    catalog["obrasArtista"]=mp.newMap(maptype="CHAINING",loadfactor=1.5)
    catalog['medio']=mp.newMap(maptype="CHAINING",loadfactor=1.5)
    catalog['nacionalidad']=mp.newMap(maptype='CHAINING',loadfactor=8.0)
    return catalog

# Funciones para agregar informacion al catalogo
    
def addAuthors(catalog,author):
    id=(author["ConstituentID"].replace(" ",""))
    mp.put(catalog["artistas"],id,author)

def addArtworks (catalog,artwork):
    id=artwork["ObjectID"]
    mp.put(catalog["obras"],id,artwork)

def addMedium(catalog,artwork):
    med=artwork["Medium"]
    if mp.contains(catalog['medio'],med)==False:
        obras=lt.newList("ARRAY_LIST")
        lt.addLast(obras,artwork)
        mp.put(catalog["medio"],med,obras)
    else:
        obras=mp.get(catalog['medio'],med)['value']
        lt.addLast(obras,artwork)

def addNacionality(catalog,artist):
    nat=artist['Nationality']
    if mp.contains(catalog['nacionalidad'],nat)==False:
        artistas=lt.newList("ARRAY_LIST")
        lt.addLast(artistas,artist)
        mp.put(catalog["nacionalidad"],nat,artistas)
    else:
        artistas=mp.get(catalog['nacionalidad'],nat)['value']
        lt.addLast(artistas,artist)

def addArtworkOfArtist(catalog,obra):
    IDs=str(obra["ConstituentID"]).replace("[","").replace("]","").replace(" ","").split(",")
    j=0
    while j!=len(IDs):
        if mp.contains(catalog['obrasArtista'],IDs[j])==False:
            obras=lt.newList("ARRAY_LIST")
            lt.addLast(obras,obra)
            mp.put(catalog["obrasArtista"],IDs[j],obras)
        else:
            obras=mp.get(catalog['obrasArtista'],IDs[j])['value']
            lt.addLast(obras,obra)
        j+=1


# Funciones para creacion de datos

# Funciones de consulta   
'''
def nacionalidadMasObras(catalogo,nacionalidad):
    obrasMasNacion=lt.newList('ARRAY_LIST')
    authors=catalogo['artistas']
    autoresIDs=mp.keySet(authors)
    i=1
    while i != lt.size(autoresIDs):
        id=lt.getElement(autoresIDs,i)
        autor=mp.get(authors,id)['value']
        if autor['Nationality']==nacionalidad:
            obras=(mp.get(catalogo["obrasArtista"],id))
            if obras!=None:
                obras=(mp.get(catalogo["obrasArtista"],id))['value']
                lt.addLast(obrasMasNacion,obras)
        i+=1
    return obrasMasNacion

def masNacionalidad(catalogo):
    nacionalidadesKeys=mp.keySet(catalogo["nacionalidad"])
    obrasNacionalidad=mp.newMap(lt.size(nacionalidadesKeys),maptype="PROBING")
    i=0
    while i !=lt.size(nacionalidadesKeys):
        nac=lt.getElement(nacionalidadesKeys,i)
        obras=nacionalidadMasObras(catalogo,nac)
        mp.put(obrasNacionalidad,nac,obras)
        i+=1
    return obrasNacionalidad

def masNacionalidad(catalogo):
    autores=catalogo['artistas']
    artworks=mp.keySet(catalogo["obras"])
    nacObras=mp.newMap(837,maptype="CHAINING")
    numObras={}
    i=0
    while i != mp.size(catalogo["obras"]):
        obraKey=lt.getElement(artworks,i)
        obra=mp.get(catalogo["obras"],obraKey)
        ids=(obra["value"]["ConstituentID"]).replace("[","").replace("]","").replace(" ","").split(",")
        for j in ids:
            nac=mp.get(autores,j)["value"]["Nationality"]
            mp.put(nacObras,nac,obra)
        i+=1
    nacio=mp.keySet(nacObras)
    k=0
    while k!= lt.size(nacio):
        nacionalidad=lt.getElement(nacio,k)
        num=len(mp.get(nacObras,nacionalidad))
        numObras[nacionalidad]=num
    return nacObras,numObras
'''

def obrasNacionalidades(catalogo):
    autores=catalogo["artistas"]
    nacionalidades=mp.newMap(maptype="PROBING")
    obrasArtistas=catalogo["obrasArtista"]
    idsAutores=mp.keySet(obrasArtistas)
    i=0
    while i!=lt.size(idsAutores):
        autor=lt.getElement(idsAutores,i)
        nac=mp.get(autores,autor)["value"]["Nationality"]
        obras=mp.get(obrasArtistas,autor)['value']
        if mp.contains(nacionalidades,nac)==False:
            obrasNac=lt.newList("ARRAY_LIST")
            for a in obras:
                lt.addLast(obrasNac,a)
            mp.put(nacionalidades,nac,obrasNac)
        else:
            listaDeObras=mp.get(nacionalidades,nac)['value']
            for b in obras:
                lt.addLast(listaDeObras,b)
        i+=1
    nac=mp.keySet(nacionalidades)
    j=0
    masNac=lt.newList("ARRAY_LIST")
    while j!=lt.size(nac):
        nacActual=lt.getElement(nac,j)
        num=lt.size(mp.get(nacionalidades,nacActual)['value'])
        lt.addLast(masNac,(nacActual,num))
        j+=1
    #masNac=ms.sort(masNac)
    return nacionalidades,masNac

# Funciones utilizadas para comparar elementos dentro de una lista

def compareMapMedium(id,entry):
    identry =  me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareArtIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

#def cmpNacionalidadesKeys(catalogo,nac1,nac2):

# Funciones de ordenamiento



''''''