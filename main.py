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

    def speak(self, myList, a):
        outputList = []
        for item in myList:
            res = item * a
            outputList.append(res)
        
        print(outputList)

player1 = PlayerCharecters("Sabbir", 22)
player2 = PlayerCharecters('sakil', 25)
player1.speak([1,2,3, 434], 5)


