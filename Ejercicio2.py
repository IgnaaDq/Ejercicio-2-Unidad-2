import csv
from clase import ViajeroFrecuente

def _menu(numero,lista):
	print(f"[Numero de viajero]: {numero} \n ---Menu de opciones--- \n \n [Consultar] -> c \n [Acumular] -> a \n [Canjear] -> n \n [Fin] -> f")
	var = input("Ingrese opcion: ")
	i = int(numero) - 1
	while (var != "f"):
		if lista[i].getnum() == numero:
			if var == "c":
				print(f"\n La cantidad de millas del viajero {numero} es de: [{lista[i].getmillas()}]")
				
			elif var == "a":
				x = int(input("\n Ingrese cantidad de millas a acumular: "))
				b = lista[i].acumularMillas(x)
				print(f"\n Las millas acumuladas del viajero numero: {numero} ahora es de: {b}")
			elif var == "n":
				canj = int(input("\n Ingrese la cantidad de millas a canjear: "))
				lista[i].canjearMillas(canj)
			else:
				print("\n Ingreso mal la opcion.")
		else:
			i = i + 1
		print(f"[Numero de viajero]: {numero} \n ---Menu de opciones--- \n \n [Consultar] -> c \n [Acumular] -> a \n [Canjear] -> n \n [Fin] -> f")
		var = input("Ingrese opcion: ")
		
if __name__ == "__main__":
	lista = []
	archivo = open("viajeros.csv")
	datos = csv.reader(archivo,delimiter = ",")

	for fila in datos:
		unviajero = ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3])
		lista.append(unviajero)
	numviaj = input("Ingrese un numero de un viajero frecuente: ")
	_menu(numviaj,lista)
	for i in range (len(lista)):
		print (f"[Numero pasajero]: {lista[i].getnum()} [DNI del viajero]: {lista[i].getdni()} [Nombre del viajero]: {lista[i].getnombre()} [Millas acumuladas del viajero]: {lista[i].getmillas()}")
