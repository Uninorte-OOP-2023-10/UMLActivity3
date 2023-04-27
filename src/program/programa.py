from __future__ import annotations
from typing import List

#from person.persona import Invitado, Locutor
from program.cancion import Cancion

class Programa:

    __ID = 1

    def __init__(self, nombre: str, locutor: "Locutor") -> None:
        self.__nombre = nombre
        self.__serial = Programa.__ID
        self.__emisiones: List["Emision"] = []
        self.__locutores: List["Locutor"] = [locutor]

        self.__locutores[0].add_programa(self)

        Programa.__ID += 1

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    def add_emision(self, emision: "Emision") -> bool:
        self.__emisiones.append(emision)
        return True
    
    def get_last_emision(self) -> "Emision":
        return self.__emisiones[-1]
    
    def get_frecuencia_canciones(self, artista: "Artista") -> int:
        frecuencia = 0
        for emision in self.__emisiones:
            frecuencia += emision.get_cantidad_canciones(artista)
        return frecuencia

class Emision:

    __ID = 1

    def __init__(self, programa: "Programa") -> None:
        self.__serial = Emision.__ID
        self.__canciones: List["Cancion"] = []
        self.__invitados: List["Invitado"] = []
        self.__programa = programa

        self.__programa.add_emision(self)

        Emision.__ID += 1

    def add_cancion(self, cancion: "Cancion") -> bool:
        self.__canciones.append(cancion)
        return True
    
    def add_invitado(self, invitado: "Invitado") -> bool:
        self.__invitados.append(invitado)
        return True
    
    def get_cantidad_canciones(self, artista: "Artista") -> int:
        canciones = [cancion for cancion in self.__canciones if cancion.artista == artista]
        return len(canciones)