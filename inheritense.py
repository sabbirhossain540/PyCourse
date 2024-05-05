class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attck with of power {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attcking with of arrows {self.num_arrows}')



wiz = Wizard('ddd', 20)
print(wiz.attack())

arc = Archer('dfd', 500)
print(arc.attack())