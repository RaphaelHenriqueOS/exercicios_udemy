#resolução dos exercícios 3 e 4 da seção 17

class Quadrado:
    def __init__(self, lado=0, area=0, perimetro=0):
        self.__lado = lado
        self.__area = area
        self.__perimetro = perimetro

    def get_instanciar(self):
        self.__lado = int(input('Informe o valor do lado: '))
        self.__area = int(input('Informe a área ou digite zero: '))
        self.__perimetro = int(input('Informe o valor do perímetro ou zero: '))

    def get_calcularArea(self):
        calculoArea = self.__lado * self.__lado
        self.__area = calculoArea
        return calculoArea

    def get_calcularPerimetro(self):
        calculoPerimetro = self.__lado * 4
        self.__perimetro = calculoPerimetro
        return calculoPerimetro

    def get_imprimir(self):
        return print(f'O valor do lado do quadrado informado é {self.__lado}. Com isso, o valor da área do quadrado é {self.get_calcularArea()} e o valor do Perímetro desse quadrado é {self.get_calcularPerimetro()}')


funcao = Quadrado()
funcao.get_instanciar()
funcao.get_imprimir()
