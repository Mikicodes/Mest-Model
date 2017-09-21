import csv


class Person:

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class Eit(Person):
    def __init__(self, name, nationality, fun_fact=" "):
        super().__init__(name, nationality)
        self.fun_fact = fun_fact

    def tell_fun_fact(self, fun_fact='Tech is too great'):
        self.fun_fact = fun_fact
        print(self.fun_fact)


class Fellows(Person):
    def __init__(self, name, nationality, happiness_level=0):
        super().__init__(name, nationality)
        self.happiness_level = happiness_level

    def eat(self):
        self.happinness_level = self.happiness_level + 1

    def teach(self):
        self.happiness_level = self.happiness_level - 1


class School:
    def __init__(self, eit, fellow):
        self.eit = eit
        self.fellow = fellow

    def recruiting(self, eit):

        self.eit = eit
        with open('eits.csv') as file:
            for line in file.readline():
                name,nationality =line.split(",")
                if nationality in ['Nigeria', 'Ghana','Ivory Coast','Kenya','South Africa']:
                    return line
                else:
                    return 'You are not from Mest'

  







