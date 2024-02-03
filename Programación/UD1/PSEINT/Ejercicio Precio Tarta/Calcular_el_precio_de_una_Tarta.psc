Algoritmo Calcular_Precio_de_una_Tarta
	
	Escribir "Escoja entre los tres sabores que le ofrecemos: Manzana, Fresa y Chocolate. Tenga en cuenta que solo tenemos estos sabores. (Escríbalo en minúsculas)"
	Leer sabor
	Segun sabor Hacer
		"manzana":
			tartaSola<-18
			Escribir "La tarta sola de: " sabor " te costará: " tartaSola
		"fresa":
			tartaSola<-16
			Escribir "La tarta sola de: " sabor " te costará: " tartaSola
		"chocolate":
			Escribir "¿Qué tipo de chocolate quieres? ¿Negro o Blanco? (escríbalo en minúsculas)"
			Leer tipo_chocolate
			si tipo_chocolate=blanco Entonces
				tartaSola<-15
				Escribir "La tarta sola de " sabor " te costará: " tartaSola
			SiNo
				tartaSola<-14
				Escribir "La tarta sola de " sabor " te costará: " tartaSola
			FinSi
	FinSegun
	Escribir "¿Deseas nata? Responda con sí o no (Costará 2.5 euros más)"
	Leer nata
	Escribir "¿Deseas que pongamos su nombre? Responda con sí o no (Costará 2.75 euros más)"
	Leer nombre
	Si nata="sí" Entonces
		Si nombre="sí" Entonces
			valortarta<- tartaSola+2.5+2.75
		SiNo
			valortarta<- tartaSola+2.5
		FinSi
	SiNo
		Si nombre="sí" Entonces
			valortarta<- tartaSola+2.75
		SiNo
			valortarta<- tartaSola
		FinSi
	FinSi
	
	Escribir "La tarta le costará " valortarta " euros."
FinAlgoritmo
