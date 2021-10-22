class Guess:
    """A guess made by the user. The responsibility of Guess is to keep track of the player's last guess.
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess (integer): The number guessed by user.
    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Guess): an instance of Guess.
        """
        self._guess = guess

    def get_guess(self):
        """Returns the user's guess.

        Args:
            self (Guess): an instance of Guess.
        """
        return self._guess
