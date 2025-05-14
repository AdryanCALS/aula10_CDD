class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"O {self.nome} foi miando...")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def mugir(self):
        print(f"A {self.nome} {self.cor} ta mugindo muuuu...")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def morrer(self):
        print(f"O {self.nome} {self.cor} infelizmente morreu :(")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f"{self.nome} {self.cor} está latindo")

class Ingresso():
    def __init__(self, valor):
        self.valor = valor
    def imprimeValor(self):
        print(f"O valor do ingresso é: {self.valor}")

class IngressoVip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
    def imprimirVip(self):
        self.valor = self.valor + self.valor*0.5
        print(f"O preço do VIP é: {self.valor}")

