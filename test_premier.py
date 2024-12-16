import premier
n = premier.nombre_premier(191)
assert n.PremierNaive() == True, "Le code ne marche pas"
assert n.PremierRacine() == True, "Le code ne marche pas"
assert n.PremierRacineImpair() == True, "Le code ne marche pas"
assert n.PremierCrible() == True, "Le code ne marche pas"

n = premier.nombre_premier(83)
assert n.PremierNaive() == True, "Le code ne marche pas"
assert n.PremierRacine() == True, "Le code ne marche pas"
assert n.PremierRacineImpair() == True, "Le code ne marche pas"
assert n.PremierCrible() == True, "Le code ne marche pas"

n = premier.nombre_premier(2)
assert n.PremierNaive() == True, "Le code ne marche pas"
assert n.PremierRacine() == True, "Le code ne marche pas"
assert n.PremierRacineImpair() == True, "Le code ne marche pas"
assert n.PremierCrible() == True, "Le code ne marche pas"

n = premier.nombre_premier(1)
assert n.PremierNaive() == False, "Le code ne marche pas"
assert n.PremierRacine() == False, "Le code ne marche pas"
assert n.PremierRacineImpair() == False, "Le code ne marche pas"
assert n.PremierCrible() == False, "Le code ne marche pas"