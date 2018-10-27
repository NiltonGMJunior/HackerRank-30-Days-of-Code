class Person(object):
    def __init__(self, initialAge = 0):
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
            self.age = 0
        else:
            self.age = initialAge
    def yearPasses(self, years = 1):
        self.age += years
    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

if __name__ == '__main__':

    t = int(input())
    for i in range(0, t):
        age = int(input())
        p = Person(age)
        p.amIOld()
        for j in range(0, 3):
            p.yearPasses()
        p.amIOld()
        print("")
