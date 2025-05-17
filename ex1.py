class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

uno = Carro("Fiat", "Uno", 2010)
gol = Carro("Volkswagen", "Gol", 2012)

print(uno.modelo)
print(gol.modelo)