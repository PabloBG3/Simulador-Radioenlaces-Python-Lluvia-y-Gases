import math
from Funciones_Lluvia import *
from Lee_Excel_DistanciayAltitud import *

print("Simulador de radiocomunicaciones. Cálculo de la atenuación por lluvia.")
print("Se necesitan los siguientes datos para el estudio:")

frecuencia=float(input("Frecuencia en GHz: "))
intensidad_lluvia=float(input("Intensidad de precipitación excedida durante el 0.01% del tiempo en mm/h: "))
polarizacion=input("Tipo de polarización (horizontal:h,vertical:v,circular:c o lineal:l): ")
porcentaje_tiempo=float(input("Indique el porcentaje de tiempo que desea [margen: 0.001% a 1%]: "))

#Llamada a la función que calcula la longitud del trayecto en km
distancia=calcula_distancia()
print("La longitud del trayecto en Km es de: ",distancia,"km")

if(frecuencia<5):
	atenuacion_lluvia=0
	print("La atenuación debido a lluvia es de", atenuacion_lluvia, "dB")

else:
	#Llamada a la función que calcula la atenuación específica
	(atenuacion_especifica,alfa)=calcula_atenuacion_especifica(polarizacion,frecuencia,intensidad_lluvia)
	print("La atenuación específica es de ",atenuacion_especifica,"dB/km")

	#Llamada a la función que calcula la longitud efectiva del trayecto
	longitud_efectiva=calcula_longitud_efectiva(distancia,intensidad_lluvia,frecuencia,alfa)
	print("La longitud efectiva del trayecto es de",longitud_efectiva," km")

	#Cálculo de la atenuación de lluvia excedida durante el 0,01'%' del tiempo
	atenuacion_lluvia=atenuacion_especifica*longitud_efectiva

	#Cálculo de la atenuación de lluvia para el porcentaje de tiempo indicado
	if(porcentaje_tiempo==0.01):
		print("La atenuación por lluvia durante un porcentaje de tiempo del 0.01% es: ",atenuacion_lluvia, " dB")
	else:
		if(frecuencia>=10):
			C0=0.12+0.4*(math.log10(frecuencia/10)**0.8)
		elif(frecuencia<10):
			C0=0.12
		C1=(0.07**C0)*(0.12**(1-C0))
		C2=0.855*C0+0.546*(1-C0)
		C3=0.139*C0+0.043*(1-C0)
		atenuacion_lluvia=atenuacion_lluvia*C1*porcentaje_tiempo**(-(C2+C3*math.log10(porcentaje_tiempo)))
		print("La atenuación de lluvia durante un porcentaje de tiempo del ",porcentaje_tiempo, "% es: ",atenuacion_lluvia, "dB")
		
