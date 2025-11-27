class InvalidData(Exception):
    pass

class osoba:

    def __init__(self, jmeno, telefon, mail):
        self.jmeno = jmeno
        self.telefon = telefon
        self.mail = mail
    def __str__(self):
        return f"osoba({self.jmeno}, {self.telefon}, {self.mail})"
    
    def __str__(self):
        return f"osoba({self.jmeno}, {self.telefon}, {self.mail})"
    

    @property
    def jmeno(self):
        return self.__jmeno #umíme přečíst jméno,ale nejde zapsat
    @property
    def telefon(self):
        return self.__telefon
    
    
    @telefon.setter
    def telefon(self, hodnota:str):
        if not hodnota.startswith("+420"):
            raise InvalidData(f'Nelze "{hodnota}" - musí začínat na +420')
        for c in hodnota:
            if not c.isdigit() and hodnota [0] != '+': #!= nerovná se , isalnum 
                 raise InvalidData(f'Nelze "{hodnota}"')
        if len(hodnota) == 13:
            raise InvalidData(f'Nelze "{hodnota}" - musí být přesně 13 číslic')
        self.__telefon = hodnota
    
    @jmeno.setter
    def jmeno(self, hodnota:str):
        for c in hodnota:
            if not c.isalpha() and not c.isspace():
                raise InvalidData(f'Nelze "{hodnota}"')
        self.__jmeno = hodnota #můžeme do toho zapisovat 

   
if __name__ == "__main__":
    o1 = osoba("jan", "+4204567890123", "???")

    print(o1)