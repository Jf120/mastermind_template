import random

class Code:
    """Keep track of players guesses, codes, and info. 

    Attributes:
        self._items (dict): contains player information.
    """
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Code): an instance of Code.
        """
        self._items = {}
    
    def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Code): an instance of Code.
            player (Player): The player object to get info.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

    def to_string(self):
        """Converts the guesses of each player into a string.
        
        Args:
            self (Code): an instance of Code.
        """
        
        string = "\n"
        string += "-------------------- \n"
        
        for name, value in self._items.items():
            string += f"Player {name}: {value[1]}, {value[2]}\n"
        
        string += "-------------------- \n"
        
        return string
    
    def get_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

            Args:
                self (Board): An instance of Board.
                code (string): The code to compare with.
                guess (Guess): The guess object of each player.

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
        """Saves the guess of each user and gives a hint based on it.
        
        Args:
            self (Code): an instance of Code.
            gues (Guess): The guess object of each player.
            player (Player): An instance of Player, for player information.
        """
        name = player.get_name()
        number = guess.get_guess()
        values = self._items[name]
        values[1] = number
        values[2] = self.get_hint(values[0], guess)
        self._items[name] = values
    
    def guessed_correctly(self, player):
        """Checks if the player guessed the number.
        
        Args:
            self (Code): an instance of Code.
            player (Player): An instance of Player, for player information.
        """
        name = player.get_name()
        values = self._items[name]
        if values[2] == "xxxx":
            return True 
        else:
            return False 