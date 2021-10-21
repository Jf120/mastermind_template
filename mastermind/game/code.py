import random

class Code:
    
    def __init__(self):
        self._items = {}
    
    def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (code): an instance of Code.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

    def to_string(self):
        
        string = "-------------------- \n"
        
        for name, value in self._items.items():
            string += f"Player {name}: {value[1]}, {value[2]}\n"
        
        string += "-------------------- \n"
        
        return string
    
    def get_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

            Args:
                self (Board): An instance of Board.
                code (string): The code to compare with.
                guess (string): The guess that was made.

            Returns:
                string: A hint in the form [xxxx]
        """
        number = guess.get_guess()
        hint = ""
        for index, letter in enumerate(str(number)):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint
    
    def apply(self, guess, player):
        name = player.get_name()
        number = guess.get_guess()
        values = self._items[name]
        values[1] = number
        values[2] = self.get_hint(values[0], guess)
        self._items[name] = values
    
    def guessed_correctly(self, player):
        name = player.get_name()
        values = self._items[name]
        if values[2] == "xxxx":
            return True 
        else:
            return False 