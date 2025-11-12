import sys
import os

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    """
    Načte prvnich header_length bytů ze souboru file_name.
    Pokud soubor neexistuje, vyhodí FileNotFoundError.
    """
    with open(file_name, 'rb') as f:
        return f.read(header_length)


def is_jpeg(file_name):
    header = read_header(file_name, len(jpeg_header))
    return header == jpeg_header


def is_gif(file_name):
    header = read_header(file_name, len(gif_header1))
    return header == gif_header1 or header == gif_header2


def is_png(file_name):
    header = read_header(file_name, len(png_header))
    return header == png_header


def print_file_type(file_name):
    """
    Vypíše typ souboru; také pro debug vypíše prvních 16 bytů v hexu.
    """
    try:
        # debug: ukaž cestu a prvních pár bytů (hex) - velmi užitečné při ladění
        abs_path = os.path.abspath(file_name)
        header_for_debug = read_header(file_name, 16)
        header_hex = ' '.join(f'{b:02x}' for b in header_for_debug)
        print(f"DEBUG: Kontroluji soubor: {file_name}")
        print(f"DEBUG: Absolutní cesta: {abs_path}")
        print(f"DEBUG: Prvních {len(header_for_debug)} bytů (hex): {header_hex}")

        if is_jpeg(file_name):
            print(f"Soubor {file_name} je typu jpeg")
        elif is_gif(file_name):
            print(f"Soubor {file_name} je typu gif")
        elif is_png(file_name):
            print(f"Soubor {file_name} je typu png")
        else:
            print(f"Soubor {file_name} je neznámého typu")
    except FileNotFoundError:
        print(f"Chyba: soubor '{file_name}' nebyl nalezen.")
    except PermissionError:
        print(f"Chyba: nelze otevřít '{file_name}' — nedostatečná práva.")
    except Exception as e:
        print(f"Nastala neočekávaná chyba při čtení '{file_name}': {e}")


if __name__ == '__main__':
    try:
        # pokud uživatel nezadal argumenty, nabídneme interaktivní vstup
        if len(sys.argv) < 2:
            file_name = input("Zadejte název souboru (nebo cestu): ").strip()
        else:
            # podpora více souborů: zpracujeme všechny argumenty
            for arg in sys.argv[1:]:
                print_file_type(arg)
            # skončíme (u více argumentů jsme všechno zpracovali)
            sys.exit(0)

        print_file_type(file_name)

    except Exception as e:
        print(f"Nastala chyba: {e}")
