#abaixo temos meu progresso de estudo com 100 dias de python
#DIA 1

print("Hello world!")
print("Hello world\n Hello world!")

print("Hello" + "Jean")
#combinação de string


print("Hello " + " " +"Jean" )
#espaçamento de python, concatenou os espaços

#string unica
"Hello Angela"

#string dupla
"Hello" "Jean"

#erro de identição são espaços antes da linha
 print("Hello world!") #isso aqui vai voltar um indent error

#função input (entrada)
input("Qual seu nome?")
print(input)

print(input("Qual é seu nome?"))
print("Hello " + input("What is your name?"))

print("Hello " + input ("What is your name?") + "!")


#aqui estamos utilizando o calculo do tamanho da frase inserida
#usamos o termo lenght ou a versão resumida(len)     
#alguns exemplos abaixo
print(len("angela"))
print(len("EAUHSEHASEEHEUASEHUH213U12391023819023129"))

#inserindo uma string dentro de um input e printando o número de caracteres dentro do input
name = (input("What is your name?"))
print(len(name))

#clean way to do
print(len(input("What is your name?")))


#variáveis em python
#exemplos
name=input("What is your name?")
print(name)

name = "Jack"
print(name)

NAME = "Angela"
print(NAME)

number = 38
print(number)

#dados armazenadoas na variável name
name = input("What is your name?")
lenght = len(name)
print(lenght)

#resolvendo o desafio
>inverter a com b 

a = input("a: ")
b = input("b: ")
c=a 
a=b  
b=c
print("a: " + a)
print("b: " + b)

#C se tornou A --> portanto não foi preciso criar a variável C
#A se tornou B 
#B se tornou C


#variáveis DEVEM usar nome completo 
user_name=input("What is your age?")
lenght= len(user_name)
print(len)

#SE USAREM NOMES CURTOS, perderá o sentido E VOCÊ SE ESQUECERÁ
#exemplo

n = input("What is your age?")
l = len(n)
print(l)

#resolvendo desafio

print("Welcome to the band name generator.")
city = input("Which city did you grow up in?")
pet = input("What is the name of a pet?")
print("Your band name could be " + city + " " + pet)



#DIA 2


#tipos primitivos de dados
#não conseguimos contar o quantos caracteres pois são inteiros
print(len(12353623))

#aqui estamos mostrando a indexação iniciada por 0, ao avançar 1, muda a letra
print("Hello" [0])
print("Hello" [1])
print("Hello" [2])
print("Hello" [3])
print("Hello" [4])

#tratando numeros como strings
print("123" + "456")

#declarando como numeros INTEIROS
print(12+12)

#PODEMOS USAR underline
print(12_12 + 12_12)

#numeros flutuantes (com virgula)
3.1415... #numero PI constante

#Booleano
True or False #Verdadeiro ou falso

#TYPE ERROR
num_char = len(input("What is your name"))
print(type("Your name has" + num_char + "characters."))

#podemos apenas adicionar type antes e solucionar o problema, o type vai
#nos dizer o tipo e podemos alterar ele antes da sentença ou variavel
#int antes, ou string, boolean, etc
print(str(len(input("What is your name?"))))

#EXEMPLO
A=123
print(type(A))

#também podemos atribuir antes
A=str(123)
print(type(A))

#definimos uma nova variavel de nome num_char
#pegamos o tamanho dela junto com a capacidade de oferecer um input
#defini a variável como string
#recebi o input, a contagem e uma mensagem junto
num_char=len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

#podemos também transformar duas variaveis em sentenças
print(str(1 + 9))

"""#tratando dois numeros string como inteiros
passos da resolução: 
1- printamos que a entrada é tratada como string
2- buscamos e separamos os dígitos entre o indexado (0) e o segundo (1)
3- transformamos os resultados em uma soma
4- transformamos a soma em inteiro
5- saímos o print dos inteiros"""
two_digit_number=input("Type a two digit number")
first_digit_number = two_digit_number[0]
second_digit_number = two_digit_number[1]
result = int(first_digit_number) + int(second_digit_number)
print(result)



#Operadores matemáticos em python
print(7+5)  #SOMA
print(7-5)  #divisão
print(10%2) #módulo mostrando o que sobra 
print(10**2) #potência
print(688/2) #divisão

#PEMDAS - ordem das operações, o que está a esquerda que será priorizado
#()
#**   ->potência
#* /  >multiplicação e divisão
#+ -

print(3 * 3 + 3 / 3) # 3 * 3 + 1 -> AMBAS ESTÃO ACONTECENDO AO MESMO TEMPO 
print(3/3+3*3)


#if, else, e overflow
#overflow é como um buraco na banheira par nao deixar pular água para fora
#condicional if/else
#exemplo de como é usado
#dois pontos são chamados de CÓLON

if condition:
    do this
else:    
    do this

#exemplos

water_level = 50
if water_level > 80:
    print("Drain Water")
else:
    print("Continue")     


#start
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm?"))

if height > 120 :
    print("You can ride the rollercoaster!")
else:
    print("You can't ride the rollercoaster!") 

#e se a pessoa tiver 120 e quer ir na montanha russa? então adicionamos o termo >=
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("You can't ride the rollercoaster, you have to grow taller! ")

#relembrando operadores de comparação
#>
#<
#>=
#<=
#==  IGUAL EXATO
#!=  not equal to
# = estamos apenas atribuindo

#praticando
#nesse caso != vai apenas testar se dois valores são diferentes

print("Welcome to the rollercoaster!")  
height=int(input("What is your height in cm?"))

if height != 120:
    print("You can ride the rollercoaster!")
else: 
    print("You can't ride the rollercoaster!")

#resolvendo o desafio
#se o numero for dividido por 2 e não sobrar nada, então ele é par
#se o numero for dividido e sobrar, ele é impar
#odd number = numero impar
#even number = numero par
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:    
    print("This is an odd number.")

