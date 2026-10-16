"""As perguntas de referência estão válidas e de acordo com os dados da loja?"""
from datetime import date

import pytest

from contrato import AQUI, Decisao, carregar, carregar_referencia

CASOS = carregar_referencia()
CASOS_DO_LEITOR = AQUI / "meus-casos.jsonl"
if CASOS_DO_LEITOR.exists():
    CASOS += carregar_referencia(CASOS_DO_LEITOR)
PEDIDOS = {p["id"]: p for p in carregar("pedidos")}
EMAIL = {c["id"]: c["email"] for c in carregar("clientes")}
HOJE = date.fromisoformat(carregar("loja")["hoje"])


def dono(pedido):
    return EMAIL[PEDIDOS[pedido]["cliente"]]

