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


def test_ids_unicos_e_em_ordem():
    assert [c.id for c in CASOS] == [f"R{i:02d}" for i in range(1, len(CASOS) + 1)]


def test_as_quatro_decisoes_aparecem():
    assert {c.decisao for c in CASOS} == set(Decisao)


def test_todo_pedido_citado_existe():
    assert all(c.pedido in PEDIDOS for c in CASOS if c.pedido)


def test_linha_invalida_diz_qual_linha(tmp_path):
    arquivo = tmp_path / "ruim.jsonl"
    arquivo.write_text('{"id": "R01", "pergunta": "Oi, tudo bem?", "decisao": "talvez", "motivo": "não existe"}\n', encoding="utf-8")
    with pytest.raises(ValueError, match="linha 1"):
        carregar_referencia(arquivo)
