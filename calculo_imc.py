
import os
os.system('cls||clear')

def calculo_imc(peso,altura):
    imc = peso/(altura*altura)
    print(f'Olá {nome}, seu IMC está em {imc:.1f}')

def indice(imc):
    if imc <= 18.5:
        print('com Baixo peso')
    elif imc > 18.5 and imc <= 24.9:
        print(f'com Peso ideal' )
    elif imc >=30 and imc <=34.9:
        print(f'com Sobrepeso' )
    else:
        print(f'Obeso' )

    

nome = input('Digite o seu nome: ')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
calculo_imc(peso,altura)

indice()
print(f'você está {indice}')





print(f'Olá {nome} seu IMC é de {imc:.1f}, você está: ')

