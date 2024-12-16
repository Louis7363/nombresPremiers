import premier
import math
import time

n = int(input("Quel nombre souhaitait vous déterminer sa primarité"))
n = premier.nombre_premier(n)

methode = int(input("Quel méthode souhatez-vous utiliser (chiffre)? 1 : Naïve; 2 : Par la racine; 3 : par la racine et impair et 4: avec le crible d'eratosthène"))

if methode == 1 :
    start1 = time.time()
    print(n.PremierNaive())
    end1 = time.time()
    print("Temps d'execution : " + str(end1-start1))
elif methode == 2 :
    start2 = time.time()
    print(n.PremierRacine())
    end2 = time.time()
    print("Temps d'exectution : " + str(end2-start2))
elif methode == 3 :
    start3 = time.time()
    print(n.PremierRacineImpair())
    end3 = time.time()
    print("Temps d'exectution : " + str(end3-start3))
else :
    start4 = time.time()
    print(n.PremierCrible())
    end4 = time.time()
    print("Temps d'exectution : " + str(end4-start4))