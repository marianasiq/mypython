#vamos iniciar a entender e ultilizar mod 
import math #aqui estamos importando algumas operações aritmetricas adicionais 
num=float(input('write a number: '))
print('the broken value is: {} and the whole value is: {} '.format(num, math.trunc(num))) 
#estou importando um mod para ser utilizado na minha variavel 

print('lets calculate the hypotenuse of a right triangle! ')
co=float(input('what value of the opposite leg? '))
ca=float(input('what value of the adjacente leg? '))
hypo=math.hypot(co, ca) #existe uma importação com o valor direto da hipotenusa
print('This is a hypotenuse: {:.2f}'.format(hypo))  

#funções
def ler_celsius():
    celsius = float(input('qual a temperatura?'))
    return celsius
def converção(celsius):
      converção = ((9*celsius+160)/5)
      return converção
def valor_converção(converção):
       print(converção)
celsius = ler_celsius()
converção = converção(celsius)
print(converção) #mostra a converção de c para F 