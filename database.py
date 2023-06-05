import mysql.connector
import interface_insert
import interface_select


class Dbase:
    def __init__(self, tab):
        self._conector = mysql.connector.connect(user='root', host='127.0.0.1', password='', database='biblioteca')
        self.tabela = tab
        self.interface = interface_insert
        self.Interface = interface_select

    def insert(self, n, c, p):
        a = self._conector
        b = a.cursor()
        if self.tabela == 'livro':
            c = self.interface.ITlivro().table(n, c, p)
        elif self.tabela == 'emprestimo':
            c = self.interface.ITemprestimno().table(n, c)
        b.execute(c)
        a.commit()
        b.close()
        a.close()

    def select(self):
        a = self._conector
        b = a.cursor()
        if self.tabela == 'livro':
            c = self.Interface.ILivro().table()
        elif self.tabela == 'emprestimo':
            c = self.Interface.IEmprestimo().table()
        b.execute(c)
        for i in b:
            for co in i:
                print(co)
        b.close()
        a.close()
