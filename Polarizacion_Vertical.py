import math

k_vertical={1:[-3.80595,0.56934,0.81061],
2:[-3.44965,-0.22911,0.51059],
3:[-0.39902,0.73042,0.11899],
4:[0.50167,1.07319,0.27195]}

m_k=-0.16398
c_k=0.63297


alfa_vertical={1:[-0.07771,2.33840,-0.76284],
2:[0.56727,0.95545,0.54039],
3:[-0.20238,1.14520,0.26809],
4:[-48.2991,0.791669,0.116226],
5:[48.5833,0.791459,0.116479]}

m_alfa=-0.053739
c_alfa=0.83433


def calcula_coef_k_vertical(frecuencia):

	i=1
	sumatorio=0.0

	while i<=len(k_vertical):
		expresion=k_vertical[i][0]*math.exp(-((math.log10(frecuencia)-k_vertical[i][1])/k_vertical[i][2])**2)
		sumatorio=sumatorio+expresion
		i=i+1

	log10_k=sumatorio+(m_k*math.log10(frecuencia)+c_k)
	return log10_k


def calcula_coef_alfa_vertical(frecuencia):

	i=1
	sumatorio=0.0

	while i<=len(alfa_vertical):
		expresion=alfa_vertical[i][0]*math.exp(-((math.log10(frecuencia)-alfa_vertical[i][1])/alfa_vertical[i][2])**2)
		sumatorio=sumatorio+expresion
		i=i+1

	alfa=sumatorio+(m_alfa*math.log10(frecuencia)+c_alfa)
	return alfa