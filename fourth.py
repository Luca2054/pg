import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    """
    Načte prvních `header_length` bytů ze souboru `file_name`
    """
    with open(file_name, 'rb') as f:
        return f.read(header_length)


def is_jpeg(file_name):
    """
    Ověří, zda má soubor hlavičku JPEG
    """
    header = read_header(file_name, len(jpeg_header))
    return header == jpeg_header


def is_gif(file_name):
    """
    Ověří, zda má soubor hlavičku GIF (může být GIF87a nebo GIF89a)
    """
    header = read_header(file_name, len(gif_header1))
    return header == gif_header1 or header == gif_header2


def is_png(file_name):
    """
    Ověří, zda má soubor hlavičku PNG
    """
    header = read_header(file_name, len(png_header))
    return header == png_header


def print_file_type(file_name):
    """
    Vypíše typ souboru
    """
    if is_jpeg(file_name):
        print(f"Soubor {file_name} je typu jpeg")
    elif is_gif(file_name):
        print(f"Soubor {file_name} je typu gif")
    elif is_png(file_name):
        print(f"Soubor {file_name} je typu png")
    else:
        print(f"Soubor {file_name} je neznámého typu")


if __name__ == '__main__':
    try:
        file_name = input("Zadejte název souboru: ")
        print_file_type(file_name)
    except Exception as e:
        print(f"Nastala chyba: {e}")

