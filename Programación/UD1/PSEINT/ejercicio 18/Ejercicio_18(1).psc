Algoritmo Ejercicio_18
	escribir "nombre"        //datos: horasextras(hex), horas(h), Tarifa(t), tarifaextra(tex)
	Leer nombre		//horas2(h2), Sueldobase(Sb), Pagoconimpuestos(Pgi), Pagoconimpuestos2(Pgi2)
	escribir "horas trabajadas"			//Sueldoneto(Sn)
	leer h
	hex <- h-35
	escribir "tarifa por hora"
	leer t
	tex <- t*1.5
	h2 <- 35
	Sb <- (h2*t)+(hex*tex)
	Pgi <- Sb-500
	Pgi2 <- Pgi-400
	si Sb<=500 Entonces
		escribir nombre "este es tu Sueldo neto" Sb
	sino si Pgi>=400  entonces
			Sn1 <- 500+((400*0.75)+(Pgi2*0.55))
			escribir nombre " este es tu sueldo neto: " Sn1
			
		sino  Sn2 <- 500+(Pgi*0.75)
			escribir nombre " este es tu sueldo neto: " Sn2 
			finsi
	FinSi
	
FinAlgoritmo
