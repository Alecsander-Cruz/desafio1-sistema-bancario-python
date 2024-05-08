import os
from time import sleep

class Account:
    def __init__(self):
        self.balance = 0.00
        self.daily_withdrawals = 3
        self.maximum_withdrawals_limit = 500.00
        self.deposits = []
        self.withdrawals = []

    def deposit(self, value):

        if value <= 0:
            return 'Não é possível depositar menos do que R$ 0.01'
        
        else:
            self.deposits.append(value)
            self.balance += value
            return f'\nSaldo: R$ {self.balance:10.2f}'
        

    def withdrawal(self, value):
        if(self.daily_withdrawals == 0):
            return '\nNão é possível fazer mais nenhum saque hoje. Limite de saques diários atingido!'
        
        elif value > self.maximum_withdrawals_limit:
            return f'\nValor limite de saque ultrapassado! Por favor, saque uma quantia menor que R$ {self.maximum_withdrawals_limit:10.2f}!'
        
        elif value > self.balance:
            return f'\nSaldo insuficiente! Você só possui R$ {self.balance:10.2f} na conta.'

        elif value <= 0:
            return 'Não é possível sacar um valor menor do que R$ 0.01'
        else:
            self.withdrawals.append(value)
            self.balance -=value
            self.daily_withdrawals -= 1
            return f'\nNovo saldo R$ {self.balance:10.2f}'
        
    def statement_balance(self):
        if len(self.deposits) > 0:
            for i in range(len(self.deposits)):
                print(f'\nDepósito {i+1}: R$ {self.deposits[i]:10.2f}')
            
        if len(self.withdrawals) > 0:
            for i in range(len(self.withdrawals)):
                print(f'\nSaque {i+1}: R$ {self.withdrawals[i]:10.2f}')

        print()
        print(f'\nSaldo: R$ {self.balance:10.2f}')







acc = Account()

os.system('clear')

menu = '''

Sistema do Banco Python>


    [d] DEPOSITAR
    [s] SAQUE
    [e] EXTRATO

    [q] SAIR

===> '''

while True:
    opcao = input(menu)[0].lower()

    if opcao == 'd':
        value = float(input('Insira o valor a ser depositado (exemplo: 15.70): '))
        print(acc.deposit(value))
    
    elif opcao == 's':
        value = float(input('Insira o valor a ser sacado (exemplo: 15.70): '))
        print(acc.withdrawal(value))

    elif opcao == 'e':
        acc.statement_balance()

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')

    sleep(4)
    os.system('clear')