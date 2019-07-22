import math

k_horizontal={1:[-5.33980,-0.10008,1.13098,-0.18961,0.71147],
2:[-0.35351,1.26970,0.45400,-0.18961,0.71147],
3:[-0.23789,0.86036,0.15354,-0.18961,0.71147],
4:[-0.94158,0.64552,0.16817,-0.18961,0.71147]}

alfa_horizontal={1:[-0.14318,1.82442,-0.55187,0.67849,-1.95537],
2:[0.29591,0.77564,0.19822,0.67849,-1.95537],
3:[0.32177,0.63773,0.13164,0.67849,-1.95537],
4:[-5.37610,-0.96230,1.47828,0.67849,-1.95537],
5:[16.1721,-3.29980,3.43990,0.67849,-1.95537]}


def calcula_coef_k_horizontal(frecuencia):

	i=1
	sumatorio=0.0

	while i<=len(k_horizontal):
		expresion=k_horizontal[i][0]*math.exp(-((math.log10(frecuencia)-k_horizontal[i][1])/k_horizontal[i][2])**2)
		sumatorio=sumatorio+expresion
		i=i+1

	log10_k=sumatorio+(k_horizontal[1][3]*math.log10(frecuencia)+k_horizontal[1][4])
	return log10_k


def calcula_coef_alfa_horizontal(frecuencia):

	i=1
	sumatorio=0.0

	while i<=len(alfa_horizontal):
		expresion=alfa_horizontal[i][0]*math.exp(-((math.log10(frecuencia)-alfa_horizontal[i][1])/alfa_horizontal[i][2])**2)
		sumatorio=sumatorio+expresion
		i=i+1

	alfa=sumatorio+alfa_horizontal[1][3]*math.log10(frecuencia)+alfa_horizontal[1][4]
	return alfa