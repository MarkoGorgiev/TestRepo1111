# Да се дефинира класа Person со атрибутите name, age.
# Да се дефинира класа Student која ќе ги има атрибутите name, age, grade.
#
# Да напише функција која што ќе ги принта податоците за класата Person.
# Да напише функција која што ќе ги принта податоците за класата Student.


class Person():
    def __init__(self, ime, godini):
        self.name = ime
        self.age = godini

    def __str__(self):
        return f"name: {self.name}; age: {self.age};"


class Student(Person):
    def __init__(self, ime, godini, ocenka):
        super().__init__(ime, godini)
        self.grade = ocenka

    def __str__(self):
        # return f"name: {self.name}, age: {self.age}, grade: {self.grade}"
        return f"{super().__str__()} grade: {self.grade}"


instance_p = Person("Person 1", 100)
print(instance_p)

instance_s = Student("Student 1", 120, 10)
print(instance_s)
