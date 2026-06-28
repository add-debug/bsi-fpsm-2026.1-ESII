from repositorio.assinantes import RepositorioAssinantes
from servico.newsletter import ServicoNewsletter

class FakeEmail:
    def __init__(self):
        self.enviados = []

    def enviar(self, para, texto):
        self.enviados.append(para)

if __name__ == "__main__":
    repo = RepositorioAssinantes()
    enviador = FakeEmail()
    
    servico = ServicoNewsletter(repo, enviador) 
    servico.enviar_edicao("Edicao teste")
    
    print("Quem receberia:", enviador.enviados)
