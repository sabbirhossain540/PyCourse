#OOP
class PlayerCharecters:
    membership = True
    def __init__(self, name, age):
        if (age > 18):
            self._name = name
            self._age = age
    
    def shout(self):
        print(f'my name is {self.name}')

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name} and age is {self._age}')

player1 = PlayerCharecters("Sabbir", 22)
player2 = PlayerCharecters('sakil', 25)
player1.speak()


