from __future__ import annotations
from abc import ABC
from typing import List

from program.cancion import Cancion
#from program.programa import Emision, Programa

class Persona(ABC):

    def __init__(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre
    

class Artista(Persona):

    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        self.__canciones: List["Cancion"] = []

    def add_cancion(self, cancion: "Cancion") -> bool:
        self.__canciones.append(cancion)
        return True
    

class Invitado(Persona):

    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        self.__emisiones: List["Emision"] = []

    def add_emision(self, emision: "Emision") -> bool:
        self.__emisiones.append(emision)
        return True
    

class Locutor(Persona):

    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        self.__programas: List["Programa"] = []

    def add_programa(self, programa: "Programa") -> bool:
        self.__programas.append(programa)
        return True