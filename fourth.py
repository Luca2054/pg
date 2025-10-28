def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """

    typ = figurka["typ"]
    start = figurka["pozice"]

    # Kontrola, že cílová pozice je na šachovnici (1–8)
    r, c = cilova_pozice
    if not (1 <= r <= 8 and 1 <= c <= 8):
        return False

    #Cílové pole nesmí být obsazené
    if cilova_pozice in obsazene_pozice:
        return False

    # Výpočet rozdílu v řádcích a sloupcích
    dr = cilova_pozice[0] - start[0]
    dc = cilova_pozice[1] - start[1]

   
    if typ == "pěšec":
    # Pěšec se nemůže hýbat do stran ani dozadu
        if dc != 0 or dr <= 0:
            return False
    # O jedno pole dopředu
        if dr == 1 and (start[0] + 1, start[1]) not in obsazene_pozice:
            return True
    # O dvě pole dopředu ze startovní pozice
        if (
            dr == 2
            and start[0] == 2
            and (start[0] + 1, start[1]) not in obsazene_pozice
            and (start[0] + 2, start[1]) not in obsazene_pozice):
            return True
        return False

    if typ == "jezdec":
        return (abs(dr), abs(dc)) in [(1, 2), (2, 1)]

    def je_cesta_volna():
        step_r = (dr > 0) - (dr < 0)
        step_c = (dc > 0) - (dc < 0)
        r, c = start
        while (r + step_r, c + step_c) != cilova_pozice:
            r += step_r
            c += step_c
            if (r, c) in obsazene_pozice:
                return False
        return True


    if typ == "věž":
        if dr != 0 and dc != 0:
            return False
        return je_cesta_volna()

 
    if typ == "střelec":
        if abs(dr) != abs(dc):
            return False
        return je_cesta_volna()


    if typ == "dáma":
        if dr == 0 or dc == 0 or abs(dr) == abs(dc):
            return je_cesta_volna()
        return False


    if typ == "král":
        return abs(dr) <= 1 and abs(dc) <= 1

    return False

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
