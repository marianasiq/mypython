price=float(input('how price of your product? '))
discount= price - (price*0.05) #o novo preço sera o antigo menos o desconto de 5%
print('your product witch discount 5 percent is: {}'.format(discount))

salary=float(input('How is your salary? '))
readjustment= salary + (salary*15 / 100)
print('congratulations, you had a 15 percent increase! your new salary is {} ! '.format(readjustment))
