import random

def funcionRandom():
	seleccion = random.choice(["A", "B", "C"])
	print("%s" % seleccion)


def funcion():
	a = input("Ingrese un valor: ")
	if a == "A":
		print("Ingreso: %s" % a)
	else:
		print("Ingreso no valido: %s" % a)


funcionRandom()
funcion()