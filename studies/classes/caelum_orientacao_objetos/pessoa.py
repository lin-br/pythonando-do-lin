class Pessoa:
    # é possível utilizar uma variável embutida no Python chamada __slots__ para não deixar as pessoas
    # adicionarem atributos novos para a classe.
    __slots__ = ['__nome', '__idade', '_endereco']

    # com os dois underscores (__) o python muda a visibilidade daquele atributo, igual private no Java
    # com um único underscor (_) o atributo torna-se protegido, para os desenvolvedores Python, isso já é suficiente
    def __init__(self, nome, idade, endereco):
        self.__nome = nome
        self.__idade = idade
        self._endereco = endereco

    # o @property é um decorator no Python, define um método GETTER para um atributo
    @property
    def endereco(self):
        return self._endereco

    # o @[ATRIBUTO].setter é um decorator no Python, define um método SETTER para um atributo
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
