import math

def je_prvocislo(cislo):
    
    # Prvocisla jsou pouze cisla vetsi nez 1 (nejsou prvočísla)
    if cislo <= 1:
        return False
    
    # Zkontroluje delitele pouze do druhé odmocniny z cisla
    for i in range(2, int(math.sqrt(cislo)) + 1):#zaokrouhlení druhé odmocniny na celá
        if cislo % i == 0:#dělení beze zbytku
            return False
    return True
    
print(je_prvocislo(11)) 

def vrat_prvocisla(maximum): #Funkce spočíta vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    prvocisla = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            prvocisla.append(i)# Přidáme prvočíslo do seznamu
    return(prvocisla)

if __name__ == "__main__":
    maximum = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(maximum)
    print(prvocisla)