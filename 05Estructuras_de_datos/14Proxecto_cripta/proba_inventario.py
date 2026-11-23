"""Executa este ficheiro para comprobar as túas funcións de inventario.py."""

import inventario
from inventario import *
from utilidades import proba, executar, resumo, comprobar_sen_globais


def probas_engadir():
    inv = ["espada"]
    proba("engade se hai sitio", engadir_obxecto(inv, "corda", 8), True)
    proba("queda ao final", inv, ["espada", "corda"])
    cheo = ["pedra", "pedra", "pedra"]
    proba("non engade se está cheo (capacidade 3)", engadir_obxecto(cheo, "corda", 3), False)
    proba("o inventario cheo non cambia", cheo, ["pedra", "pedra", "pedra"])
    proba("con capacidade 4 si que cabe", engadir_obxecto(cheo, "corda", 4), True)


def probas_tirar():
    inv = ["poción", "espada", "poción"]
    proba("tira un obxecto que está", tirar_obxecto(inv, "poción"), True)
    proba("só tira o primeiro", inv, ["espada", "poción"])
    proba("non tira o que non está", tirar_obxecto(inv, "chave"), False)
    proba("se non está, non cambia nada", inv, ["espada", "poción"])


def probas_posicion():
    inv = ["espada", "corda", "chave", "corda"]
    proba("posición de chave", posicion(inv, "chave"), 2)
    proba("posición de espada", posicion(inv, "espada"), 0)
    proba("se está repetido, a primeira", posicion(inv, "corda"), 1)
    proba("obxecto que non está", posicion(inv, "facho"), -1)


def probas_posicion_percorrendo():
    inv = ["espada", "corda", "chave", "corda"]
    proba("posición de chave", posicion_percorrendo(inv, "chave"), 2)
    proba("posición de espada", posicion_percorrendo(inv, "espada"), 0)
    proba("se está repetido, a primeira", posicion_percorrendo(inv, "corda"), 1)
    proba("obxecto que non está", posicion_percorrendo(inv, "facho"), -1)
    proba("inventario baleiro", posicion_percorrendo([], "facho"), -1)


def probas_contar_pocions():
    proba("tres pocións", contar_pocions(["poción", "espada", "poción", "poción"]), 3)
    proba("ningunha poción", contar_pocions(["espada"]), 0)
    proba("inventario baleiro", contar_pocions([]), 0)


def probas_contar_pocions_percorrendo():
    proba("tres pocións", contar_pocions_percorrendo(["poción", "espada", "poción", "poción"]), 3)
    proba("ningunha poción", contar_pocions_percorrendo(["espada"]), 0)
    proba("inventario baleiro", contar_pocions_percorrendo([]), 0)


def probas_equipar():
    inv = ["corda", "chave", "espada"]
    proba("equipar espada", equipar(inv, "espada"), True)
    proba("a espada pasa á posición 0", inv, ["espada", "corda", "chave"])
    proba("equipar algo que non está", equipar(inv, "arco"), False)
    proba("se non está, non cambia nada", inv, ["espada", "corda", "chave"])


def probas_usar_pocion():
    inv = ["poción", "espada"]
    proba("cura 20 puntos", usar_pocion(inv, 50), 70)
    proba("gasta a poción", inv, ["espada"])
    proba("sen pocións a vida non cambia", usar_pocion(inv, 50), 50)
    proba("non pasa de 100", usar_pocion(["poción"], 95), 100)


def probas_extra():
    proba("EXTRA obxecto_mais_longo", obxecto_mais_longo(["pa", "lanterna", "corda"]), "lanterna")
    proba("EXTRA obxecto_mais_longo baleiro", obxecto_mais_longo([]), "")
    proba("EXTRA ultimos_collidos", ultimos_collidos(["a", "b", "c", "d"], 2), ["d", "c"])


executar(probas_engadir)
executar(probas_tirar)
executar(probas_posicion)
executar(probas_posicion_percorrendo)
executar(probas_contar_pocions)
executar(probas_contar_pocions_percorrendo)
executar(probas_equipar)
executar(probas_usar_pocion)
executar(probas_extra)
comprobar_sen_globais(inventario)
resumo()
