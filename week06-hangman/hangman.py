import random 

class User:
    def __init__(self):
        self.name = None

    def read_user_name(self):
        self.name = input("Username: ")

    def ask_user_play(self):
        letter = input("Guess: ")
        return letter


class Game:
    def __init__(self):
        self.user = User()
        self.secret = None 
        self.wrong = [] 
        self.correct = []

    def set_secret(self):
        words = ['object', 'function', 'inheritance', 'polymorhism',
                'factorial', 'modulus', 'fibonacci', 'compiler', 
                'debugger', 'computer', 'quantum', 'intelligence']
        self.secret = random.choice(words)

    def play(self, letter):
        if letter in self.secret:
            if letter not in self.correct:
                self.correct.append(letter)
        else: 
            if letter not in self.wrong:
                self.wrong.append(letter)

    def is_hanged(self):
        return len(self.wrong) == 6
    
    def secret_found(self):
        for ch in self.secret[1:-1]:
            if ch not in self.correct:
                return False
        return True
    
    def get_secret_to_display(self):
        display = self.secret[0]
        for ch in self.secret[1:-1]:
            if ch in self.correct:
                display += ch 
            else:
                display += '_'
        display += self.secret[-1]
        return display
    
    def get_wrong_num(self):
        return len(self.wrong)

        