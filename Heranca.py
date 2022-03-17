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

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

batman = Filme('the batman', 2022, 176)
print(f'Nome: {batman.nome} - Ano: {batman.ano} - Duração: {int(batman.duracao / 60)}h{int(batman.duracao % 60)}min')
# m = int(digitado - hora * 60)

peacemaker = Serie('peacemaker', 2022, 1)
print(f'Nome: {peacemaker.nome} - Ano: {peacemaker.ano}')