import abc


class Autenticavel(abc.ABC):
    """
    Classe abstrata que contém operações de um objeto autenticável.
    As subclasses concretas devem sobrescrever o método autentica
    """

    @abc.abstractmethod
    def autentica(self, senha):
        """
        Método abstrato que faz verificação da senha,
        return True se a senha confere, e False caso contrário.
        """
        pass
