from datetime import datetime
import pytz
from random import randint

class ContaCorrente:    

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []
    def consultar_saldo(self): #Método consultar saldo
        print(f"Seu saldo atual é de R$: {(self._saldo):,.2f}")
        
    def depositar(self, valor):
        self._saldo += valor
        self.consultar_saldo()
        self._transacoes.append((valor, f'Saldo R$ {(self._saldo):,.2f} às {ContaCorrente._data_hora()}'))
        
    def _limite_conta(self): # _nome_método significa método privado!
        self._limite = 500
        return self._limite
    
    def sacar_dinheiro(self, valor): 
        if self._saldo - valor < self._limite_conta():
            print("Você não tem saldo suficiente para sacar esse valor")
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((- valor, f'Saldo {self._saldo} às {ContaCorrente._data_hora()}'))
            
    def consultar_limite_cheque_especial(self):
        print(f"Seu limite de cheque especial é de R$ {(self._limite_conta()):,.2f} Reais.")
        
    def consultar_historico_transacoes(self):
        print("Historico de transações:")
        for transacao in self._transacoes:
            print("Valor, Saldo, Data e Hora")
            print(transacao)
    
    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((- valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))
class CartaoCredito:
    
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f"{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}"
        self.cod_seguranca = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}"
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)
    
    #Criação do método GET pegar a senha privada
    @property
    def senha(self):
        return self._senha
    #Criação do SET, verificação se o valor é INT e possui 4 itens
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha inválida")