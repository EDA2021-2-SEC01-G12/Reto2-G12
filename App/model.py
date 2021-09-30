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
    catalog={'artistas':None,'obras':None,'medio':None}
    catalog['artistas']=lt.newList('ARRAY_LIST',compareArtIds)
    catalog['obras']=lt.newList('ARRAY_LIST',compareArtIds)
    catalog['medio']=mp.newMap(1,maptype='CHAINING',loadfactor=4,comparefunction=compareMapMedium)
    return catalog

# Funciones para agregar informacion al catalogo

'''def addAuthors(catalog, author):
    lt.addLast(catalog['books'], book) 
    mp.put(catalog['bookIds'], book['goodreads_book_id'], book) 
    authors = book['authors'].split(",")  
    for author in authors: 
        addBookAuthor(catalog, author.strip(), book) 
    addBookYear(catalog, book)'''
    
def addAuthors(catalog,author):
    lt.addLast(catalog['artistas'],author)

def addArtworks (catalog,artwork):
    lt.addLast(catalog['obras'],artwork)


# Funciones para creacion de datos

# Funciones de consulta

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
