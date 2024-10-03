# Calculadora de IMC

import os
import time

while True:
    print('CALCULADORA DE IMC')

    nome = input('Digite seu nome: ') # Entrada de Dados para receber o nome do usuário

    if len(nome) < 2:
        print('Nome inválido')
        time.sleep(2) # Realiza uma pausa de 2seg
        os.system('cls') # Limpa a tela
        continue

    pesoInput = input('Digite seu peso (KG): ') # Entrada de Dados para receber o peso do usuário
    alturaInput = input('Digite sua altura (m): ') # Entrada de Dados para receber a altura do usuário

    numeros_validos = None # Variavel que vai verificar se foi digitado número no input

    try:
        peso = float(pesoInput) # Realiza a conversão do peso que está em string para float
        altura = float(alturaInput) # Realiza a conversão da altura que está em string para float
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Número digitado inválido!')
        time.sleep(2) # Realiza uma pausa de 2seg
        os.system('cls') # Limpa a tela
        continue # Voltará para o início do código

    imc = peso / (altura ** 2) # Fórmula do IMC = peso / (altura x altura) - Realiza o cálculo do IMC

    # Define a classificação de acordo com o valor do IMC
    if imc < 18.5:
        classificacao = 'Magreza'
    elif imc >= 18.5 and imc < 25.0:
        classificacao = 'Normal'
    elif imc >= 25.0 and imc < 30.0:
        classificacao = 'Sobrepeso'
    elif imc >= 30.0 and imc < 40.0:
        classificacao = 'Obesidade'
    else:
        classificacao = 'Obesidade Grave'

    # Mostra todos os dados e deixa dentro de uma string
    linha1 = f'Nome = {nome} \nPeso = {peso:.2f} kg\nAltura = {altura:.2f} m\nIMC = {imc:.2f}\nClassificação = {classificacao}'

    os.system('cls') # Limpa a tela
    print(linha1) # Apresenta todos os dados na tela
    time.sleep(5) # Realiza uma pausa de 5seg

    sair = input('Deseja fazer novamente? [s] sim - [n] não\n')
    sair = sair.lower() # Vai tornar a String em minuscula
    sair = sair.startswith('n') # Vai verificar se a str 'sair' começa com 'n'
    os.system('cls') # Limpa a tela

    if sair is True:
        break