"""
# NOTAS
As notas estão sendo definidas em uma constante `NOTAS`. 
Foi optado por menter somente as notas no formato Natural e o Sustenido (#) para a simplificação do fluxo de trabalho. 
Embora não esteja totalmente correto. Para ver as 12 notas você pode:

```py
>>> from notas import NOTAS
>>> NOTAS
['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
```
"""

NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
