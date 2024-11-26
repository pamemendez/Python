#---------------------------------------------------------------- Exercicio 1)---------------------------------------------------------------
# 1- 
# numeros = []  

# for i in range(10):
#     num = int(input(f"Digite o {i+1}º número: "))
#     numeros.append(num)

# pares = 0
# for num in numeros:
#     if num % 2 == 0:
#         pares += 1

# print(f"Quantidade de números pares: {pares}")


# 2-
# numeros = [] 

# while True:
#     num = int(input("Digite um número (ou -1 para parar): "))
#     if num == -1:
#         break
#     numeros.append(num)

# maior_menor_100 = None
# for num in numeros:
#     if num < 100:
#         if maior_menor_100 is None or num > maior_menor_100:
#             maior_menor_100 = num

# if maior_menor_100 is not None:
#     print(f"O maior número menor que 100 é: {maior_menor_100}")
# else:
#     print("Nenhum número menor que 100 foi encontrado.")


#---------------------------------------------------------------- Exercicio 2)---------------------------------------------------------------
# 6-
# numeros = input("Digite números separados por espaço: ").split()

# quadrados = []
# for num in numeros:
#     quadrados.append(int(num) ** 2)

# print("Os quadrados são:", quadrados)


#---------------------------------------------------------------- Exercicio 3)---------------------------------------------------------------
# 7-
# num1 = input("Digite o primeiro número: ")
# num2 = input("Digite o segundo número: ")

# soma = int(num1) + int(num2)

# print("A soma é:", soma)

# #8-
# frio = float(input("Limite para frio: "))
# quente = float(input("Limite para quente: "))
# temperatura = float(input("Digite a temperatura em Celsius: "))

# if temperatura < frio:
#     print("Frio")

# elif temperatura > quente:
#     print("Quente")

# else:
#     print("Moderado")


#---------------------------------------------------------------- Exercicio 4)---------------------------------------------------------------
# 10-
# try:
#     import pandas

#     print("Ambiente configurado corretamente!")

# except ImportError:
#     print("Erro ao importar a biblioteca.")


#  #11-
# with open('numeros.txt', 'r') as arquivo:
#     numeros = [int(line.strip()) for line in arquivo]


 #---------------------------------------------------------------- Exercicio 5)---------------------------------------------------------------   
 #12-
# arquivo = open('texto.txt', 'r')
# conteudo = arquivo.read()
# arquivo.close()

# palavras = conteudo.split()
# contador = 0

# for palavra in palavras:
#     if len(palavra) > 5:
#         contador += 1

# print(contador)

#13-
# with open('tabuadas.txt', 'w') as arquivo:

#     for i in range(1, 11):
#         tabuada = [f"{i} x {j} = {i*j}" for j in range(1, 11)]
#         arquivo.write(' | '.join(tabuada) + '\n')

# print("Tabuadas escritas no arquivo 'tabuadas.txt'")

#14-
# import csv

# try:
#     with open('produtos.csv', 'r') as arquivo:
#         leitor = csv.DictReader(arquivo)

#         for linha in leitor:
#             try:
#               preco = linha['Preço'].replace(',', '.').strip() 
#               if float(preco) > 50:
#                     print(linha['Produto'])

#             except ValueError:
#                 print("Erro ao ler o preço.")

# except FileNotFoundError:
#     print("Arquivo 'produtos.csv' não encontrado.")

#15-
# def verifica_primo(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# numeros = input("Digite os números separados por espaço: ").split()
# primos = 0

# for num in numeros:
#     if verifica_primo(int(num)):
#         primos += 1

# print(f"Quantidade de números primos: {primos}")


#---------------------------------------------------------------- Exercicio 6)---------------------------------------------------------------   
#16-
# def verificar_se_eh_primo(numero):
#     if numero < 2:
#         return False
#     for i in range(2, numero):
#         if numero % i == 0:
#             return False
#     return True

# entrada_usuario = input("Digite os números separados por espaço: ").split()
# quantidade_primos = 0

# for numero_str in entrada_usuario:
#     numero = int(numero_str)
#     if verificar_se_eh_primo(numero):
#         quantidade_primos += 1

# print(f"Quantidade de números primos: {quantidade_primos}")

#17-
# senha_correta = "1234"
# tentativas = 0

# while tentativas < 3:
#     senha = input("Digite a senha de 4 dígitos: ")

#     if senha == senha_correta:
#         print("Senha correta! Acesso permitido.")
#         break
#     else:
#         tentativas += 1
#         print(f"Senha incorreta! Você tem {3 - tentativas} tentativa(s) restante(s).")

# if tentativas == 3:
#     print("Você atingiu o número máximo de tentativas. Acesso negado.")

#18-
# a = int(input("Digite o primeiro número: "))
# b = int(input("Digite o segundo número: "))
# c = int(input("Digite o terceiro número: "))

# numeros = [a, b, c]
# numeros.sort()

# if numeros[0] + numeros[1] > numeros[2]:
#     print("Verdadeiro")
# else:
#     print("Falso")

#19-
# alunos = {}

# for i in range(5):
#     nome = input(f"Digite o nome do {i+1}º aluno: ")
#     nota = float(input(f"Digite a nota de {nome}: "))
#     alunos[nome] = nota

# aluno_maior_nota = max(alunos, key=alunos.get)

# print(f"O aluno com a maior nota é {aluno_maior_nota} com a nota {alunos[aluno_maior_nota]}")

#20-
# def calcular_mdc(a, b):
#     menor = min(a, b)
#     for i in range(menor, 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i

# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))

# mdc = calcular_mdc(numero1, numero2)
# print(f"O MDC de {numero1} e {numero2} é {mdc}")

#21-
# n = int(input("Digite o valor de n (termo até o qual calcular a sequência de Fibonacci): "))

# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# ___________________________fim_______________________________________
#Fluxograma e respostas em texto estão no arquivo em word :)
