# Tarczali Roland
# Feke Erik
# 10C
# "Első IKT beadandó"
import random

t=[]
n=int(input())

for i in range(n):
    t.append(random.randint(-10000,10000))
# kiírás
for i in range (len(t)):
    print(t[i], end=" ")
print()


# b
osszeg=0
for i in range (len(t)):
    osszeg+=t[i]
if osszeg<0:
    print(f"{osszeg} hiányzik a pénztárcánkból")
elif osszeg>0:
    print(f"{osszeg} van a pénz tárcánkban")