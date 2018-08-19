from random import randint
valor1 = randint(0,10)
valor2 = randint(0,10)
valor3 = randint(0,10)
media = (valor1 + valor2) / 2 #Calculo de média
print ("Primeiro valor:" , valor1)
print ("Segundo valor:" , valor2)
print ("Terceiro valor:" , valor3)
print ("Media do primeiro e segundo valor:" , media)
print ("Maior valor(primeiro, segundo, terceiro):")
maior = max(valor1,valor2,valor3)#Calculo do maior valor.
#Informando quais dos valores é o maior
if valor1 > valor2 and valor1 > valor3:
	print ("Primeiro: %s" % maior)
elif valor2 > valor1 and valor2 > valor3:
	print ("Segundo: %s" % maior)
elif valor3 > valor1 and valor3 > valor2:
	print ("Terceiro: %s" % maior)
elif valor1 == valor2 > valor3:
	print ("Valores repetidos: Primeiro e Segundo: %s" % maior)
elif valor2 == valor3 > valor1:
	print ("Valores repetidos: Segundo e Terceiro: %s" % maior)
elif valor1 == valor3 > valor2:
	print ("Valores repetidos: Primeiro e Terceiro: %s" % maior)
else:
	print ("Todos os valores iguais: %s" % maior)