from random import randint
valor1 = randint(0,100)
valor2 = randint(0,100)
valor3 = randint(0,100)
media = valor1 + valor2 / 2 #Calculo de média
print ("Primeiro valor:" , valor1)
print ("Segundo valor:" , valor2)
print ("Terceiro valor:" , valor3)
print ("Media do primeiro e segundo valor:" , media)
print ("Calculo de maior valor(primeiro, segundo, terceiro):")
#Calculo de maior valor
if valor1 > valor2 and valor1 > valor3:
	print ("Maior valor: Primeiro ->", valor1)
elif valor2 > valor1 and valor2 > valor3:
	print ("Maior valor: Segundo ->", valor2)
elif valor3 > valor1 and valor3 > valor2:
	print ("Maior valor: Terceiro ->", valor3)
else:
	print ("Existem valores repetidos como maior valor.")