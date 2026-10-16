"""O contrato do agente: o que ele faz com cada pergunta, escrito antes de existir agente."""
from enum import StrEnum


class Decisao(StrEnum):
    """As quatro saídas possíveis do agente para uma pergunta."""

    RESPONDER = "responder"           # responde com o que está nos dados ou na política
    ABRIR_CHAMADO = "abrir_chamado"   # abre um chamado de troca ou de defeito
    RECUSAR = "recusar"               # diz que não pode, e por quê
    PASSAR = "passar"                 # passa a vez para uma pessoa da equipe


class Fonte(StrEnum):
    """Onde está a informação de que o agente precisa."""

    PEDIDOS = "pedidos"
    POLITICA = "politica"
    CATALOGO = "catalogo"

