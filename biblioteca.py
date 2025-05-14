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
        super().__init__(valor*1.5)
    def imprimeValor(self):
        print(f"O valor do VIP é: {self.valor}")

class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self, lado1, lado2):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
    def CalculaAreaR(self):
        self.area = self.lado1*self.lado2
        print(f"A area do retangulo é {self.area}")
    def CalculaPerimetroR(self):
        self.perimetro = self.lado1*2 + self.lado2*2
        print(f"O perimetro do retangulo é: {self.perimetro}")

class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
    def CalculaAreaT(self):
        self.area = (self.base * self.altura)/2
        print(f"A area do triangulo é: {self.area}")
    def CalculaPerimetro(self):
        self.perimetro = self.base*3
        print(f"O perimetro do triangulo é {self.perimetro}")





