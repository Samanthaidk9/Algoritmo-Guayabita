# Algoritmo-Guayabita
parcial # 1 analisis de algoritmos
Algoritmo guayabita
	repetir
		Escribir "Digite la cantidad de jugadores"
		Leer jugadores
		mientras jugadores<2 o jugadores>6
			Escribir "No se puede jugar con " jugadores " jugadores"
			Escribir "Por favor digite nuevamente la cantidad de jugadores"
			leer jugadores
		fin mientras
		plante=10000
		Dimension usuario[jugadores]
		Para i<-1 Hasta jugadores con Paso i+1 Hacer
			Escribir "Digite el nombre de cada jugador"
			Leer usuario[i];
		Fin Para
		Escribir "Por favor cada jugador colocar el plante"
		Escribir "El acumulado es de " plante
		Repetir
			Para i<-1 Hasta jugadores Con Paso 1 Hacer
				Si plante>0 Entonces
					Escribir "Es el turno de " usuario[i]
					Escribir "Por favor presiones una tecla para sacar un numero al azar";
					leer x
					lanzar1=azar(6)+1
					Si lanzar1=1 o lanzar1=6 Entonces
						Escribir "Su numero es " lanzar1
						Escribir "Usted perdio. Por favor coloque el plante"
						plante=plante+1
						Escribir "El acumulado es " plante
					Sino
						Escribir "Su puntaje es " lanzar1
						Escribir "De cuanto harta la apuesta"
						leer apuesta
						Mientras apuesta<0 o apuesta>plante Hacer
							Escribir "No se puede hacer esta apuesta"
							Escribir "Escribir nuevamente el valor de la apuesta"
							Leer apuesta
						Fin Mientras
						Escribir "Por favor presiones una tecla para sacar un numero al azar";
						leer x
						lanzar=azar(6)+1
						Si lanzar1+1>lanzar Entonces
							Escribir "Su puntaje es " lanzar
							Escribir "Perdio!!!"
							Escribir "Por favor coloque ", apuesta," su apuesta sobre la mesa"
							plante=plante+apuesta
							Escribir "El plante es " plante
						Sino
							Escribir "Su puntaje es " lanzar
							Escribir "Gano!!!"
							Escribir "Por favor retire su " apuesta " plata de la mesa"
							plante=plante-plante
							Escribir "El plante es " plante
						Fin Si
					Fin Si
				sino
					Si plante <=0 Entonces
						Escribir "Se termina el juego"
					Fin Si
				Fin Si
			FinPara
		Hasta Que plante <=0
	Hasta Que exit=1;
FinAlgoritmo
