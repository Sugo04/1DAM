Algoritmo Ejercicio_21_modulo_3
	Definir media Como Real
	Escribir "Vaya introduciendo n�meros:"
	i<-0
	suma<-0
	Repetir
		Leer n
		i=i+1//contador
		suma=suma+n
	Hasta Que suma>=10000
	si suma>10000 Entonces
		suma=suma-n
	FinSi
	Escribir "El total de la suma de los n�meros introducidos es: " suma
	Escribir "Se han escrito " i " n�meros"
	media=suma/i
	Escribir "La media del total es: " media
FinAlgoritmo
