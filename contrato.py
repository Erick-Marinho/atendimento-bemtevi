"""O contrato do agente: o que ele faz com cada pergunta, escrito antes de existir agente."""
from enum import StrEnum

from pydantic import BaseModel, Field


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


class Caso(BaseModel):
    """Uma pergunta de referência e a decisão que o contrato espera para ela."""

    id: str = Field(pattern=r"^R\d{2}$")
    pergunta: str = Field(min_length=5)
    decisao: Decisao
    motivo: str = Field(min_length=5, description="por que o contrato decide assim, em uma frase")
    precisa: list[Fonte] = []
    pedido: str | None = Field(default=None, pattern=r"^BT-\d{4}$")
    email: str | None = None
