from abc import ABC, abstractmethod
from database import Dbase
from interface_insert import tempo2


class Livro(ABC):
    def __init__(self, nom, cat, pag):
        self.nome = nom
        self.categoria = cat
        self.paginas = pag
    @abstractmethod
    def ler_livro(self):
        pass


class Biblioteca(Livro):
    def ler_livro(self):
        print(f"lendo {self.nome} de {self.paginas} paginas da categoria {self.categoria}")

    def adicionar(self, nom, cat, pag):
        a = Dbase('livro')
        a.insert(nom, cat, pag)

    def estante(self):
        a = Dbase('livro')
        a.select()

    def emprestimo(self, cli, pro):
        a = Dbase('emprestimo')
        a.insert(cli, pro, tempo2())

    def devolucao(self):
        a = Dbase('emprestimo')
        a.select()

