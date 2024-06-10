import pytest
from utils.utils import read_csv
from calculadora.calculadoraArea import area_do_quadrado, area_do_retangulo, area_do_triangulo

def test_area_do_quadrado():
    num1 = 10
    resultado_esperado = 100

    resultado_obtido = area_do_quadrado(num1)

    assert resultado_esperado == resultado_obtido

def test_area_do_retangulo():
    base = 10
    altura = 5
    resultado_esperado = 50

    resultado_obtido = area_do_retangulo(base,altura)

    assert resultado_esperado == resultado_obtido

def test_area_do_triangulo():
    base = 6
    altura = 6
    resultado_esperado = 18

    resultado_obtido = area_do_triangulo(base,altura)

    assert resultado_esperado == resultado_obtido

@pytest.mark.parametrize('base,altura,resultado_esperado', [
                                                                (8,8,64),
                                                                (20,5,100),
                                                                (3,7,21),
                                                                (6,3.27,19.62)

                                                            ]
                                                            )

def test_area_do_retangulo_lista(base,altura,resultado_esperado):

    #Act / Executa
    resultado_obtido = area_do_retangulo(base,altura)

    #valida
    assert resultado_esperado == resultado_obtido


@pytest.mark.parametrize('base,altura,resultado_esperado', read_csv('./fixtures/massa_area_triangulo.csv'))

def test_area_do_triangulo_csv(base,altura,resultado_esperado):

    resultado_obtido = area_do_triangulo(float(base),float(altura))

    assert float(resultado_esperado) == resultado_obtido


