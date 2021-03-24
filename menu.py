import os
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción del Menu")
	print ("\t1 - Inventario")
	print ("\t2 - Compras")
	print ("\t3 - Facturas")
	print ("\t4 - Repuestos")
	print ("\t5 - Orden de Servicio")
	print ("\t6 - Proveedores")
	print ("\t9 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta la Opcion... >> ")
 
	if opcionMenu=="1":
		print ("1")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("2")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("3")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="4":
		print ("4")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="5":
		print ("5")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="6":
		print ("6")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")




