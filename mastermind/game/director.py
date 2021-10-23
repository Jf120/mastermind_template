from game.console import Console
from game.player import Player
from game.roster import Roster
from game.code import Code
from game.guess import Guess

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._console = Console()
        self._keep_playing = True
        self._roster = Roster()
        self._code = Code()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
            self._code.prepare(player)
        self._console.write(
"""\nRules of the game:
1. A code is randomly generated for each player. Ex: '1a3g'
2. On your turn, enter a guess into the console.
3. First player to correctly guess their code wins.
"""
        )
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the guess from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # display the players and guesses
        guesses = self._code.to_string()
        self._console.write(guesses)
        # gets next player's guess
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn: ")
        user_code = self._console.read("What is your guess? ")
        guess = Guess(user_code)
        player.set_guess(guess)
        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating hints with the current guess.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        guess = player.get_guess()
        self._code.apply(guess, player)

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if any player was able to guess the number.

        Args:
            self (Director): An instance of Director.
        """
        if self._code.guessed_correctly(self._roster.get_current()):
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\nCongrats {name}! You won fair and square!")
            self._keep_playing = False
        self._roster.next_player()

