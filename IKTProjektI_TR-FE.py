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

# a

maxi=0
i=0
for i in range(0,len(t),1):
    if t[i]>t[maxi]:
        maxi=i
print(f"{maxi}. héten volt a legnagyobb nyereségünk")
# b
osszeg=0
for i in range (len(t)):
    osszeg+=t[i]
if osszeg<0:
     print(f"{osszeg}FT hiányzik a pénztárcánkból")
elif osszeg>0:
     print(f"{osszeg}FT  van a pénz tárcánkban")

# c
db=0
db2=0
for i in range(len(t)):
    if t[i]<0:
        db+=1
for i in range(len(t)):
    if t[i]>0:
        db2+=1
if db>db2:
    print("Többször vesztettünk")
elif db2>db:
     print("Többször nyertünk.")
else:
    print("Ugyananyiszor nyertünk mint vesztettünk.")

#d
db=0
maxny=0
maxj=0
sorozatvege=0

for i in range(len(t)):
    if (t[i]>0):
        if maxj==0:
            db+=1
        maxj+=1
    else:
        if(maxj>maxny):
            maxj==maxny
print(f" {maxny} napon keresztül volt nyerőszérriánk")

