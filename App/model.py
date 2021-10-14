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
    mp.put(catalog["medio"],med,artwork)

def addNacionality(catalog,artist):
    nat=artist['Nationality']
    mp.put(catalog["nacionalidad"],nat,artist)

def addArtworkOfArtist(catalog,obra):
    IDs=str(obra["ConstituentID"]).replace("[","").replace("]","").replace(" ","").split(",")
    j=0
    while j!=len(IDs):
        mp.put(catalog["obrasArtista"],IDs[j],obra)
        j+=1


# Funciones para creacion de datos

# Funciones de consulta   

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

# Funciones de ordenamiento



''''''