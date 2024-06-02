import pytest

from calculadora.calculadora import somar_dois_numeros,subtrair_dois_numeros,multiplicar_dois_numeros,dividir_dois_numeros


def test_somar_dois_numeros():

    # Padrão/ Standard AAA (se diz Triple A/3A) = Arrange, Act, Assert

    # Arrange / Prepara / Configura
    #Dados de entrada e saída
    num1 = 5 
    num2 = 7
    resultado_esperado = 12


    #Act / Executa
    resultado_obtido = somar_dois_numeros(num1,num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

def test_subtrair_dois_numeros():

# Arrange / Prepara / Configura
    #Dados de entrada e saída
    num1 = 15
    num2 = 8
    resultado_esperado = 7


    #Act / Executa
    resultado_obtido = subtrair_dois_numeros(num1,num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

def test_multiplicar_dois_numeros():

    num1 = 10
    num2 = 10
    resultado_esperado = 100

    resultado_obtido = multiplicar_dois_numeros(num1,num2)

    assert resultado_esperado == resultado_obtido

def test_dividir_dois_numeros():

    num1 = 120
    num2 = 6
    resultado_esperado = 20

    resultado_obtido = dividir_dois_numeros(num1,num2)

    assert resultado_esperado == resultado_obtido

def test_dividir_por_zero():
    num1 = 320
    num2 = 0

    resultado_obtido = dividir_dois_numeros(num1,num2)

    assert resultado_obtido

    