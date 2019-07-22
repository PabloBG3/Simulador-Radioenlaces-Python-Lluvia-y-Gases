import math
from Lee_Excel_Latitud import *



def calcula_parametros(altura):
	#Obtención de T, e y p en función de la altura promedia sobre el nivel del mar
	#En caso de tener información sobre latitud uso la atmósfera de referencia sobre latitudes bajas, medias o altas
	#En caso de no tener información sobre latitud uso la atmósfera de referencia mundial anual media
	respuesta=input("¿Tengo información sobre latitud? (sí:s,no:n): ")
	if(respuesta=="s"):
		#Llamada a la función que calcula la latitud en grados
		latitud=calcula_latitud()
		print("La latitud es de ",latitud,"grados")
		#Caso de latitudes bajas
		if(latitud<22):
			#Calculo la temperatura
			if(0<=altura<17):
				temperatura=300.4222-6.3533*altura+0.005886*altura**2
			elif(17<=altura<47):
				temperatura=194+(altura-17)*2.533
			elif(47<=altura<52):
				temperatura=270
			elif(52<=altura<80):
				temperatura=270-(altura-52)*3.0714
			elif(80<=altura<=100):
				temperatura=184
			print("La temperatura es de: ",temperatura,"K")
			#Calculo la presión de aire seco
			if(0<=altura<=10):
				presion=1012.0306-109.0338*altura+3.6316*altura**2
			elif(10<altura<=72):
				presion_10=1012.0306-109.0338*10+3.6316*(10**2)
				presion=presion_10*math.exp(-0.147*(altura-10))
			elif(72<altura<=100):
				presion_10=1012.0306-109.0338*10+3.6316*(10**2)
				presion_72=presion_10*math.exp(-0.147*(72-10))
				presion=presion_72*math.exp(-0.165*(altura-72))
			print("La presión del aire seco es de: ",presion,"hPa")
			#Calculo la densidad de vapor de agua
			if(0<=altura<=15):
				densidad_vapor=19.6542*math.exp(-0.2313*altura-0.1122*altura**2+0.01351*altura**3-0.0005923*altura**4)
			elif(altura>15):
				densidad_vapor=0
		#Caso de latitudes medias
		elif(22<=latitud<=45):
			respuesta=input("Estación del año (verano:v o invierno:i): ")
			if(respuesta=="v"):
				#Calculo la temperatura
				if(0<=altura<13):
					temperatura=294.9838-5.2159*altura-0.07109*altura**2
				elif(13<=altura<17):
					temperatura=215.5
				elif(17<=altura<47):
					temperatura=215.5*math.exp((altura-17)*0.008128)
				elif(47<=altura<53):
					temperatura=275
				elif(53<=altura<80):
					temperatura=275+(1-math.exp((altura-53)*0.06))*20
				elif(80<=altura<=100):
					temperatura=175
				print("La temperatura es de: ",temperatura,"K")
				#Calculo la presión de aire seco
				if(0<=altura<=10):
					presion=1012.8186-111.5569*altura+3.8646*altura**2
				elif(10<altura<=72):
					presion_10=1012.8186-111.5569*10+3.8646*10**2
					presion=presion_10*math.exp(-0.147*(altura-10))
				elif(72<altura<=100):
					presion_10=1012.8186-111.5569*10+3.8646*10**2
					presion_72=presion_10*math.exp(-0.147*(72-10))
					presion=presion_72*math.exp(-0.165*(altura-72))
				print("La presión del aire seco es de: ",presion,"hPa")
				#Calculo la densidad de vapor de agua
				if(0<=altura<=15):
					densidad_vapor=14.3542*math.exp(-0.4174*altura-0.02290*altura**2+0.001007*altura**3)
				elif(altura>15):
					densidad_vapor=0

			elif(respuesta=="i"):
				#Calculo la temperatura
				if(0<=altura<10):
					temperatura=272.7241-3.6217*altura-0.1759*altura**2
				elif(10<=altura<33):
					temperatura=218
				elif(33<=altura<47):
					temperatura=218+(altura-33)*3.3571
				elif(47<=altura<53):
					temperatura=265
				elif(53<=altura<80):
					temperatura=265-(altura-53)*2.0370
				elif(80<=altura<=100):
					temperatura=210
				print("La temperatura es de: ",temperatura,"K")
				#Calculo la presión de aire seco
				if(0<=altura<=10):
					presion=1018.8627-124.2954*altura+4.8307*altura**2
				elif(10<altura<=72):
					presion_10=1018.8627-124.2954*10+4.8307*10**2
					presion=presion_10*math.exp(-0.147*(altura-10))
				elif(72<altura<=100):
					presion_10=1018.8627-124.2954*10+4.8307*10**2
					presion_72=presion_10*math.exp(-0.147*(72-10))
					presion=presion_72*math.exp(-0.155*(altura-72))
				print("La presión del aire seco es de: ",presion,"hPa")
				#Calculo la densidad de vapor de agua
				if(0<=altura<=10):
					densidad_vapor=3.4742*math.exp(-0.2697*altura-0.03604*altura**2+0.0004489*altura**3)
				elif(altura>10):
					densidad_vapor=0				
		#Caso latitudes altas
		elif(latitud>45):
			respuesta=input("Estación del año (verano:v o invierno:i): ")
			if(respuesta=="v"):
				#Calculo la temperatura
				if(0<=altura<10):
					temperatura=286.8374-4.7805*altura-0.1402*altura**2
				elif(10<=altura<23):
					temperatura=225
				elif(23<=altura<48):
					temperatura=225*math.exp((altura-23)*0.008317)
				elif(48<=altura<53):
					temperatura=277
				elif(53<=altura<79):
					temperatura=277-(altura-53)*4.0769
				elif(79<=altura<=100):
					temperatura=171
				print("La temperatura es de: ",temperatura,"K")
				#Calculo la presión de aire seco
				if(0<=altura<=10):
					presion=1008.0278-113.2494*altura+3.9408*altura**2
				elif(10<altura<=72):
					presion_10=1008.0278-113.2494*10+3.9408*10**2
					presion=presion_10*math.exp(-0.140*(altura-10))
				elif(72<altura<=100):
					presion_10=1008.0278-113.2494*10+3.9408*10**2
					presion_72=presion_10*math.exp(-0.140*(72-10))
					presion=presion_72*math.exp(-0.165*(altura-72))
				print("La presión del aire seco es de: ",presion,"hPa")
				#Calculo la densidad de vapor de agua
				if(0<=altura<=15):
					densidad_vapor=8.988*math.exp(-0.3614*altura-0.005402*altura**2-0.001955*altura**3)
				elif(altura>15):
					densidad_vapor=0
				
			elif(respuesta=="i"):
				#Calculo la temperatura
				if(0<=altura<8.5):
					temperatura=257.4345+2.3474*altura-1.5479*altura**2+0.08473*altura**3
				elif(8.5<=altura<30):
					temperatura=217.5
				elif(30<=altura<50):
					temperatura=217.5+(altura-30)*2.125
				elif(50<=altura<54):
					temperatura=260
				elif(54<=altura<=100):
					temperatura=260-(altura-54)*1.667
				print("La temperatura es de: ",temperatura,"K")
				#Calculo la presión de aire seco
				if(0<=altura<=10):
					presion=1010.8828-122.2411*altura+4.554*altura**2
				elif(10<altura<=72):
					presion_10=1010.8828-122.2411*10+4.554*10**2
					presion=presion_10*math.exp(-0.147*(altura-10))
				elif(72<altura<=100):
					presion_10=1010.8828-122.2411*10+4.554*10**2
					presion_72=presion_10*math.exp(-0.147*(72-10))
					presion=presion_72*math.exp(-0.150*(altura-72))
				print("La presión del aire seco es de: ",presion,"hPa")
				#Calculo la densidad de vapor de agua
				if(0<=altura<=10):
					densidad_vapor=1.2319*math.exp(0.07481*altura-0.0981*altura**2+0.00281*altura**3)
				elif(altura>10):
					densidad_vapor=0

		#Cálculo de la presión parcial de vapor de agua
		respuesta=input("¿La atmósfera es normal o seca? n/s: ")
		if(respuesta=="n"):
			altura_escala=2
		elif(respuesta=="s"):
			altura_escala=6

		presion_parcial_vapor=(densidad_vapor*temperatura)/(216.7)
		print("La presión parcial de vapor de agua es de: ",presion_parcial_vapor,"hPa")

	#En caso de no tener información sobre latitud uso la atmósfera de referencia mundial anual media
	elif(respuesta=="n"):
		altura_geopotencial=(6356.766*altura)/(6356.766+altura)
		print("La altura geopotencial es de: ",altura_geopotencial, "km")
		#Cálculo de la temperatura
		if(0<=altura_geopotencial<=11):
			temperatura=288.15-6.5*altura_geopotencial
		elif(11<altura_geopotencial<=20):
			temperatura=216.65
		elif(20<altura_geopotencial<=32):
			temperatura=216.65+(altura_geopotencial-20)
		elif(32<altura_geopotencial<=47):
			temperatura=228.65+2.8*(altura_geopotencial-32)
		elif(47<altura_geopotencial<=51):
			temperatura=270.65
		elif(51<altura_geopotencial<=71):
			temperatura=270.65-2.8*(altura_geopotencial-51)
		elif(71<altura_geopotencial<=84.852):
			temperatura=214.65-2.0*(altura_geopotencial-71)
		else:
			if(86<=altura<=91):	
				temperatura=186.8673
			elif(91<altura<=100):	
				temperatura=263.1905-76.3232*((1-(((altura-91)/19.9429))**2))**0.5
		print("La temperatura es de: ",temperatura,"K")
		#Cálculo la presión del aire seco
		if(0<=altura_geopotencial<=11):
			presion=1013.25*(((288.15)/(288.15-6.5*altura_geopotencial)))**((-34.1632)/(6.5))
		elif(11<altura_geopotencial<=20):
			presion=226.3226*math.exp(-34.1632*(altura_geopotencial-11)/216.65)
		elif(20<altura_geopotencial<=32):
			presion=54.74980*(((216.65)/(216.65+(altura_geopotencial-20))))**34.1632
		elif(32<altura_geopotencial<=47):
			presion=8.680422*(((228.65)/(228.65+2.8*(altura_geopotencial-32))))**(34.1632/2.8)
		elif(47<altura_geopotencial<=51):
			presion=1.109106*math.exp(-34.1632*(altura_geopotencial-47)/270.65)
		elif(51<altura_geopotencial<=71):
			presion=0.6694167*(((270.65)/(270.65-2.8*(altura_geopotencial-51))))**(-34.1632/2.8)
		elif(71<altura_geopotencial<=84.852):
			presion=0.03956649*(((214.65)/(214.65-2.0*(altura_geopotencial-71))))**(-34.1632/2.0)
		else:
			if(86<=altura<=100):
				presion=math.exp(95.571899-4.011801*altura+0.06424731*altura**2+(-4.789660*(10**(-4)))*altura**3+(1.340543*(10**(-6)))*altura**4)
		print("La presión del aire seco es de: ",presion,"hPa")
		#Cálculo de la presión parcial de vapor de agua
		respuesta=input("¿La atmósfera es normal o seca? n/s: ")
		if(respuesta=="n"):
			altura_escala=2
		elif(respuesta=="s"):
			altura_escala=6

		densidad_vapor=7.5*math.exp(-altura/altura_escala)
		presion_parcial_vapor=(densidad_vapor*temperatura)/(216.7)
		print("La presión parcial de vapor de agua es de: ",presion_parcial_vapor,"hPa")
	return (temperatura, presion, presion_parcial_vapor,respuesta)