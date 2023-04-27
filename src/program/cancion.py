from __future__ import annotations
from typing import List

#from person.persona import Artista
from utils.enumeration import Genero

class Cancion:

    def __init__(self, nombre: str, artista: "Artista", genero: "Genero") -> None:
        self.__nombre = nombre
        self.__artista = artista
        self.__genero = genero

        self.__artista.add_cancion(self)

    @property
    def artista(self) -> "Artista":
        return self.__artista