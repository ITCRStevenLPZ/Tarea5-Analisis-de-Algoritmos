import random
def burbuja(A):
    n = len(A)
    for i in range(1, n):
        for j in range(0, n - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
'''
def burbuja_optimizado2(A):#La optimizacion del algoritmo burbuja es que simplemente se le anade un contador "c" el cual se suma si ya esta ordenado y se resta si no esta ordenado
	n = len(A)			  #Cada vez que este ordenado se verifica si "c" no es mayor a "n/2", si es asi, el programa considera ordenada la lista y hace break
	c = 0
	for i in range(n - 1):
		for j in range(0, n - i - 1):
			if A[j] > A[j + 1]:
				swap(A, j, j + 1)
				c-=1
			else:
				if c >= n/2:
					break
				else:
					c+=1
'''					

def burbuja_optimizado(A): #El anterior algoritmo se sometio a una lista la cual no mostro un resultado acertado, la lista en cuestion fue: A=[21,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,1,0]
	M = True			   #Por lo tanto se ideo un algoritmo de banderas, en este caso "M" el cual significa movimiento, e indica si se hizo un swap o no y abarca toda la lista
	n = len(A)
	for i in range(1, n):
		if M == True:
			M = False
			for j in range(0, n - i):
				if A[j] > A[j + 1]:
					swap(A, j, j + 1)
					M = True
		else:
			break 

    ##raise NotImplementedError()