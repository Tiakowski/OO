import CriarConta

class Conta:
    def __init__(self,titular,saldo,limite = 1000):
        print("Classe criada, no endereço {}".format(self))
        self.__id = CriarConta.criar_conta_nova()
        print(self.__id)
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self,valor):
        if valor < self.saldo:
            self.saldo-= valor
        else:
            print("Saldo insuficiente.")

    @property
    def id(self):
        return self.__id

    @property
    def titular(self):
        return self.__titular

