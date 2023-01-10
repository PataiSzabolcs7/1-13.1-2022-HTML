ez = ["Én", "nem", "vagyok", "egy", "csodabogár"]
az = ["Én", "nem", "vagyok", "egy", "csodabogár"]
print("Test 1:{0}".format(ez is az))
ez = az
print("Test 2:{0}".format(ez is az))

#Mivel az első esetnél, hiába ugyan azok vannak a listába a program azt nézi, hogy a változó egyenlő-e egymással. A második esétnél azért true, mert előtte oda írtuk, hogy a változó = b változóval! Ézért lett True a Második teszt