def cislo_text(cislo):
    cislo = int(cislo)
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    nact = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
   
    if cislo < 10:
        return jednotky[cislo]
    elif 10 <= cislo < 20:
        return nact[cislo - 10]
    elif 20 <= cislo < 100:
        d = cislo // 10
        j = cislo % 10
        if j == 0:
            return desitky[d]
        else:
            return f"{desitky[d]} {jednotky[j]}"
    elif cislo == 100:
        return ("sto")
    else:
       return "čislo mimo rozsah"
   
if __name__ == "__main__":
    cislo =  input("Zadej číslo:")
    text = cislo_text(cislo)
    print (text)


