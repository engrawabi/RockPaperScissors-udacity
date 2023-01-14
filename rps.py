from termcolor import colored
import random
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']

"""The Player class is the parent class for all of the Players
in this game"""


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(1)


class Player:
    def move(self):
        Player.my_move = moves
        Player.their_move = random.choice(moves)

    def learn(self, my_move, their_move):
        Player.my_move = my_move
        Player.their_move = their_move


class HumanPlayer():
    def move(self):
        while True:
            rock = colored("Rock ", "red")
            paper = colored("Paper ", "green")
            sc = colored("Scissors ", "red")
            sp = colored("Spock ", "green")
            liz = colored("Lizard, ", "red")
            go = colored(" Go!>  ", "yellow")
            move_human = input(rock + paper + sc + sp + liz + go)
            if move_human.lower() in moves:
                return move_human.lower()
            elif move_human.lower() == 'x':
                exit()

    def learn(self, my_move, their_move):
        pass


class RandomPlayer():
    def move(self):
        random_move = random.randint(0, 4)
        computerMove = moves[random_move]
        return computerMove

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        Player.their_move = None

    def move(self):
        if Player.their_move is None:
            Player.their_move = moves[0]
            return Player.their_move
        else:
            return Player.their_move

    def learn(self, my_move, their_move):
        Player.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        Player.my_move = None

    def move(self):
        if Player.my_move == moves[0]:
            return moves[1]
        elif Player.my_move == moves[1]:
            return moves[2]
        elif Player.my_move == moves[2]:
            return moves[3]
        elif Player.my_move == moves[3]:
            return moves[4]
        else:
            return moves[0]


class RepeatPlayer():
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock') or
                (one == 'rock' and two == 'lizard') or
                (one == 'lizard' and two == 'spock') or
                (one == 'spock' and two == 'scissors') or
                (one == 'scissors' and two == 'lizard') or
                (one == 'lizard' and two == 'paper') or
                (one == 'paper' and two == 'spock') or
                (one == 'spock' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if self.beats(move1, move2):
            self.score_p1 += 1
            winner = colored("** PLAYER ONE WINS **", "green")
        elif self.beats(move2, move1):
            self.score_p2 += 1
            winner = colored("** PLAYER TWO WINS **", "green")
        elif move1 == move2:
            self.score_p1 = self.score_p1
            self.score_p2 = self.score_p2
            winner = colored("** TIE **", "yellow")
        print_pause(colored("You played:" + move1, "blue"))
        print_pause(colored("\nOpponent played:" + move2, "blue"))
        print_pause("\n")
        print_pause(winner)
        playerOne = colored("\nScore: Player One ", "blue")
        playerTwo = colored(" ,Player two ", "blue")
        score_one = playerOne + str(self.score_p1)
        score_two = playerTwo + str(self.score_p2)
        print_pause(score_one + score_two)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print_pause(colored("Game start!\n", "red", attrs=["bold", "blink"]))
        print_pause(colored("To exit of the game enter X\n", "green"))
        print_pause(colored("Rules:\n", "cyan", attrs=["bold", "blink"]))
        print_pause(colored("1-Scissors cuts Paper\n", "blue"))
        print_pause(colored("2-Paper covers Rock\n", "blue"))
        print_pause(colored("3-Rock crushes Lizard\n", "blue"))
        print_pause(colored("4-Lizard poisons Spock\n", "blue"))
        print_pause(colored("5-Spock smashes Scissors\n", "blue"))
        print_pause(colored("6-Scissors decapitates Lizard\n", "blue"))
        print_pause(colored("7-Lizard eats Paper\n", "blue"))
        print_pause(colored("8-Paper disproves Spock\n", "blue"))
        print_pause(colored("9-Spock vaporizes Rock\n", "blue"))
        print_pause(colored("10-Rock crushes Scissors\n", "blue"))
        Gameover = colored('\nGame over!', 'red')
        plyone = colored("Score: Player one ", "cyan")
        plytwo = colored(" Player two  ", "cyan")
        oneplay = plyone + str(self.score_p1)
        twoplay = plytwo + str(self.score_p2)

        for round in range(7):
            round1 = colored("\nRound ", "cyan")
            minus = colored(" --", "cyan")
            print(round1 + str(round)+minus)
            self.play_round()
        if self.score_p1 == self.score_p2:
            print_pause(Gameover)
            print_pause(colored("\n** The game ended in a tie **\n", "cyan"))
            print_pause(oneplay + twoplay)
        elif self.score_p1 > self.score_p2:
            print_pause(Gameover)
            print_pause(colored("\n** Player ONE has won **\n", "cyan"))
            print_pause(oneplay + twoplay)
        else:
            print_pause(Gameover)
            print_pause(colored("\n** Player TWO has won **\n", "cyan"))
            print_pause(oneplay + twoplay)


if __name__ == '__main__':
    random_Move = random.randint(1, 4)
    if random_Move == 1:
        random_Move = RandomPlayer()
    elif random_Move == 2:
        random_Move = ReflectPlayer()
    elif random_Move == 3:
        random_Move = CyclePlayer()
    elif random_Move == 4:
        random_Move = RepeatPlayer()
    game = Game(HumanPlayer(), random_Move)
    game.play_game()
