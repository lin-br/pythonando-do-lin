from aprendendo.aulas.caelum_orientacao_objetos.heranca.autenticavel import Autenticavel
from aprendendo.aulas.caelum_orientacao_objetos.heranca.funcionario import Funcionario


class Gerente(Funcionario, Autenticavel):
    __slots__ = ['_nome', '_cpf', '_salario', '_senha', '_qtdGerenciados']

    # é possível redefinir a chamada do método reservado do Python str(), esse método é parecido com
    # o toString() padrão do Java, trás as informações do objeto na memória, porém de uma maneira confusa
    # então podemos altera-lo:
    def __str__(self):
        return f"Gerente [{self.nome}], com o CPF [{self.cpf}]"

    def __init__(self, nome, cpf, salario, senha, qtdGerenciados):
        super().__init__(nome, cpf, salario)
        self._senha = str(senha)
        self._qtdGerenciados = qtdGerenciados

    # aqui ocorre um Override de método, neste caso, do método da classe Funcionario
    def getBonificacao(self):
        return self._salario * 0.15

    def autentica(self, senha):
        if self._senha == senha:
            return True
        else:
            return False
