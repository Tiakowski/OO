class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def horas(self, duracao):
        horas = int(self.duracao / 60)
        minutos = int(self.duracao % 60)
        return f'{horas}h{minutos}min'

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano}, -  Duração: {Programa.horas(self,self.duracao)}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas}'


batman = Filme('the batman', 2022, 176)
bastardos = Filme('bastardos inglorios', 2009, 153)
peacemaker = Serie('peacemaker', 2022, 1)

lista = [batman, bastardos, peacemaker]

for programa in lista:
    print(programa)
