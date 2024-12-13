

# class Employee:
#     name = ""
#     surname = ""
#     age = ""
#     salaray = 0


# vraboten1 = Employee()
# vraboten1.name = "Ime 1"
# vraboten1.surname = "Prezime 1"
# vraboten1.age = 20
#
# print(vraboten1.surname)

# Внесете податоци за 5 вработени (име, години, плата)
# и потоа пресметајте просечна плата
# и испечатете ги имињата и платите на вработените
# кои што имаат плата над просечната

# class Laptop:
#     golemina_ekran = "14'"
#     boja = "crna"
#     procesor = ""
#
# class Vraboten:
#     ime = ""
#     godini = ""
#     plata = 0


# lista_vraboteni = list()
# lista_vraboteni = []
# my_dict = dict()
# my_dict = {}

# # for i in range(5):
# for _ in range(5):
#     # Gi kreirame objektite od vraboteni i gi dodavame vo listata so vraboteni
#     temp_vraboten = Vraboten()
#
#     temp_vraboten.ime = input("Vnesi go imeto na vraboteniot: ")
#     temp_vraboten.godini = input("Vnesi gi godinite na vraboteniot: ")
#     temp_vraboten.plata = float(input("Vnesi ja platata na vraboteniot: "))
#
#     lista_vraboteni.append(temp_vraboten)
#
# suma_plata = 0
#
# for vrab in lista_vraboteni:
#     # Gi izminuvame objektite i pravime suma na plata
#     # suma_plata = suma_plata + vrab.plata
#     suma_plata += vrab.plata
#
# print(f"Vkupnata plata na vrabotenite iznesuva: {suma_plata}")
#
# prosecna_plata = suma_plata / len(lista_vraboteni)
# print(f"Prosecnata plata na vrabotenite iznesuva: {prosecna_plata}")
#
# for vrab in lista_vraboteni:
#     # Printanje na vrabotenite sto go zadovoluvaat uslovot
#     if vrab.plata >= prosecna_plata:
#         print(f"Vraboteniot {vrab.ime} ima nadprosecna plata: {vrab.plata}")


# class Vraboten:
#     def __init__(self, ime, godini, plata):
#         self.name = ime
#         self.age = godini
#         self.salary = plata
#
#     def __str__(self):
#         return f"Ime: {self.name}, salary: {self.salary}"



# x = Vraboten("Vrab 1", 100, 50)
# y = Vraboten("Vrab 2", 11, 55)

# print(x)  # Ime: Vrab 1, salary: 50
# print(y)  # Ime: Vrab 2, salary: 55



class Vraboten:
    def __init__(self, ime, godini, plata, mbr=""):
        self.name = ime
        self.age = godini
        self.salary = plata
        self.mbr = mbr

    def __str__(self):
        return f"Ime: {self.name}, salary: {self.salary}"

lista_vraboteni = []

for _ in range(2):
    # Gi kreirame objektite od vraboteni i gi dodavame vo listata so vraboteni
    ime_vraboten = input("Vnesi go imeto na vraboteniot: ")
    godini_vraboten = input("Vnesi gi godinite na vraboteniot: ")
    plata_vraboten = int(input("Vnesi ja platata na vraboteniot: "))

    vraboten = Vraboten(ime_vraboten, godini_vraboten, plata_vraboten) # ke go povika __init__ metodot

    lista_vraboteni.append(vraboten)
    # vraboten = Vraboten(ime=ime_vraboten, plata=plata_vraboten, godini=godini_vraboten)


suma_plata = 0

for vrab in lista_vraboteni:
    # Gi izminuvame objektite i pravime suma na plata
    suma_plata += vrab.salary

print(f"Vkupnata plata na vrabotenite iznesuva: {suma_plata}")

prosecna_plata = suma_plata / len(lista_vraboteni)
print(f"Prosecnata plata na vrabotenite iznesuva: {prosecna_plata}")

for vrab in lista_vraboteni:
    # Printanje na vrabotenite sto go zadovoluvaat uslovot
    if vrab.salary >= prosecna_plata:
        print(f"Vraboteniot {vrab.name} ima nadprosecna plata: {vrab.salary}")