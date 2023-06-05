from tempinho import tempo, tempo2


class ITlivro:
    def table(self, a, b, c):
        return f"insert into livros(nome, categoria, paginas) values('{a}', '{b}', '{c}');"


class ITemprestimno:
    def table(self, a, b, c=tempo2(), d=tempo()):
        return f"insert into emprestimo(cliente, produto, pegou, devolver) values('{a}', '{b}', '{c}', '{d}');"
