# main.py — ponto de entrada
from modelos.ingresso import Inteira, Meia, VIP, Cortesia
from servico.bilheteria import total


if __name__ == "__main__":
    # Cortesia() incluída na lista de venda
    venda = [Inteira(), Meia(), VIP(), Cortesia()]
    
    for i in venda:
        print(f"{i.__class__.__name__}: R${i.preco():.2f}")
        
    print(f"Total: R${total(venda):.2f}") 
