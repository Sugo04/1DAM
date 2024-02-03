Algoritmo Ejercicio_18
	Escribir 'Escribe tu nombre'
	Leer nombre
	Escribir 'Escribe el número de horas que has trabajado'
	Leer horas
	horasextra <- (horas-35) //ya me ha vuelto a dar problemas xD
	Si horasextra<35 Entonces
		horasextra<-0 
		Escribir "No tienes horas extras"
	SiNo
		Escribir 'Tus horas extra son: ', horasextra
	Fin Si
	horas2 <- (horas-horasextra)
	Escribir 'Escribe la tarifa que cobras por hora: '
	Leer tarifa
	tarifaextra <- tarifa*1.5
	Si horasextra==0 Entonces
		Escribir "Esto es lo que cobrarias por hora extra: " tarifaextra
	SiNo
		Escribir 'Esto es lo que cobras por hora extra: ', tarifaextra
	Fin Si
	salariobruto <- (horas2*tarifa)+(horasextra*tarifaextra)
	Escribir 'Este es tu salario bruto: " salariobruto
	pagoconimp <- (salariobruto-500)
	pagoconimp2 <- (pagoconimp-400)
	Si salariobruto<=500 Entonces
		Escribir nombre, ' tu salario es: ', salariobruto
	SiNo
		Si pagoconimp>=400 Entonces
			Escribir nombre, ' tu salario neto es: ', 500+((400*(75/100))+(pagoconimp2*(55/100)))
		SiNo
			Escribir nombre, ' tu salario neto es: ', 500+(pagoconimp*0.75)
		FinSi
	FinSi
FinAlgoritmo
