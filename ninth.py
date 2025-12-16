def dec_to_bin(cislo):
    try:
        n = int(cislo)
    except Exception:
        raise ValueError(f"Neplatný vstup: {cislo}")

    if n == 0:
        return "0"

    sign = ""
    if n < 0:
        sign = "-"
        n = -n

    vysledek = []
    while n > 0:
        vysledek.append(str(n & 1))
        n >>= 1

    return sign + "".join(reversed(vysledek))


def test_dec_to_bin():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"
    assert dec_to_bin(-5) == "-101"
    try:
        dec_to_bin("12.3")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for non-integer input")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] in ("--test", "-t"):
        test_dec_to_bin()
        print("Tests passed")
        sys.exit(0)

    if len(sys.argv) > 1:
        vstup = sys.argv[1]
    else:
        try:
            vstup = input("Zadej dekadické číslo: ")
        except EOFError:
            sys.exit(1)

    try:
        print(dec_to_bin(vstup))
    except ValueError as e:
        print("Chyba:", e)
        sys.exit(1)
