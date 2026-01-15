import math

def statistika(rezim, cisla):
    """
    rezim: "soucet" | "pocet" | "max" | "min" | "prumer"
    cisla: list[int] nebo list[float]

    Vrat:
      - "soucet": soucet vsech cisel v seznamu
      - "pocet": pocet prvku v seznamu
      - "max": nejvetsi hodnota v seznamu (pokud je seznam prazdny, vrat None)
      - "min": nejmensi hodnota v seznamu (pokud je seznam prazdny, vrat None)
      - "prumer": aritmeticky prumer (pokud je seznam prazdny, vrat None)

    Nepouzivej vestavene funkce sum(), max(), min().
    Pouzij cyklus a podminky.
    """
    if rezim == "soucet": # pokud chceme součet - sečteme všechny prvky v seznamu
        soucet = 0
        for x in cisla:
            soucet += x
        return soucet # a vrátí součet
    
    elif rezim == "max": # pokud chceme maximum 
        if not cisla:
            return None
        maximum = cisla[0]
        for x in cisla: # do maximum dáme první prvek seznamu a pak postupně zkoumáme všechny prvky, zda nejsou větší
            if x > maximum:
                maximum = x
        return maximum

    elif rezim == "min":
        if not cisla:
            return None
        minimum = cisla[0]
        for x in cisla:
            if x < minimum:
                minimum = x
        return minimum
    
    elif rezim == "pocet": # pokud chceme počet prvků v seznamu
        pocet = 0
        for _ in cisla:
            pocet += 1 # program je postupně načítá a za každý prvek přičte 1
        return pocet

    elif rezim == "prumer": # pokud chceme průměr 
        if not cisla:
            return None
        soucet = 0
        pocet = 0
        for x in cisla:
            soucet += x
            pocet += 1
        return soucet / pocet # výpočet průměru = součet / počet

    else:
        return None

    


def test_statistika():
    assert statistika("soucet", [1, 2, 3, 4]) == 10
    assert statistika("soucet", [-1, -2, -3]) == -6
    assert statistika("soucet", []) == 0
    assert statistika("pocet", [1, 2, 3]) == 3
    assert statistika("pocet", []) == 0
    assert statistika("max", [1, 9, 3]) == 9
    assert statistika("max", [-10, -2, -30]) == -2
    assert statistika("max", []) is None
    assert statistika("min", [1, 9, 3]) == 1
    assert statistika("min", [-10, -2, -30]) == -30
    assert statistika("min", []) is None
    assert math.isclose(statistika("prumer", [2, 4, 6]), 4.0)
    assert math.isclose(statistika("prumer", [1, 2]), 1.5)
    assert statistika("prumer", []) is None
    assert statistika("neco", [1, 2, 3]) is None


if __name__ == "__main__":
    print(statistika("soucet", [1, 2, 3]))     # 6
    print(statistika("pocet", [1, 2, 3]))     # 3
    print(statistika("max", [1, 9, 3]))       # 9
    print(statistika("min", [1, 9, 3]))       # 1
    print(statistika("prumer", [2, 4, 6]))    # 4.0