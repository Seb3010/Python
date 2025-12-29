class signature:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def status(self):
        if self.grade >= 60:
            return "Aprobado"
        else:
            return "Reprobado"

    def average(self):
        return sum(grades) / len(signatures)
