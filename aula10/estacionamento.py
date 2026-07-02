class Tarifa:
    def valor(self, horas):
        raise NotImplementedError


class TarifaCarro(Tarifa):
    def valor(self, horas):
        return 5.0 + 3.0 * horas


class TarifaMoto(Tarifa):
    def valor(self, horas):
        return 3.0 + 1.5 * horas


class TarifaCaminhao(Tarifa):
    def valor(self, horas):
        return 10.0 + 5.0 * horas


def criar_tarifa(tipo):
    tabela = {"carro": TarifaCarro, "moto": TarifaMoto, "caminhao": TarifaCaminhao}
    if tipo not in tabela:
        raise ValueError(f"tipo de veículo desconhecido: {tipo!r}")
    return tabela[tipo]()


class Observador:
    def atualizar(self, evento):
        raise NotImplementedError


class Cancela(Observador):
    def atualizar(self, evento):
        print(f"[CANCELA] abrindo para {evento['placa']}")


class Caixa(Observador):
    def atualizar(self, evento):
        print(f"[CAIXA] cobrar R$ {evento['valor']:.2f} de {evento['placa']}")


class Painel(Observador):
    def atualizar(self, evento):
        print(f"[PAINEL] vaga liberada (placa {evento['placa']})")


def _horas_cobradas(hora_entrada, hora_fim):
    horas = hora_fim - hora_entrada
    return 1 if horas <= 0 else horas


class Estacionamento:
    def __init__(self):
        self.obs = [Cancela(), Caixa(), Painel()]
        self.d = {}
        self.n = 0

    def entrar(self, placa, tipo, hora_entrada):
        self.d[placa] = (tipo, hora_entrada)
        self.n = self.n + 1

    def processar_saida(self, placa, hora_saida):
        tipo = self.d[placa][0]
        hora_entrada = self.d[placa][1]
        horas = _horas_cobradas(hora_entrada, hora_saida)
        tarifa = criar_tarifa(tipo)
        valor = tarifa.valor(horas)
        evento = {"placa": placa, "tipo": tipo, "horas": horas, "valor": valor}
        for o in self.obs:
            o.atualizar(evento)
        del self.d[placa]
        self.n = self.n - 1
        return valor

    def previa(self, placa, hora_atual):
        hora_entrada = self.d[placa][1]
        horas = _horas_cobradas(hora_entrada, hora_atual)
        tipo = self.d[placa][0]
        return criar_tarifa(tipo).valor(horas)


if __name__ == "__main__":
    e = Estacionamento()
    e.entrar("ABC1234", "carro", hora_entrada=8)
    print("prévia às 10h:", e.previa("ABC1234", 10))
    print("--- saída às 11h ---")
    total = e.processar_saida("ABC1234", 11)
    print(f"=> cobrado: R$ {total:.2f}  | carros dentro: {e.n}")
