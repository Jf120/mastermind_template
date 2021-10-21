class Player:
    
    """A person taking part in a game. The responsibility of Player is to keep track of their identity and last guess.
    
    Stereotype: 
        Information Holder

    Attributes:
    
    """
    
    def __init__(self, name):
        self._guess = None
        self._name = name
    
    def get_guess(self):
        """Returns the player's last number guesses (an instance of Guess). If the player 
        hasn't guessed yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self._guess

    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._name

    def set_guess(self, guess):
        """Sets the player's last move to the given instance of Guess.

        Args:
            self (Player): an instance of Player.
            move (Guess): an instance of Guess
        """
        self._guess = guess