# test_locadora.py — a rede de segurança da locadora.
#
# Estes testes PASSAM (rode: pytest). Eles são a rede que deixa você mexer
# no código com segurança: depois de cada mudança, rode pytest e veja verde.
from locadora import Locadora


def test_devolver_no_prazo():
    loc = Locadora()
    loc.alugar("BK1", "bike", 8, 2)
    assert loc.devolver("BK1", 10) == 9.0             # 2h, sem atraso
    assert "BK1" not in loc.ativos

def test_piso_de_uma_hora():
    loc = Locadora()
    loc.alugar("BK2", "patinete", 8, 1)
    assert loc.devolver("BK2", 8) == 7.0              # 0h -> piso 1 -> 4 + 3*1

def test_multa_por_atraso():
    loc = Locadora()
    loc.alugar("BK3", "bike", 8, 2)
    assert loc.devolver("BK3", 12) == 19.0            # usa 4h (13) + atraso 2h (6)


def test_avisos_saem_na_devolucao(capsys):
    loc = Locadora()
    loc.alugar("BK4", "bike", 8, 2)
    loc.devolver("BK4", 10)
    saida = capsys.readouterr().out
    assert "[MANUTENCAO]" in saida
    assert "[PAINEL]" in saida
    assert "[FINANCEIRO]" in saida
