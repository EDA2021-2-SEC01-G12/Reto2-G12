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
    catalog['medio']=mp.newMap(maptype="CHAINING",loadfactor=8.0)
    catalog['nacionalidad']=mp.newMap(maptype='CHAINING',loadfactor=8.0)
    catalog['fechaNacimiento']=mp.newMap(maptype="CHAINING",loadfactor=8.0)
    catalog['fechaAdquisicion']=mp.newMap(maptype="CHAINING",loadfactor=8.0)
    catalog['departamentos']=mp.newMap(maptype="CHAINING",loadfactor=8.0)
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
        artistasLista=mp.get(catalog['nacionalidad'],nat)['value']
        lt.addLast(artistasLista,artist)

def addArtworkOfArtist(catalog,obra):
    IDs=str(obra["ConstituentID"]).replace("[","").replace("]","").replace(" ","").split(",")
    j=1
    while j!=len(IDs):
        if mp.contains(catalog['obrasArtista'],IDs[j])==False:
            obras=lt.newList("ARRAY_LIST")
            lt.addLast(obras,obra)
            mp.put(catalog["obrasArtista"],IDs[j],obras)
        else:
            obras=mp.get(catalog['obrasArtista'],IDs[j])['value']
            lt.addLast(obras,obra)
        j+=1

def addArtistByBeginDate(catalogo,artista):
    fecha=artista['BeginDate']
    if not mp.contains(catalogo['fechaNacimiento'],fecha):
        artistas=lt.newList("ARRAY_LIST")
        lt.addLast(artistas,artista['ConstituentID'])
        mp.put(catalogo['fechaNacimiento'],fecha,artistas)
    else:
        listaArtistas=me.getValue(mp.get(catalogo['fechaNacimiento'],fecha))
        lt.addLast(listaArtistas,artista['ConstituentID'])

def addArtworksByDateAquired(catalogo,artwork):
    date=artwork['DateAcquired']
    if not mp.contains(catalogo['fechaAdquisicion'],date):
        obras=lt.newList("ARRAY_LIST")
        lt.addLast(obras,artwork['ObjectID'])
        mp.put(catalogo['fechaAdquisicion'],date,obras)
    else:
        listaArtistas=mp.get(catalogo['fechaAdquisicion'],date)['value']
        lt.addLast(listaArtistas,artwork['ObjectID'])

def addDepartment(catalogo,obra):
    departamento=obra['Department']
    if not mp.contains(catalogo['departamentos'],departamento):
        depart=lt.newList("ARRAY_LIST")
        lt.addLast(depart,obra)
        mp.put(catalogo['departamentos'],departamento,depart)
    else:
        departamentos=me.getValue(mp.get(catalogo['departamentos'],departamento))
        lt.addLast(departamentos,obra)

# Funciones para creacion de datos

# Funciones de consulta   

def artistasNacidosEnRango(catalogo,fechaInicio,fechaFin):
    artistas=lt.newList("ARRAY_LIST")
    llaves=mp.keySet(catalogo['fechaNacimiento'])
    for fecha in lt.iterator(llaves):
        if fechaFin>=int(fecha)>=fechaInicio:
            ids=me.getValue(mp.get(catalogo['fechaNacimiento'],fecha))
            for IDe in lt.iterator(ids):
                datosAutor=me.getValue(mp.get(catalogo['artistas'],IDe))
                lt.addLast(artistas,datosAutor)
    artistas=ms.sort(artistas,cmpArtistasBeginDate)
    return artistas

def obrasPorDateAcquired(catalogo,fechaInicio,fechaFin):
    fechaInicio=int(fechaInicio.replace("-","")) 
    fechaFin=int(fechaFin.replace("-",""))
    obras=lt.newList("ARRAY_LIST")
    llaves=mp.keySet(catalogo['fechaAdquisicion'])
    for fecha in lt.iterator(llaves):
        if fecha!="":
            fechaAdq=int(fecha.replace("-",""))
        else:
            fechaAdq=0
        if fechaInicio<=fechaAdq<=fechaFin:
            ids=me.getValue(mp.get(catalogo['fechaAdquisicion'],fecha))
            for obra in lt.iterator(ids):
                datosObra=me.getValue(mp.get(catalogo['obras'],obra))
                lt.addLast(obras,datosObra)
    obras=ms.sort(obras,cmpObrasDateAquired)
    return obras

def obrasNacionalidades(catalogo):
    nacionalidades=mp.newMap(maptype="CHAINING",loadfactor=8.0)
    keysNac=mp.keySet(catalogo['obras'])
    for idObra in lt.iterator(keysNac):
        obraIDS=me.getValue(mp.get(catalogo['obras'],idObra))['ConstituentID'].replace("[","").replace("]","").replace(" ","").split(",")
        obraNac=[]
        for x in obraIDS:
            nacio=me.getValue(mp.get(catalogo['artistas'],x))['Nationality']
            obraNac.append(nacio)
        for j in obraNac:
            if j=="" or j =="Nationality unknown":
                j="Nacionalidad desconocida"
            if not mp.contains(nacionalidades,j):
                nacionalidadesObras=lt.newList("ARRAY_LIST")
                lt.addLast(nacionalidadesObras,me.getValue(mp.get(catalogo['obras'],idObra)))
                mp.put(nacionalidades,j,nacionalidadesObras)
            else:
                nacioObras=me.getValue(mp.get(nacionalidades,j))
                lt.addLast(nacioObras,me.getValue(mp.get(catalogo['obras'],idObra)))
    natioKeys=mp.keySet(nacionalidades)
    natioNum=lt.newList("SINGLE_LINKED")
    for key in lt.iterator(natioKeys):
        num=lt.size(me.getValue(mp.get(nacionalidades,key)))
        tup=(key,num)
        lt.addLast(natioNum,tup)
    natioNum=ms.sort(natioNum,cmpNacionalidades)
    mas=lt.getElement(natioNum,1)[0]
    listaMas=me.getValue(mp.get(nacionalidades,mas))
    listaMas=sa.sort(listaMas,cmpObrasPorTitulo)
    return nacionalidades,natioNum

def transportarObrasDepartamento(catalogo,departamento):
    pass

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtistasBeginDate(artista1,artista2):
    artista1=int(artista1["BeginDate"])
    artista2=int(artista2["BeginDate"])
    if artista1 < artista2:
        return True
    else:
        return False

def cmpObrasDateAquired(artwork1,artwork2):
    art1=int(artwork1['DateAcquired'].replace("-",""))
    art2=int(artwork2['DateAcquired'].replace("-",""))
    if art1 < art2:
        return True
    else:
        return False

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

def cmpNacionalidades(nac1,nac2):
    nacio1=int(nac1[1])
    nacio2=int(nac2[1])
    if nacio1>nacio2:
        return True
    else:
        return False

def cmpObrasPorTitulo(obra1,obra2):
    obra1Titulo=obra1['Title']
    obra2Titulo=obra2['Title']
    if obra1Titulo < obra2Titulo:
        return True
    else:
        return False

# Funciones de ordenamiento



''''''