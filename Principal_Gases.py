import math
from Funciones_Gases import *
from Datos_Oxigeno import *
from Datos_Vapor import *
from Lee_Excel_DistanciayAltitud import *


print("Simulador de radiocomunicaciones. Cálculo de la atenuación debida a gases.")
print("Se necesitan los siguientes datos para el estudio")
frecuencia=float(input("Frecuencia en GHz: "))

#Llamada a la función que calcula la altura promedia sobre el nivel del mar en metros
altura=calcula_altura()
print("La altura promedia sobre el nivel del mar en metros es de: ",altura,"m")
#Paso de metros a kilómetros
altura=altura*(10**(-3))
#Llamada a la función que calcula la longitud del trayecto en km
distancia=calcula_distancia()
print("La longitud del trayecto en Km es de: ",distancia,"km")

if(frecuencia<10):
	atenuacion_gases=0
	print("La atenuación debida a gases es de", atenuacion_gases, "dB")

else:
	#Llamada a la función que obtiene el valor de los parámetros de temperatura, presión de aire seco y presión parcial de vapor de agua
	#en función de la altura promedia sobre el nivel del mar
	(temperatura,presion,presion_parcial_vapor,respuesta)=calcula_parametros(altura)
	#Una vez obtenidos los parámetros de T, e y p en función de la altura promedia sobre el nivel del mar	
	#Cálculo del sumatorio de la contribución de todas las rayas de oxígeno
	sumatorio_SixFi=calcula_N_oxigeno(presion,temperatura,presion_parcial_vapor,frecuencia)
	print("El sumatorio de la contribución de todas las rayas de oxígeno es: ",sumatorio_SixFi)
	#Cálculo del espectro continuo de aire seco debido a nitrógeno y efecto Debye
	anchura_debye=5.6*(10**(-4))*(presion+presion_parcial_vapor)*(300/temperatura)**0.8
	N_debye=frecuencia*presion*((300/temperatura)**2)*(((6.14*(10**(-5)))/(anchura_debye*(1+(frecuencia/anchura_debye)**2)))+((1.4*(10**(-12))*presion*((300/temperatura)**1.5))/(1+1.9*(10**(-5))*(frecuencia**1.5))))
	print("El espectro continuo de aire seco debido a nitrógeno y efecto Debye es: ",N_debye)
	#Cálculo de la parte imaginaria del valor complejo de la refractividad del oxígeno
	N_oxigeno=sumatorio_SixFi+N_debye
	print("La refractividad del oxígeno es de: ",N_oxigeno)
	#Cálculo del sumatorio de la contribución de todas las rayas de vapor de agua
	N_vapor_agua=calcula_N_vapor(presion,temperatura,presion_parcial_vapor,frecuencia)
	if(respuesta=="s"):
		N_vapor_agua=0
	print("La refractividad del vapor de agua es de: ",N_vapor_agua)
	#Cálculo de la atenuación específica
	atenuacion_especifica=0.1820*frecuencia*(N_oxigeno+N_vapor_agua)
	if(atenuacion_especifica<0):
		atenuacion_especifica=0
	print("La atenuación específica es de: ",atenuacion_especifica,"dB/km")
	#Cálculo de la atenuación por gases total
	atenuacion_gases=atenuacion_especifica*distancia
	print("La atenuación total debida a gases es de: ",atenuacion_gases,"dB")

		
		

