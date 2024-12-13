# class A():
#     def __init__(self):
#         self.public_att_a = "public a"
#         self._protected_att_a = "protected a"
#         self.__private_att_a = "private a"
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.public_att_b = "public b"
#         self._protected_att_b = "protected b"
#         self.__private_att_b = "private b"

# instance_a = A()
# print(instance_a.public_att_a)
# print(instance_a._protected_att_a)  #
# print(instance_a.__private_att_a)  # nemame pristap do private att
# instance_b = B()
#
# print(instance_b.public_att_a)
# print(instance_b.public_att_b)
# print(instance_b._protected_att_a)
# print(instance_b._protected_att_b)
# print(instance_b.__private_att_a)
# print(instance_b.__private_att_b)


class Employee():
    def __init__(self, ime, plata, pozicija):
        self.ime = ime
        self._plata = plata
        self.pozicija = pozicija
        self._bonus_procent = 0.1

    def get_plata(self):
        return self._plata

    def get_bonus(self):
        return self._plata * self._bonus_procent

class Manager(Employee):
    def __init__(self, ime, plata, pozicija, oddel):
        super().__init__(ime, plata, pozicija)
        self.menagira = oddel
        self.__neto_plata = self._plata + self._plata * 0.1
        self.__dodadeten_bonus_menager = 1.05

    def get_neto_plata(self):
        """
        platata za menadzerite e 10% povisoka od platata na rabotenite
        :return: self.plata
        """
        return self.__neto_plata

    def get_bonus(self):
        return self._plata * self._bonus_procent * self.__dodadeten_bonus_menager

vrab1 = Employee("Vraboten 1", 10000, "obezbeduvanje")
vrab2 = Employee("Vraboten 2", 12000, "obezbeduvanje nokjna smena")
shef_obezbeduvanje = Manager("Manager", 12000, "shef na obzbeduvanje", "Obzbeduvanje")

# print("plata vrab 2 zema plata od:", vrab2.plata)
# print("plata vrab 2 zema plata od:", vrab2.get_plata())
# print("Osnovnata plata na shefot na obezbeduvanje iznesuva:", shef_obezbeduvanje.get_plata())
# print("shefot na obezbeduvanje zema plata od:", shef_obezbeduvanje.get_neto_plata())

print("Bonus za vrab 2:", vrab2.get_bonus())
print("Bonus za shef_obezbeduvanje 1:", shef_obezbeduvanje.get_bonus())