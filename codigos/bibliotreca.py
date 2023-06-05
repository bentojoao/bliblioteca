from database import Dbase
from interface_insert import tempo2


class Biblioteca:
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

