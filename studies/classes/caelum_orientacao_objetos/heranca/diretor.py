from studies.classes.caelum_orientacao_objetos.heranca.autenticavel import Autenticavel
from studies.classes.caelum_orientacao_objetos.heranca.funcionario import Funcionario


class Diretor(Funcionario, Autenticavel):
    __slots__ = ['_nome', '_cpf', '_salario', '_senha']

    # por conta do método ser abstrato, é obrigatório a sua implementação
    def getBonificacao(self):
        return super().getBonificacao()

    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self._senha = senha

    def autentica(self, senha):
        if self._senha == senha:
            return True
        else:
            return False
