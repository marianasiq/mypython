#começando a trabalhar com as operações de cadeias de strings
sentence= 'hi my name is mariana'
print(len(sentence),(' de comprimento')) #ultilizado para saber o tamanho da frase
print(sentence[14:]) #conseguimos utilizar somente a parte desejada com essa função
print(sentence.count('i'),(' são quantas vezes o "i" se repete')) #da para saber quantas vezes um algorismo ou palavra se repete
#agora uma cadeia maior
poem='saberás que não te amo ' \
'e que te amo posto que de dois modos é a vida,' \
' a palavra é uma asa do silêncio, ' \
'o fogo tem uma metade de frio.' \
' Eu te amo para começar a amar-te,' \
' para recomeçar o infinito e para não deixar de amar-te nunca: ' \
'por isso não te amo ainda.'
print(poem)
print(poem.count('amo'),('vezes "amo" se repete durante o poema'))