# locadora.py — sistema da locadora de veículos (bikes, patinetes...).
#
# Um veículo é alugado (alugar) e depois devolvido (devolver). Na devolução,
# cobra-se o aluguel + a multa de atraso, e os interessados são avisados.

from precos import preco_aluguel
from cobranca import ServicoCobranca


class Locadora:
    def __init__(self):
        self.ativos = {}
        self.c = ServicoCobranca()

    def alugar(self, cod, tipo, ini, prev):
        self.ativos[cod] = (tipo, ini, prev)

    def devolver(self, cod, fim):
        t = self.ativos[cod][0]
        ini = self.ativos[cod][1]
        prev = self.ativos[cod][2]
        h = fim - ini
        if h < 1:
            h = 1
        p = preco_aluguel(t, h)
        a = fim - (ini + prev)
        if a <= 0:
            m = 0.0
        else:
            m = 3.0 * a
        total = p + m
        self.c.cobrar(cod, total)
        print("[MANUTENCAO] revisar {} {}".format(t, cod))
        print("[PAINEL] {} disponível de novo".format(cod))
        print("[FINANCEIRO] recebido R$ {:.2f} de {}".format(total, cod))
        del self.ativos[cod]
        return total

    def simular(self, cod, fim):
        t = self.ativos[cod][0]
        ini = self.ativos[cod][1]
        prev = self.ativos[cod][2]
        h = fim - ini
        if h < 1:
            h = 1
        p = preco_aluguel(t, h)
        a = fim - (ini + prev)
        if a <= 0:
            m = 0.0
        else:
            m = 3.0 * a
        return p + m
