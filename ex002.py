#para fazer a converção de uma string do input para um outro valor, devemos coloca-lo antes do input.
num1=int(input ('write your first number '))
num2=int(input ('write your second number '))
sum=(num1 + num2)
print('your sum is: {} + {} = {}'.format(num1,num2,sum)) #o '.format' é ultilizado para exibir variaveis 

var=input('type something: ') 
print(type(var)) 
print('this is number?', var.isnumeric()) 
print('is this written in capital letters?', var.isupper())

name= input ('qual seu nome? ')
age= input ('qual sua idade? ')
peso = input ('qual seu peso? ')
print (name,age,peso)  
print ('seja bem vindo', name)
print ('idade é {}!'.format(age))