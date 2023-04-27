from __future__ import annotations

from core.radio import RockRollRadio
from person.persona import Artista, Invitado, Locutor
from program.cancion import Cancion
from program.programa import Emision, Programa
from utils.enumeration import Genero

def main() -> None:
    radio = RockRollRadio()

    radio.add_locutor(Locutor('Pedro Rock'))
    radio.add_locutor(Locutor('Pablo Clásico'))
    radio.add_locutor(Locutor('Simona Tropical'))
    radio.add_locutor(Locutor('Carolina Marel'))
    
    radio.add_programa(Programa('Great Rock', radio.locutores[0]))
    radio.add_programa(Programa('Las 40 clásicas', radio.locutores[1]))
    radio.add_programa(Programa('Pa la Tropicalle', radio.locutores[2]))
    radio.add_programa(Programa('De todito', radio.locutores[3]))

    radio.add_artista(Artista('Muse'))
    radio.add_cancion(Cancion('Starlight', radio.artistas[0], Genero.ROCK))
    radio.add_cancion(Cancion('Uprising', radio.artistas[0], Genero.ROCK))

    radio.add_artista(Artista('Ludwig van Beethoven'))
    radio.add_cancion(Cancion('Sonata Clara de Luna', radio.artistas[1], Genero.CLASICA))
    radio.add_cancion(Cancion('Fur Elise', radio.artistas[1], Genero.CLASICA))

    radio.add_artista(Artista('Carlos Vives'))
    radio.add_cancion(Cancion('Fruta fresca', radio.artistas[2], Genero.TROPICAL))
    radio.add_cancion(Cancion('Robarte un beso', radio.artistas[2], Genero.TROPICAL))

    radio.add_emision(Emision(radio.programas[0]))
    radio.add_invitado(Invitado('James Hetfield'), radio.programas[0].get_last_emision())
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[1])

    radio.add_emision(Emision(radio.programas[0]))
    radio.add_invitado(Invitado('Los de Adentro'), radio.programas[0].get_last_emision())
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[1])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[1])

    radio.add_emision(Emision(radio.programas[0]))
    radio.add_invitado(Invitado('Carlos Santana'), radio.programas[0].get_last_emision())
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[1])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[1])

    radio.add_emision(Emision(radio.programas[1]))
    radio.add_invitado(Invitado('Alexis Trejos'), radio.programas[1].get_last_emision())
    radio.programas[1].get_last_emision().add_cancion(radio.canciones[2])
    radio.programas[1].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[1].get_last_emision().add_cancion(radio.canciones[3])

    radio.add_emision(Emision(radio.programas[1]))
    radio.add_invitado(Invitado('Julian Navarro'), radio.programas[1].get_last_emision())
    radio.programas[1].get_last_emision().add_cancion(radio.canciones[2])
    radio.programas[1].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[1].get_last_emision().add_cancion(radio.canciones[3])

    radio.add_emision(Emision(radio.programas[2]))
    radio.add_invitado(Invitado('Checo Acosta'), radio.programas[2].get_last_emision())
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[5])
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[5])

    radio.add_emision(Emision(radio.programas[2]))
    radio.add_invitado(Invitado('Fonseca'), radio.programas[2].get_last_emision())
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[5])
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[5])

    radio.add_emision(Emision(radio.programas[2]))
    radio.add_invitado(Invitado('Bacilos'), radio.programas[2].get_last_emision())
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[5])

    radio.add_emision(Emision(radio.programas[3]))
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[2])

    radio.add_emision(Emision(radio.programas[3]))
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[1])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[2])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[3])

    radio.add_emision(Emision(radio.programas[3]))
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[2])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[5])

    radio.add_emision(Emision(radio.programas[3]))
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[1])
    
    for artista in radio.artistas:
        print(
            f'El programa que más ha puesto canciones del artista {artista.nombre} es',
            f'{radio.get_programa_con_mas_canciones_de_artista(artista).nombre}'
        )


if __name__ == '__main__':
    main()


""" RESULTADOS
El programa que más ha puesto canciones del artista Muse es Great Rock
El programa que más ha puesto canciones del artista Ludwig van Beethoven es De todito
El programa que más ha puesto canciones del artista Carlos Vives es Pa la Tropicalle
"""