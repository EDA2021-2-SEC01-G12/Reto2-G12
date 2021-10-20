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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    catalog = model.initCatalog()
    return catalog

# Funciones para la carga de datos

def addAuthors(catalog):
    authorsFile= cf.data_dir + "Artists-utf8-small.csv" 
    autFile = csv.DictReader(open(authorsFile, encoding='utf-8'))
    for author in autFile:
        model.addAuthors(catalog,author)
        model.addNacionality(catalog,author)
        model.addArtistByBeginDate(catalog,author)

def addArtworks (catalog):
    artworksFile = cf.data_dir + "Artworks-utf8-small.csv"
    art= csv.DictReader (open(artworksFile, encoding="utf-8"))
    for line in art:
        model.addArtworks(catalog,line)
        model.addMedium(catalog,line)
        model.addArtworkOfArtist(catalog,line)
        model.addArtworksByDateAquired(catalog,line)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def artistasNacidosEnRango(catalogo,fechaInicio,fechaFin):
    return model.artistasNacidosEnRango(catalogo,fechaInicio,fechaFin)

def obrasPorDateAcquired(catalogo,fechaInicio,fechaFin):
    return model.obrasPorDateAcquired(catalogo,fechaInicio,fechaFin)

def nacionalidadMasObras(catalogo,nacionalidad):
    return model.nacionalidadMasObras(catalogo,nacionalidad)

def masNacionalidad(catalogo):
    return model.masNacionalidad(catalogo)

def obrasNacionalidades(catalogo):
    return model.obrasNacionalidades(catalogo)