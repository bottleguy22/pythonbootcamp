# 100 DAYS OF CODE : THE COMPLETE PYTHON PRO BOOTCAMP

abaixo temos meu progresso de estudo com 100 dias de python
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
