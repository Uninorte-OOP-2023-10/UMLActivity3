from __future__ import annotations
from typing import List

from person.persona import Artista, Invitado, Locutor
from program.cancion import Cancion
from program.programa import Emision, Programa

class RockRollRadio:

    def __init__(self) -> None:
        self.__artistas: List["Artista"] = []
        self.__canciones: List["Cancion"] = []
        self.__invitados: List["Invitado"] = []
        self.__locutores: List["Locutor"] = []
        self.__programas: List["Programa"] = []

    @property
    def artistas(self) -> List["Artista"]:
        return self.__artistas
        
    @property
    def canciones(self) -> List["Cancion"]:
        return self.__canciones
        
    @property
    def locutores(self) -> List["Locutor"]:
        return self.__locutores
        
    @property
    def programas(self) -> List["Programa"]:
        return self.__programas
    
    def add_artista(self, artista: "Artista") -> bool:
        self.__artistas.append(artista)
        return True
    
    def add_cancion(self, cancion: "Cancion") -> bool:
        self.__canciones.append(cancion)
        return True
    
    def add_emision(self, emision: "Emision") -> bool:
        return True

    def add_invitado(self, invitado: "Invitado", emision: "Emision") -> bool:
        self.__invitados.append(invitado)
        invitado.add_emision(emision)
        emision.add_invitado(invitado)
        return True

    def add_locutor(self, locutor: "Locutor") -> bool:
        self.__locutores.append(locutor)
        return True

    def add_programa(self, programa: "Programa") -> bool:
        self.__programas.append(programa)
        return True
    
    def get_programa_con_mas_canciones_de_artista(self, artista: "Artista") -> "Programa":
        frecuencia = {}
        for programa in self.__programas:
            frecuencia[programa] = programa.get_frecuencia_canciones(artista)
        return max(frecuencia, key = frecuencia.get)
