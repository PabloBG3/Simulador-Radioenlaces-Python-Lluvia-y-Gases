import math
from Polarizacion_Horizontal import *
from Polarizacion_Vertical import *

def calcula_atenuacion_especifica(polarizacion,frecuencia,intensidad_lluvia):

	#Cálculo de la atenuación específica de lluvia
	if(polarizacion=="h"):
		log10_k=calcula_coef_k_horizontal(frecuencia)
		k=10**log10_k
		alfa=calcula_coef_alfa_horizontal(frecuencia)
	elif(polarizacion=="v"):
		log10_k=calcula_coef_k_vertical(frecuencia)
		k=10**log10_k
		alfa=calcula_coef_alfa_vertical(frecuencia)
	elif(polarizacion=="c" or polarizacion=="l"):
		log10_k_horizontal=calcula_coef_k_horizontal(frecuencia)
		k_horizontal=10**log10_k_horizontal
		alfa_horizontal=calcula_coef_alfa_horizontal(frecuencia)
		log10_k_vertical=calcula_coef_k_vertical(frecuencia)
		k_vertical=10**log10_k_vertical
		alfa_vertical=calcula_coef_alfa_vertical(frecuencia)

		angulo_elevacion_trayecto=float(input("Introduce el ángulo de elevación del trayecto en grados: "))
		#Pasamos el ángulo a radianes
		angulo_elevacion_trayecto=(angulo_elevacion_trayecto*math.pi)/180
		if(polarizacion=="c"):
			angulo_inclinacion=math.pi/4
		elif(polarizacion=="l"):
			angulo_inclinacion=float(input("Introduce el ángulo de inclinación de la polarización con respecto a la horizontal en grados: "))
			#Pasamos el ángulo a radianes
			angulo_inclinacion=(angulo_inclinacion*math.pi)/180
		k=(k_horizontal+k_vertical+(k_horizontal-k_vertical)*math.cos(angulo_elevacion_trayecto)**2*math.cos(2*angulo_inclinacion))/2
		alfa=(k_horizontal*alfa_horizontal+k_vertical*alfa_vertical+(k_horizontal*alfa_horizontal-k_vertical*alfa_vertical)*math.cos(angulo_elevacion_trayecto)**2*math.cos(2*angulo_inclinacion))/(2*k)

	atenuacion_especifica=k*intensidad_lluvia**alfa

	return (atenuacion_especifica,alfa)


def calcula_longitud_efectiva(distancia,intensidad_lluvia,frecuencia,alfa):

	#Cálculo de la longitud efectiva del trayecto
	r=1/(0.477*(distancia**0.633)*(intensidad_lluvia**(0.073*alfa))*(frecuencia**0.123)-10.579*(1-math.exp(-0.024*distancia)))
	if(r>2.5):
		r=2.5
	print("r= ",r)
	longitud_efectiva=distancia*r

	return longitud_efectiva