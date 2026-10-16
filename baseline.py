"""A nota de partida: um "agente" que passa toda pergunta para uma pessoa da equipe.

Ele nunca erra feio (não inventa prazo, não mostra pedido alheio), mas também não ajuda ninguém.
Todo agente que vier depois tem que bater esta nota.
"""
import sys
from collections import Counter
from pathlib import Path

from contrato import Caso, Decisao, carregar_referencia


def sempre_passar(pergunta: str) -> Decisao:
    return Decisao.PASSAR

