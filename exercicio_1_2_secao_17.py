'''
Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e altura.
Crie os métodos públicos necessários para sets e gets e também um método para imprimir os dados
de uma pessoa
'''


class Alguem:
    def __init__(self, nome, idade, altura):
        self.__nome__ = nome
        self.__idade__ = idade
        self.__altura__ = altura

    def escolha_nome(self):
        opcoes_nome = {'Carla', 'Alice', 'Pedro', 'Tiago', 'João'}
        pergunta_sexo = input('Informe seu sexo: ').upper()
        if pergunta_sexo in 'M':
            return print(f'Seu nome pode ser {opcoes_nome[2], opcoes_nome[3], opcoes_nome[4]}')
        else:
            return print(f'Seu nome pode ser {opcoes_nome[0], opcoes_nome[1]}')


testando = Alguem('Carla', 15, 1.73)
testando.escolha_nome()
