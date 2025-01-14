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
for i in range(len(t)):
    if (t[i]>0):
        db+=1
        if (db>0 and not(db<0)):
            maxj=db
        elif(db<0):
            maxj!=db
        maxny=maxj
    
print(f" {maxny} napon keresztül volt nyerőszérriánk")

max_hossz = 0 
jelenlegi_hossz = 0 
kezd_het = 0 
veg_het = 0 
legjobb_kezd_het = 0 
legjobb_veg_het = 0 
for i in range(len(t)): 
    if t[i]>0: 
        if jelenlegi_hossz==0: 
            kezd_het=i+1 
            jelenlegi_hossz+=1 
        else: 
            if jelenlegi_hossz>max_hossz: 
                max_hossz=jelenlegi_hossz 
                legjobb_kezd_het=kezd_het 
                legjobb_veg_het=i 
                jelenlegi_hossz=0 
            if jelenlegi_hossz>max_hossz: 
                max_hossz=jelenlegi_hossz 
                legjobb_kezd_het=kezd_het 
                legjobb_veg_het=len(t) 
if max_hossz>0: 
    print(f"A {legjobb_kezd_het}. és {legjobb_veg_het}. hét között volt {max_hossz} héten keresztül a leghosszabb nyerő sorozat.") 
else:
     print("Nincs nyerő sorozat.")