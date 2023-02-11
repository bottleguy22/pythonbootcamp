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

