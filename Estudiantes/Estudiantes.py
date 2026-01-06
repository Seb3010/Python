class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grades(self, grade):
        self.grades.append(grade)

    def get_average(self):
        try:
            return sum(self.grades) / len(self.grades)
        except ZeroDivisionError:
            return 0

    def keep(self):
        with open("reporte.txt", "a") as archivo:
            archivo.write(f"nombre: {self.name} | notas: {self.get_average()}\n")