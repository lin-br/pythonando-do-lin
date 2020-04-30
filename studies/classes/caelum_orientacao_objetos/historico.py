from datetime import datetime


class Historico:

    def __init__(self):
        self.dataAbertura = datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f"Data abertura: {self.dataAbertura}")
        print("transações: ")
        for transacao in self.transacoes:
            print("-", transacao)
