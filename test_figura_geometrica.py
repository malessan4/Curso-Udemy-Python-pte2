from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
print()

print('Creacion Objeto Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado=5, color='Rojo')
cuadrado1.alto = 20
print(f'Calculo de area del cuadradro: {cuadrado1.calcular_area()}')
print(cuadrado1)

print()

print('Creacion Objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=3, alto=8, color='Negro')
print(rectangulo1)
print(f'Calculo area rectangulo: {rectangulo1.calcular_area()}')

print()