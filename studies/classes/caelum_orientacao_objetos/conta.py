from studies.classes.caelum_orientacao_objetos.historico import Historico


class Conta:
    # atributo da classe
    # numero, cliente e saldo por exemplo, são atributos da instância
    _totalContas = 0

    # construtor da classe, o método __init__() é um método reservado
    # do python, utilizado para INICIALIZAR UM OBJETO, o seu primeiro
    # parâmetro, assim como qualquer método de instância, é a própria
    # instância. Por convenção chamamos este argumento de >self<.
    #
    # O método reservado __new__() é chamado antes do __init__() e é
    # esse método que realiza a instância do objeto, por isso no método
    # __init__() o primeiro parâmetro já é o próprio objeto.
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero = str(numero)
        self.cliente = cliente
        self.saldo = float(saldo)
        self.limite = float(limite)
        self.historico = Historico()
        # por ser atributo da classe é possível chama-lo dessa maneira: Conta._totalContas
        # ou é possível chama-lo através da própria classe com o método type(): type(self)._totalContas
        type(self)._totalContas += 1

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("depósito de {}".format(valor))

    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))
            return True

    def extrato(self):
        print(f"Número da conta {self.numero} está com o saldo atual de R$ {self.saldo:.2f}")
        self.historico.transacoes.append(f"tirou extrato - saldo de {self.saldo}")

    def transferePara(self, destino, valor):
        if self.saca(valor):
            destino.deposita(valor)
            self.historico.transacoes.append(f"transferencia de {valor} para conta de número {destino.numero}")
            return True
        else:
            return False

    # define um método estático, sendo assim, não necessário receber o parâmetro "self"
    @staticmethod
    def getTotalContas():
        return Conta._totalContas

    # mas é possível, ao invés de utilizar método estático, utilizado um método da própria classe
    # neste caso, ele recebe um primeiro parâmetro que o Python denomina "cls", que representa a
    # própria classe.
    @classmethod
    def get_total_contas(cls):
        return cls._totalContas
