# -*- coding: utf-8 -*-
"""Jucélio Brandão Gonçalves Junior.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NEAyc4-IDP2XrOAP7Kv7PldWRYcNxNMd

Exericicio 1
"""

# Primeiro coloco a constante da senha correta e número máximo de tentativas, além da váriavel para contar o número de tentativas
senhaCorreta = '1234'
númeroDeTentativasAtuais = 0
númeroDeTentativasMáximas = 3
while númeroDeTentativasAtuais != númeroDeTentativasMáximas: # Enquanto o usuário não chegar no máximo de tentativas, o programa continuará rodando
    senha = input('Digite sua senha: ') # Coloca a senha
    númeroDeTentativasAtuais += 1 # Incrementa o número de tentativas que o usuario fez
    if senha == senhaCorreta: # Caso a senha esteja correta, uma mensagem é mostrada e o programa para.
      print('Você acertou a senha!') 
      break 
    else:
      print('Você errou a senha! Restam ', númeroDeTentativasMáximas - númeroDeTentativasAtuais, ' tentativas.')
      # Caso não esteja, uma mensagem com o número de tentativas restantes e um aviso são mostrados e o programa continua até a condição do 'while' ser falsa

"""Exercicio 2"""

# Primeiro coloco a constante da senha correta e número máximo de tentativas
senhaCorreta = '1234'
númeroDeTentativasMáximas = 'infinitas'
while númeroDeTentativasMáximas == 'infinitas': # Dessa forma a condição do 'while' sempre será verdadeira
    senha = input('Digite sua senha: ') # Coloca a senha
    if senha == senhaCorreta: # Caso a senha esteja correta, uma mensagem é mostrada e o programa para.
      print('Você acertou a senha!') 
      break 
    else:
      print('Você errou a senha! Restam ', númeroDeTentativasMáximas, ' tentativas.')
      # Caso não esteja, uma mensagem com o número de tentativas restantes e um aviso são mostrados, como existem 'infinitas' tentativas, o programa continua rodando

"""Exercicio 3

"""

# Primeiro coloco a constante da senha correta e número máximo de tentativas
senhaCorreta = '1234'
númeroDeTentativasMáximas = 'infinitas'
númeroDeUsuarios = int(input('Qual o número de usuarios? ')) # Pergunta quantos usuarios irão tentar responder
if númeroDeUsuarios <= 0: # Esse if server apenas para impedir que o usuario coloque números restritos no input
  númeroDeUsuarios = 1
todasSenhas = []
while númeroDeTentativasMáximas == 'infinitas': # Dessa forma a condição do 'while' sempre será verdadeira
    if '0' in todasSenhas or senhaCorreta in todasSenhas: # Caso a senha '0' ou '1234' estejam na lista das senhas o 'while' para e assim todo o programa
      break
    else: # Se não:
      for usuario in range(númeroDeUsuarios): # Aqui Pegamos um usuario de cada vez
        print('Vez de Usuario:', usuario + 1) # Informamos qual o usuario a tentar a senha, o + 1 é para que não exista um usuario 0
        senha = input('Digite sua senha: ') # Coloca a senha
        todasSenhas.append(senha) # A senha inserida é colocada na lista de todas as senhas
        if senha == senhaCorreta: # Caso a senha esteja correta, uma mensagem é mostrada, todas as senhas são mostradas e o programa para.
          print('Usuário ', usuario + 1, ' acertou a senha!')
          print('Essa é a lista de todas senhas digitadas:')
          for senhaDigitada in todasSenhas: # Aqui todas as senhas são mostradas
            print(senhaDigitada)
          break
        elif senha == '0': # Caso digite 0, o 'for' para, mas o 'while' tenta rodar novamente, até que a condição do primeiro 'if' é confirmada e então o programa para.
          print('Encerrando programa.')
          break 
        else:
          print('Usuario ', usuario + 1, ' errou a senha! Restam ', númeroDeTentativasMáximas, ' tentativas.')
          # Caso não esteja, uma mensagem com o número de tentativas restantes e um aviso são mostrados, como existem 'infinitas' tentativas, o programa continua rodando

"""Exercicio 4

"""

import statistics # Biblioteca que facilita o calculo de média utilizando listas
númeroDeElementos = int(input('Escreva o número de elementos positivos que serão digitados: ')) # O usuario digita a quantidade de números a serem digitados
listaDeNúmeros = []
listaDeNúmerosPares = []
for i in range(0, númeroDeElementos): # Aqui ele vai digitar os elementos a serem incluidos na lista até atingir o limite estabelecido no input anterior
  elemento = int(input('Elemento: '))
  listaDeNúmeros.append(elemento)
print('Todos números: ', listaDeNúmeros)
for número in listaDeNúmeros: # Aqui para cada número digitado, é testado se o número é par, caso o número seja, ele é incluido em uma lista separada (poderia ser feito tirando os impares da lista já existente, mas ficaria menos intuitivo)
  if número % 2 == 0:
    listaDeNúmerosPares.append(número)
print('Números pares: ', listaDeNúmerosPares)
média = statistics.mean(listaDeNúmerosPares) # Aqui utilizo da função 'mean()' da biblioteca statistics para calcular a média
print('Média dos números pares: ', média)

"""Exercicio 5

"""

númeroDeUsuarios = int(input('Insira o número de usuários: ')) # É necessário informar a quantidade de usuarios

for usuario in range(númeroDeUsuarios): # A repetição vai se repetir até contemplar o número de usuarios especificado
  print('Vez de usuario ', usuario + 1) # Anuncia o usuario da vez
  peso = int(input('Insira seu peso, em Kilogramas, sendo um número inteiro: ')) # Necessário colocar o peso em kilogramas de forma inteira
  altura = float(input('Insira sua altura, em metros, com duas casas decimais: ')) # Necessário a altura em metros com duas casas decimais

  IMC = round(peso / (altura * altura), 1)

  print('Seu IMC é:', IMC) # Após calcular exibe o IMC
  # Após isso, de acordo com o IMC é mostrado uma mensagem sobre o peso do usuario
  if (IMC < 18.5): 
    print('Você está abaixo do peso ideal')
  elif (IMC > 18.5 and IMC < 24.9):
    print('Parábens --- Você está em seu peso normal!')
  elif(IMC > 24.9 and IMC < 29.9):
    print('Você está acima do seu peso (sobrepeso)')
  elif(IMC > 29.9 and IMC < 34.9):
    print('Obesidade grau I')
  elif(IMC > 34.9 and IMC < 39.9):
    print('Obesidade grau II')
  elif(IMC > 39.9):
    print('Obesidade grau III')