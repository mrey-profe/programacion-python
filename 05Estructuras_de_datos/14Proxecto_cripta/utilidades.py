"""Funcións de apoio para o proxecto. NON fai falta modificar este ficheiro."""

import types


def pedir_enteiro(mensaxe, minimo, maximo):
    """Pide un enteiro entre minimo e maximo (incluídos) ata que sexa válido."""
    valido = False
    while not valido:
        try:
            numero = int(input(mensaxe))
            if minimo <= numero <= maximo:
                valido = True
            else:
                print(f"Escribe un número entre {minimo} e {maximo}.")
        except ValueError:
            print("Iso non é un número.")
    return numero


# ---------------------------------------------------------------------------
# Ferramentas para os ficheiros de probas (proba_*.py)
# ---------------------------------------------------------------------------

_resultados = [0, 0]  # [correctas, fallidas]


def proba(descricion, obtido, esperado):
    """Compara o resultado obtido co esperado e mostra OK ou FALLO."""
    if obtido == esperado:
        _resultados[0] += 1
        print(f"  OK     {descricion}")
    else:
        _resultados[1] += 1
        print(f"  FALLO  {descricion}")
        print(f"           esperado: {esperado!r}")
        print(f"           obtido:   {obtido!r}")


def executar(funcion_probas):
    """Executa un grupo de probas. Se o teu código dá un erro, móstrao e continúa."""
    print(f"\n{funcion_probas.__name__}")
    try:
        funcion_probas()
    except Exception as erro:
        _resultados[1] += 1
        print(f"  ERRO   {type(erro).__name__}: {erro}")


def _nomes_usados(codigo):
    """Nomes globais que usa un bloque de código (e as funcións de dentro)."""
    nomes = list(codigo.co_names)
    for constante in codigo.co_consts:
        if isinstance(constante, types.CodeType):
            nomes += _nomes_usados(constante)
    return nomes


def comprobar_sen_globais(modulo):
    """Avisa se algunha función do módulo le variables globais do ficheiro.

    As funcións só deben traballar cos seus parámetros.
    """
    print(f"\nvariables globais en {modulo.__name__}.py")
    globais = vars(modulo)
    atopadas = 0
    for nome, valor in globais.items():
        if isinstance(valor, types.FunctionType) and valor.__module__ == modulo.__name__:
            for usado in _nomes_usados(valor.__code__):
                if usado in globais and not callable(globais[usado]) \
                        and not isinstance(globais[usado], types.ModuleType):
                    atopadas += 1
                    print(f"  FALLO  {nome} usa a variable global {usado}: pásaa como parámetro")
    if atopadas == 0:
        _resultados[0] += 1
        print("  OK     ningunha función usa variables globais")
    else:
        _resultados[1] += atopadas


def resumo():
    correctas, fallidas = _resultados
    print(f"\n{correctas} probas correctas, {fallidas} con fallos.")
    if fallidas == 0:
        print("Todo correcto!")
