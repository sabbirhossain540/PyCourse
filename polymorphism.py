class User():

    def __init__(self, email):
        self.email = email


    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
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



# wiz = Wizard('ddd', 20, 'ssss@fff.com')
# arc = Archer('dfd', 500)

# print(wiz.email)

# for char in [wiz, arc]:
#     char.attack()

# def player_attack(char):
#     char.attack()
#
#player_attack(wiz)

class HybridPoly(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, arrows)
        Archer.__init__(self, name, arrows)



hb1 = HybridPoly('dssd', 30, "SFDSD", "dsd#fff")
print(hb1.num_arrows)
