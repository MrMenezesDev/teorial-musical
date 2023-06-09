from teoria_musical.constantes import NOTAS
from teoria_musical.error import EscalaError, NotaError

ESCALAS = {
    'maior': (0, 2, 4, 5, 7, 9, 11),
    'menor': (0, 2, 3, 5, 7, 8, 10),
    'Acoustic scale or Lydian dominant scale': (0, 2, 4, 6, 7, 9, 10),
    'Aeolian mode or natural minor scale': (0, 2, 3, 5, 7, 8, 10),
    'Algerian scale': (0, 2, 3, 6, 7, 9, 11, 12, 14, 15, 17),
    'Altered scale or Super Locrian scale': (0, 1, 3, 4, 6, 8, 10),
    'Augmented scale': (0, 3, 4, 7, 8, 11),
    'Bebop dominant scale': (0, 2, 4, 5, 7, 9, 10, 11),
    'Blues scale': (0, 3, 5, 6, 7, 10),
    'Chromatic scale': (
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    ),
    'Dorian mode': (0, 2, 3, 5, 7, 9, 10),
    'Double harmonic scale': (0, 1, 4, 5, 7, 8, 11),
    'Enigmatic scale': (0, 1, 4, 6, 8, 10, 11),
    'Flamenco mode': (0, 1, 4, 5, 7, 8, 11),
    'Gypsy scale': (0, 2, 3, 6, 7, 8, 10),
    'Half diminished scale': (0, 2, 3, 5, 6, 8, 10),
    'major scale': (0, 2, 4, 5, 7, 8, 11),
    'minor scale': (0, 2, 3, 5, 7, 8, 11),
    'Yo scale': (0, 3, 5, 7, 10),
    'Harmonic Scale': (144,),
    'Ionian mode or major scale': (0, 2, 4, 5, 7, 9, 11),
    'Locrian mode': (0, 1, 3, 5, 6, 8, 10),
    'Lydian augmented scale': (0, 2, 4, 6, 8, 9, 11),
    'Lydian mode': (0, 2, 4, 6, 7, 9, 11),
    'Major Locrian scale': (0, 2, 4, 5, 6, 8, 10),
    'Major pentatonic scale': (0, 2, 4, 7, 9),
    'Melodic minor scale': (0, 2, 3, 5, 7, 9, 11),
    'Minor pentatonic scale': (0, 3, 5, 7, 10),
    'Mixolydian mode or Adonai malakh mode': (0, 2, 4, 5, 7, 9, 10),
    'Neapolitan major scale': (0, 1, 3, 5, 7, 9, 11),
    'Neapolitan minor scale': (0, 1, 3, 5, 7, 8, 11),
    'Octatonic scale': (0, 1, 3, 4, 6, 7, 9, 10),
    'Pentatonic scale': (0, 2, 4, 7, 9),
    'Persian scale': (0, 1, 4, 5, 6, 8, 11),
    'Phrygian dominant scale': (0, 1, 4, 5, 7, 8, 10),
    'Phrygian mode': (0, 1, 3, 5, 7, 8, 10),
    'Prometheus scale': (0, 2, 4, 6, 9, 10),
    'Tritone scale': (0, 1, 4, 6, 7, (10)),
    'Ukrainian Dorian scale': (0, 2, 3, 6, 7, 9, 10),
    'Whole tone scale': (0, 2, 4, 6, 8, 10),
}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade.
    Args:
        tônica: Nota que será a tônica da escala
        tonalidade: Tonalidade da escala
    Returns:
        Um dicionário com as notas da escala e os graus.
    Raises:
        NotaError: Caso a tônica não seja uma nota valida.
        EscalaError: Caso a escala não exista ou não tenha sido implementada.
    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
        >>> escala('a', 'menor')
        {'notas': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()
    try:
        intervalos = ESCALAS[tonalidade]
        tonica_pos = NOTAS.index(tonica)
    except ValueError:
        raise NotaError()
    except KeyError:
        raise EscalaError()

    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
