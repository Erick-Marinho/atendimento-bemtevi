"""O grafo do agente, testado sem chamar modelo nenhum: um modelo falso devolve respostas combinadas."""
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from langchain_core.messages import AIMessage

from agente import montar
from contrato import Decisao


def falso(decisao: Decisao, *textos: str) -> GenericFakeChatModel:
    """Um modelo que primeiro escolhe `decisao` e depois, se pedirem, escreve cada um dos `textos`. Nada além disso."""
    escolha = AIMessage(content="", tool_calls=[{"name": "Escolha", "args": {"decisao": decisao, "motivo": "teste"}, "id": "1"}])
    return GenericFakeChatModel(messages=iter([escolha, *(AIMessage(content=t) for t in textos)]))


def test_o_grafo_tem_um_caminho_para_cada_decisao():
    nos = set(montar(falso(Decisao.PASSAR)).get_graph().nodes)
    assert nos == {"__start__", "decidir", *(d.value for d in Decisao), "__end__"}
