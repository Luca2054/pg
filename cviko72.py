class Osoba:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __str__(self):
        return f"Osoba: {self.jmeno}"
    
class student(Osoba): #dědí z osoby
    def __init__(self, jmeno, rocnik):
        super().__init__(jmeno)
        self.rocnik = rocnik 
    
    def dalsi_rocnik(self):
        
        if self.rocnik >= 5:
            
            raise Exception("konec studia")
        self.rocnik += 1
    

    def __str__(self):
        return f"Student: {self.jmeno} studuje {self.rocnik} rocnik"
    
class Ucitel(Osoba): #dědí z osoby
    def __init__(self, jmeno, roky_praxe=0):
        super().__init__(jmeno) #volání nadřazené metody
        self.roky_praxe = roky_praxe
    def __str__(self):
        return f"Ucitel {self.jmeno} ma {self.roky_praxe} let praxe"

    def pridat_rok(self):
        self.roky_praxe += 1

if __name__ == "__main__":
    student1 = student("Alice", 1)
    student2 = student("Bob", 2)

    ucitel1 = Ucitel("Prof")

    for i in range(5):
        osoba.pridat_rok()
    print(ucitel1)
