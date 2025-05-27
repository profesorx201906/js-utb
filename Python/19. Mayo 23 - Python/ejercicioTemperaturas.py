#Ejercicio temperaturas
import random
temperaturas=[]

N= int(input("digite el numero temperaturas: "))
for i in range(N):
  temperaturas.append(random.randint(0,100))

maxima = max(temperaturas)
minima = min(temperaturas)
media = sum(temperaturas)/len(temperaturas)
print(temperaturas)
print(f" maxima {maxima} minima {minima} media {media}")