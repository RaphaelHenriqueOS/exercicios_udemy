class Retangulo:
    def __init__(self, comprimento=0, largura=0, area=0, perimetro=0):
        self.__comprimento = int(input('Informe o valor do comprimento: '))
        self.__largura = int(input('Informe o valor da largura: '))
        self.__area = int(input('Informe o valor da área: '))
        self.__perimetro = int(input('Informe o valor do perímetro: '))

    def get_calcularArea(self):
        return (self.__comprimento * self.__largura)

    def get_calcularPerimetro(self):
        return ((2 * self.__comprimento) + (2 * self.__largura))

    def get_imprimir(self):
        return print(f'O valor informado do comprimento é {self.__comprimento}, o valor da largura informado foi {self.__largura}, o valor da área é {self.get_calcularArea()} e o valor do perímetro foi {self.get_calcularPerimetro()}')


funcao = Retangulo()
funcao.get_imprimir()
