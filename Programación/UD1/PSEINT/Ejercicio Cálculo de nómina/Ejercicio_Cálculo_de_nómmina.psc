Algoritmo EJERCICIO_CALCULO_DE_NOMINA
	Escribir 'Elija el díjito de su cargo: '
	Escribir '1-P.Junior'
	Escribir '2-P.Senior'
	Escribir '3-J.Proyecto'
	Leer cargo
	Según cargo Hacer
		1:
			base <- 950
		2:
			base <- 1200
		De Otro Modo:
			base <- 1600
	FinSegún
	Escribir 'Elija el dígito correspondiente a su estado civil: '
	Escribir '1-Soltero'
	Escribir '2-Casado'
	Leer estadoc
	Escribir 'Indique el número de días que ha estado de viaje: '
	Leer DIAS
	pex <- (DIAS*30)
	bruto <- (base+pex)
	Si estadoc=1 Entonces
		neto <- (bruto*0.75)
		Escribir 'Al estar soltero se le aplicará una reducción del 25% a su salario por el IRPF'
	SiNo
		neto <- (bruto*0.20)
		Escribir 'Al estar casado se le aplicará una reducción del 20% a su salario por el IRPF'
	FinSi
	Escribir 'Su Sueldo neto es: ', neto
FinAlgoritmo
