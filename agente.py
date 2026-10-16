"""O primeiro agente: um grafo que lê a mensagem, decide o que o contrato manda e escreve a resposta.

Ainda sem ferramentas: ele não consulta pedido nem abre chamado de verdade. Isso chega no capítulo 3.
"""
from pydantic import BaseModel, Field

from contrato import Decisao

INSTRUCAO = """Você é o atendimento da Casa Bem-te-vi, uma loja online de utilidades para a casa.
Para cada mensagem de cliente, tome uma destas decisões:
- responder: a resposta está nos dados da loja ou na política de atendimento;
- abrir_chamado: um produto chegou com defeito, dentro do prazo;
- recusar: a loja não permite o que o cliente pede;
- passar: o caso é de uma pessoa da equipe.
Quando a política não diz, não prometa: passe a vez."""


class Escolha(BaseModel):
    """A decisão do agente para uma mensagem, e o porquê."""

    decisao: Decisao
    motivo: str = Field(description="por que esta decisão, em uma frase")
