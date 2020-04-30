import abc


class Funcionario(abc.ABC):
    __slots__ = ['_nome', '_cpf', '_salario']

    # é possível redefinir a chamada do método reservado do Python str(), esse método é parecido com
    # o toString() padrão do Java, trás as informações do objeto na memória, porém de uma maneira confusa
    # então podemos altera-lo:
    def __str__(self):
        return f"< Instância de {self.__class__.__name__}; endereço na memória: {id(self)}>"

    def __init__(self, nome, cpf, salario):
        self._nome = str(nome)
        self._cpf = str(cpf)
        self._salario = float(salario)

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def salario(self):
        return self._salario

    @abc.abstractmethod
    def getBonificacao(self):
        return self._salario * 0.10
