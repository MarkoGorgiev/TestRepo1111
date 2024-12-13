# реирајте класа Vraboten и класа Kompanija
# Потоа креирајте x објекти од класата вработен и еден објект од класта Kompanija
# Класата Vraboten ги има следните атрибури:
# име
# мбр
# плата
# датум на вработување
# Додека пак класата Kompanija ги има следните атрибути:
# име
# вработени (листа вработени)
# Дополнително размислете каде и како може да ги зачувате податоците со цел
# не внесуваме рачно голем број на податоци при секој старт на програмата.

# class Vraboten():
#     def __init__(self, ime, mbr, plata, datum_vrab):
#         self.ime = ime
#         self.mbr = mbr
#         self.plata = plata
#         self.datum_vrab = datum_vrab
#
#     def __str__(self):
#         return f"Ime: {self.ime}\nDatum Vrabotuvanje: {self.datum_vrab}"
#
#     def pokacuanje_plata(self, pokacuvanje):
#         self.plata = self.plata + pokacuvanje
#
#     def pokacunanje_plata_procent(self, procent):
#         self.plata = self.plata + self.plata * procent
#
#
# class Kompanija():
#     def __init__(self, ime, vraboteni = []):
#         self.ime = ime
#         self.vraboteni = vraboteni
#
#     def __str__(self):
#         opis_kompanija = f"Ime kompanija: {self.ime}\nBroj na vraboteni: {len(self.vraboteni)}\nVraboteni:\n"
#         for vraboten in self.vraboteni:
#             opis_kompanija += "\n" + vraboten.__str__() + "\n"
#
#         return opis_kompanija
#
#     def dodadi_vraboten(self, vraboten):
#         try:
#             self.vraboteni.append(vraboten)
#             return True
#         except:
#             return False
#
#
# vraboten1 = Vraboten("Петар Петровски", "0505000450234", 30000, "2018, 4, 22")
# vraboten2 = Vraboten("Марко Марковски", "0811983450789", 43000, "2013, 10, 12")
# vraboten3 = Vraboten("Стојан Стојановски", "2201999450237", 34000, "2023, 6, 1")
# vraboten4 = Vraboten("Никола Николовски", "1506995450643", 38000, "2019, 4, 22")
#
# # print(vraboten1)
# kompanija = Kompanija("My Company", [vraboten1, vraboten4, vraboten3, vraboten2])
# # print(kompanija)
# # nov_vraboten = Vraboten("Nov vraboten", "1234567891112", 1000, "29 11 2024")
# #
# # # kompanija.vraboteni.append(nov_vraboten) los nacin za dodavanje na novi vraboteni
# # if kompanija.dodadi_vraboten(nov_vraboten):
# #     print("Uspesno dodavanje na noviot vraboten")
# #     print(kompanija)
#
# vraboten4.pokacunanje_plata_procent(0.1)
# print(vraboten4.plata)

# class Vraboten():
#     def __init__(self, ime, prezime, mbr, plata = 0):
#         # print("Se sozdrava objekt od Vraboten")
#         self.name = ime
#         self.surname = prezime
#         self.SSN = mbr
#         self.salary = plata
#
#     def set_salary(self, plata):
#         self.salary = plata
#
#
# vraboten1 = Vraboten("Ime 1", "Prezime 1", "1")
# vraboten2 = Vraboten("Ime 2", "Prezime 2", "2", 1000)
#
#
# # vraboten1.salary = 1000
# vraboten1.set_salary(1000)


# Да се креира класа кола (Car)
# Класата ги има следните атрибути:
# Boja
# Mokjnost
# Kapacitet_rezervoar
# Gorivo
#
# На почеток секоја инстанца започнува со гориво 0
#
# Напишете метод кој што ќе прави fill_fuel на горивото.
# Напишете метод кој што ќе прави tuning на возилото за одреден процент


# class Car():
#     def __init__(self, boja, mokjnost, kapaciter_rezvoar):
#         self.color = boja
#         self.power = mokjnost
#         self.tank_capacity = kapaciter_rezvoar
#         self.fuel_level = 0
#
#     def fill_fuel(self):
#         """
#         fuel_level = procent na polnost
#         0% - 100%
#         """
#         print("fuel filled")
#         self.fuel_level = 100
#
#     def drive(self):
#         if self.fuel_level == 0:
#             print("Out of fuel, please fill the tank")
#         else:
#             print("Wroom, Wroom!")


# car1 = Car("crvena", 1000, 500)
# # car2 = Car("zolta", 1500, 800)
#
# car1.drive()
# car1.fill_fuel()
# car1.drive()
#
# my_list = [1, 2, 3]
# my_list.ap

def sell_car(boja):
    if boja.lower() == "zolta":
        print("Imate 10% popust na kolata")
    else:
        print("Nemate popust")