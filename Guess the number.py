import random
from time import sleep
juste_prix=random.randint(1,100)
proposition = 0
i = 0
while proposition != juste_prix :
 i +=1
 sleep(2)
 proposition=int(input("Devinez le nombre compris entre 1 et 100"))
 if proposition < juste_prix : 
     print("Votre proposition est basse")
 elif proposition > juste_prix :
 	print("Votre propostion est trop haute")
 else :
 	print("Bravo, vous avez trouvé en ",i,"coups")

sleep(2)
if  0 < i < 5 :
 	print("Votre score est excellent")
elif 5 <= i < 10 :
 	print("Votre score est bon")
elif 10<= i < 15 :
 	print("Bien joué")
elif 15<= i < 20 : 
     print("Vous pouvez mieux faire")
else :
 	print("Vous n’êtes pas très bon à ce jeu")