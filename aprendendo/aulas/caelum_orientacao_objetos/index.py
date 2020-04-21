from aprendendo.aulas.caelum_orientacao_objetos.cliente import Cliente
from aprendendo.aulas.caelum_orientacao_objetos.conta import Conta
from aprendendo.aulas.caelum_orientacao_objetos.heranca.autenticavel import Autenticavel
from aprendendo.aulas.caelum_orientacao_objetos.heranca.diretor import Diretor
from aprendendo.aulas.caelum_orientacao_objetos.heranca.gerente import Gerente
from aprendendo.aulas.caelum_orientacao_objetos.pessoa import Pessoa

if __name__ == '__main__':
    firstCliente = Cliente('Cabrau', 'De la', '00000000022')
    newCliente = Cliente('Lin', 'Muchacho', '00000000011')

    firstConta = Conta('80', firstCliente, 0)

    newConta = Conta('123', newCliente, 0)
    newConta.deposita(100)
    newConta.deposita(500)
    newConta.saca(80)
    newConta.transferePara(firstConta, 200)
    newConta.extrato()
    newConta.historico.imprime()

    newPessoa = Pessoa('Liiin', 25, 'Rua vou procurar')
    newPessoa.endereco = 'Achei o nome da rua'  # com o uso dos decorator do Python, não precisa criar métodos Get e Set

    newGerente = Gerente("Gerentinho", "00000000033", 6000.40, "1234", 4)
    print(f"Autenticando {newGerente.nome} -> {newGerente.autentica('1234')}")
    print(f"Salario do {newGerente.nome} é de {newGerente.salario:.2f} "
          f"e a sua bonificação é de {newGerente.getBonificacao()}")
    print(f"Vamos escrever o __str__() da classe {newGerente.__class__}: {newGerente}")

    newDiretor = Diretor("Diretorzinho", "00000000044", 15244.40, "abc")
    print(f"Autenticando {newDiretor.nome} -> {newDiretor.autentica('1234')}")
    print(f"Salario do {newDiretor.nome} é de {newDiretor.salario:.2f} "
          f"e a sua bonificação é de {newDiretor.getBonificacao()}")
    print(f"Vamos escrever o __str__() da classe {newDiretor.__class__}: {newDiretor}")

    # no python conseguimos definir que uma classe possui um contrato (interface) ou protocolo
    if isinstance(newGerente, Autenticavel):
        print(
            f"É uma instância de Autenticavel, resultado da autenticação: {newGerente.autentica('vai retornar False')}")
    else:
        print("Gerente não implementa a interface Autenticavel")
