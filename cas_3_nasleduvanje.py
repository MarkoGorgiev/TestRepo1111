
# class A():
#     def __init__(self):
#         print("Kreiranje na instanca od klasa A")
#         self.att_a = 10


# a = A()  # "Kreiranje na instanca od klasa A"
# print("Pristap do atributot att_a preku instancata a", a.att_a)

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Kreiranje na instanca od klasa B")
#         self.att_b = 20

# b = B()
# print("Pristap do atributot att_b preku instancata b", b.att_b)
# print("Pristap do atributot att_a preku instancata b", b.att_a)

# class C(B):
#     def __init__(self):
#         super().__init__()
#         self.att_c = 30
#         print("Kreiranje na instanca od klasa C")
#
# c = C()
# Kreiranje na instanca od klasa A
# Kreiranje na instanca od klasa B
# Kreiranje na instanca od klasa C




class A():
    def __init__(self, a):
        print("Kreiranje na instanca od klasa A")
        self.att_a = a


class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        print("Kreiranje na instanca od klasa B")
        self.att_b = b


# instance_a = A(10)
# print(instance_a.att_a)

instance_b = B(10, 20)
print("instance_b.att_b", instance_b.att_b)
print("instance_b.att_b", instance_b.att_a)














