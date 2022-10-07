from math import pi


class Circulo:
    from math import pi as pi

    def __init__(self, raio=0, area=0, perimetro=0):
        self.__raio = int(input('Informe o raio do cículo: '))
        self.__area = int(input('Informe a área do cículo: '))
        self.__perimetro = int(input('Informe o perímetro do cículo: '))

    def get_calcularArea(self):
        return (pi * self.__raio * self.__raio)

    def get_calcularPerimetro(self):
        return (2 * pi * self.__raio)

    def get_imprimir(self):
        return print(f'Os valores informados de raio foi {self.__raio}, o valor calculado de áerea foi {self.get_calcularArea():.4f} e o vlaor do perímetro calculado foi {self.get_calcularPerimetro():.4f}')


funcao = Circulo()
funcao.get_imprimir()
