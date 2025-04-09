#conhecimentos sobre operadores aritmetricos 
num=int(input('write one number: '))      
numless=(num-1) #a subtração do numero sera igual ao seu antecessor
numplus=(num+1) #a adição do numero sera igual ao seu sucessor
print('your number is: {}, your successor is: {}, and your predecessor is: {}'.format(num,numplus,numless)) 

numdouble=(num*2) 
numtriple=(num*3)
numroot=(num**(1/2)) #um numero elevado a 0,5 ira resultar na sua raiz quadrada
print('this is double {} , the triple {} and square root {:2} of your number'.format(numdouble,numtriple,numroot))

note1=float(input('put your first note: '))
note2=float(input('put your second note: '))
average=((note1+note2)/2) #a media aritmetica das duas notas se da pela divisao da soma das mesmas 
print('Your arithmetic mean is {} '.format(average))

table=int(input('write a number to build your multiplication table: ')) #a tabuada exige o armazenamento da variavel pura para que seu valor seja multiplicado
print('this is your multiplication table:\n{} x 1 = {}'.format(table,(table*1)))  
print('{} x 2 = {}'.format(table,(table*2)))
print('{} x 3 = {}'.format(table,(table*3))) 
print('{} x 4 = {}'.format(table,(table*4)))
print('{} x 5 = {}'.format(table,(table*5)))
print('{} x 6 = {}'.format(table,(table*6)))
print('{} x 7 = {}'.format(table,(table*7)))
print('{} x 8 = {}'.format(table,(table*8)))
print('{} x 9 = {}'.format(table,(table*9)))
print('{} x 10 = {}'.format(table,(table*10))) 

money=float(input('how much money you have available in your wallet? '))
print('this is value in dollars: {}\nand convertec in real is: {}'.format(money,(money*5.8)))

#area 
wide=float(input('how wide is your wall? '))
tall=float(input('how tall is your wall? '))
area= wide*tall
print('this is your area in square meters: {} '.format(area))


