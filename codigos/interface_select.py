
class ILivro:
    def table(self):
        return "select * from livros;"


class IEmprestimo:
    def table(self):
        return "select * from emprestimo;"


test = ILivro()
print(test.table())
