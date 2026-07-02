# cobranca.py — serviço externo de cobrança (a "maquininha" da locadora).
#
# Em produção, cobrar() fala com o gateway de pagamento DE VERDADE (custa
# dinheiro e depende da internet).


class ServicoCobranca:
    def cobrar(self, codigo, valor):
        # Aqui, na produção, entra a chamada real ao gateway de pagamento.
        print("[GATEWAY] cobrando R$ {:.2f} do aluguel {}".format(valor, codigo))
