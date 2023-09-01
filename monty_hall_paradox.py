import random
import sys


class MontyHallSimulator:
    ALL_CLOSED = """
    +------+  +------+  +------+
    |      |  |      |  |      |
    |   1  |  |   2  |  |   3  |
    |      |  |      |  |      |
    |      |  |      |  |      |
    |      |  |      |  |      |
    +------+  +------+  +------+"""

    FIRST_GOAT = """
    +------+  +------+  +------+
    |  ((  |  |      |  |      |
    |  oo  |  |   2  |  |   3  |
    | /_/|_|  |      |  |      |
    |    | |  |      |  |      |
    |GOAT|||  |      |  |      |
    +------+  +------+  +------+"""

    SECOND_GOAT = """
    +------+  +------+  +------+
    |      |  |  ((  |  |      |
    |   1  |  |  oo  |  |   3  |
    |      |  | /_/|_|  |      |
    |      |  |    | |  |      |
    |      |  |GOAT|||  |      |
    +------+  +------+  +------+"""

    THIRD_GOAT = """
    +------+  +------+  +------+
    |      |  |      |  |  ((  |
    |   1  |  |   2  |  |  oo  |
    |      |  |      |  | /_/|_|
    |      |  |      |  |    | |
    |      |  |      |  |GOAT|||
    +------+  +------+  +------+"""

    FIRST_CAR_OTHERS_GOAT = """
    +------+  +------+  +------+
    | CAR! |  |  ((  |  |  ((  |
    |    __|  |  oo  |  |  oo  |
    |  _/  |  | /_/|_|  | /_/|_|
    | /_ __|  |    | |  |    | |
    |   O  |  |GOAT|||  |GOAT|||
    +------+  +------+  +------+"""

    SECOND_CAR_OTHERS_GOAT = """
    +------+  +------+  +------+
    |  ((  |  | CAR! |  |  ((  |
    |  oo  |  |    __|  |  oo  |
    | /_/|_|  |  _/  |  | /_/|_|
    |    | |  | /_ __|  |    | |
    |GOAT|||  |   O  |  |GOAT|||
    +------+  +------+  +------+"""

    THIRD_CAR_OTHERS_GOAT = """
    +------+  +------+  +------+
    |  ((  |  |  ((  |  | CAR! |
    |  oo  |  |  oo  |  |    __|
    | /_/|_|  | /_/|_|  |  _/  |
    |    | |  |    | |  | /_ __|
    |GOAT|||  |GOAT|||  |   O  |
    +------+  +------+  +------+"""

    def __init__(self):
        self.swap_wins = 0
        self.swap_losses = 0
        self.stay_wins = 0
        self.stay_losses = 0

    def display_instructions(self):
        print(f'''
Monty Hall Paradox Simulator

In the Monty Hall game show, you can pick one of three doors. One door
has a new car for a prize. The other two doors have worthless goats:
{self.ALL_CLOSED}
Say you pick Door #1.
Before the door you choose is opened, another door with a goat is opened:
{self.THIRD_GOAT}
You can choose to either open the door you originally picked or swap
to the other unopened door.

It may seem like it doesn't matter if you swap or not, but your odds
do improve if you swap doors! This program demonstrates the Monty Hall
problem by letting you do repeated experiments.''')

    def pick_door(self):
        print(self.ALL_CLOSED)
        while True:
            response = input(
                'Pick a door 1, 2, or 3 (or "quit" to stop): ').upper()
            if response == 'QUIT':
                sys.exit()
            if response in {'1', '2', '3'}:
                return int(response)

    def reveal_goat(self, door_pick, door_with_car):
        while True:
            show_goat_door = random.randint(1, 3)
            if show_goat_door != door_pick and show_goat_door != door_with_car:
                return show_goat_door

    def display_game_state(self, show_goat_door, door_with_car):
        doors = [
            self.ALL_CLOSED, self.FIRST_GOAT,
            self.SECOND_GOAT, self.THIRD_GOAT]
        print(doors[show_goat_door])
        print(f'Door {show_goat_door} contains a goat!')
        return doors[door_with_car]

    def simulate_game(self):
        door_with_car = random.randint(1, 3)
        door_pick = self.pick_door()
        show_goat_door = self.reveal_goat(door_pick, door_with_car)

        print(self.display_game_state(show_goat_door, door_with_car))

        swap = input('Do you want to swap doors? Y/N: ').upper()
        if swap == 'Y':
            door_pick = 6 - door_pick - show_goat_door

        self.display_game_state(door_with_car, door_with_car)
        if door_pick == door_with_car:
            print('You won!')
            if swap == 'Y':
                self.swap_wins += 1
            else:
                self.stay_wins += 1
        else:
            print('Sorry, you lost.')
            if swap == 'Y':
                self.swap_losses += 1
            else:
                self.stay_losses += 1

    def display_results(self):
        def success_rate(wins, losses):
            total_attempts = wins + losses
            return round(
                wins / total_attempts * 100, 1) if total_attempts != 0 else 0.0

        print()
        print('Swapping:     ', end='')
        print(f'{self.swap_wins} wins, {self.swap_losses} losses, ', end='')
        print(
            f'success rate {success_rate(self.swap_wins, self.swap_losses)}%')
        print('Not swapping: ', end='')
        print(f'{self.stay_wins} wins, {self.stay_losses} losses, ', end='')
        print(
            f'success rate {success_rate(self.stay_wins, self.stay_losses)}%')
        print()

    def run(self):
        self.display_instructions()
        while True:
            self.simulate_game()
            self.display_results()
            input('Press Enter to repeat the experiment...')


if __name__ == '__main__':
    simulator = MontyHallSimulator()
    simulator.run()
