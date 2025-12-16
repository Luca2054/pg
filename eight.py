def bin_to_dec(binarni_cislo):
    
    bin_str = str(binarni_cislo).strip()
    if bin_str.startswith(("0b", "0B")):
        bin_str = bin_str[2:]
    if bin_str == "":
        raise ValueError("Prázdný vstup")
    for ch in bin_str:
        if ch not in "01":
            raise ValueError(f"Neplatný znak v binárním čísle: {ch}")

    vysledek = 0
    for znak in bin_str:
        vysledek = vysledek * 2 + int(znak)

    return vysledek


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] in ("--test", "-t"):
        test_bin_to_dec()
        print("Tests passed")
        sys.exit(0)

    if len(sys.argv) > 1:
        vstup = sys.argv[1]
    else:
        try:
            vstup = input("Zadej binární číslo: ")
        except EOFError:
            sys.exit(1)

    try:
        vysledek = bin_to_dec(vstup)
        print(vysledek)
    except ValueError as e:
        print("Chyba:", e)
        sys.exit(1)
