# precos.py — quanto custa alugar cada tipo de veículo.
#
# O preço é uma base fixa mais um valor por hora, que muda conforme o tipo.


def preco_aluguel(tipo, horas):
    if tipo == "bike":
        return 5.0 + 2.0 * horas
    elif tipo == "patinete":
        return 4.0 + 3.0 * horas
    elif tipo == "eletrica":
        return 8.0 + 4.0 * horas
    else:
        raise ValueError("tipo de veículo desconhecido: {!r}".format(tipo))
