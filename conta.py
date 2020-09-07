class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objecto.... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        self.__saldo += valor

    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.limite
        return valor <= valor_disponivel

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('O valor {} passou o limite'.format(valor))

    def transferencia(self, conta_destino, valor):
        self.sacar(valor)
        conta_destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
