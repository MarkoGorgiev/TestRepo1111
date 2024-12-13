from _ast import mod


# class Car():
#     def __init__(self, boja, mokjnost, kapaciter_rezvoar, cena):
#         self.color = boja
#         self.power = mokjnost
#         self.tank_capacity = kapaciter_rezvoar
#         self.fuel_level = 0
#         self.cena = cena
#         self.__liznig = 0
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
#
#     @staticmethod
#     def sell_car(boja):
#         if boja.lower() == "zolta":
#             print("Imate 10% popust na kolata")
#         else:
#             print("Nemate popust")
#
#     @staticmethod
#     def format_procent(procent):
#         return f"{procent * 100}%"
#
#     def kamata_liznig(self):
#         """
#         Metod za presmetuvanje na kamata za liznig
#         :return: kamatnata stapka za liznig
#         """
#         if self.cena > 10_000:
#             self.__liznig = 0.01
#         elif self.cena >= 5_000:
#             self.__liznig = 0.012
#         else:
#             self.__liznig = 0.015
#
#         return self.__liznig


# car = Car("Zolta", 1000, 100, 5000)
#
# car.drive()
# car.fill_fuel()
# car.drive()
# car.sell_car("Crvena") # Povikuvanje na statickata metoda preku instanca

# Car.sell_car("Zolta") # Povikuvanje na statickata metoda preku samata klasa

# print("Kamatata za liznig na voziloto iznesuva", Car.format_procent(car.kamata_liznig()))
# # car.liznig = 0 # !!! pristap do senzetiven podatok na neprivaten atribut
# print(car.cena)
#
# # car.__liznig = 2
# print(car.__liznig)


# class Car():
#     def __init__(self, boja, cena, moknost):
#         self.boja = boja
#         self.cena = cena
#         self.moknost = moknost
#
#     def max_speed(self):
#         return self.moknost * 30
#
# class Bike():
#     def __init__(self, boja, cena, moknost, zafatnina_na_motor):
#         self.boja = boja
#         self.cena = cena
#         self.moknost = moknost
#         self.zafatnina_na_motor = zafatnina_na_motor
#
#     def max_speed(self):
#         return self.moknost * 50
#
# class Truck():
#     def __init__(self, boja, cena, moknost, vlecna_moknost):
#         self.boja = boja
#         self.cena = cena
#         self.moknost = moknost
#         self.vlecna_moknost = vlecna_moknost
#
#     def max_speed(self):
#         return self.moknost * 10