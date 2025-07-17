price=float(input('how price of your product? '))
discount= price - (price*0.05) #o novo preço sera o antigo menos o desconto de 5%
print('your product witch discount 5 percent is: {}'.format(discount))

salary=float(input('How is your salary? '))
readjustment= salary + (salary*15 / 100)
print('congratulations, you had a 15 percent increase! your new salary is {} ! '.format(readjustment))

lista= []
for _ in range(1, 6):
  num=int(input('write a number :'))
  lista.append(num)
print(lista)  
soma=0
for i in range(len(lista)): 
  soma += lista[i]
print('soma: ', soma)  
alunos={}
for _ in range(1,4):
  nome=str(input('what your name? '))
  notas=float(input('write your note: '))
  alunos[nome]= notas 
print(alunos)
soma=0 
for nota in alunos.values():
  soma+= notas
print(soma/3) 
