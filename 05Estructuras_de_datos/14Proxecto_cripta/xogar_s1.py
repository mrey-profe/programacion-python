"""Sesión 1 — Menú para probar o inventario.

Completa as opcións que faltan (busca os comentarios TODO).
"""

from inventario import *
from utilidades import pedir_enteiro

CAPACIDADE = 8

inventario = cargar_inventario(CAPACIDADE)
vida = 50
opcion = -1

while opcion != 0:
    print(f"\nVida: {vida}")
    mostrar_inventario(inventario, CAPACIDADE)
    print("1. Coller obxecto  2. Tirar obxecto  3. Equipar  4. Usar poción  0. Saír")
    opcion = pedir_enteiro("Opción: ", 0, 4)
    match opcion:
        case 1:
            obxecto = input("Que colles? ")
            if not engadir_obxecto(inventario, obxecto, CAPACIDADE):
                print("Non che cabe.")
        case 2:
            # TODO: pide un obxecto e tírao. Se non o tes, avisa.
            pass
        case 3:
            # TODO: pide un obxecto e equípao. Mostra "Equipaches: ..."
            # ou avisa se non o tes.
            pass
        case 4:
            # TODO: se non hai pocións, avisa. Se as hai, usa unha e
            # mostra cantas quedan.
            pass
        case 0:
            print("Ata outra!")
