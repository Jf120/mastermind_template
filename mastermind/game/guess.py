class Guess:
    """A maneuver in the game. The responsibility of Move is to keep track of the player's last guess.
    
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
