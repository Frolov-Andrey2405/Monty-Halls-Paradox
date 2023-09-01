# Monty Hall Paradox Simulator

The Monty Hall paradox (or problem) illustrates an unexpected fact from probability theory and is related to the television game Let's Make a Deal and its host Monty Hall. In this task, the player is asked to choose one of three doors. Behind one of the doors is a prize, a new car, and behind the other two doors are goats.

Let the player choose door number 1. Before opening the selected door, the host opens one of the two remaining doors, behind which there is a goat. The player now has two choices: either he opens the door he originally chose, or he changes his choice and opens the other door.

At first glance, it may seem that the probabilities of winning do not depend on the choice, and the odds are equal. However, in fact, if the player changes his choice and chooses a different door, his chances of winning increase.

This paradox demonstrates that in probability theory, intuition can be misleading. The program presented here allows us to run several experiments to verify this effect.

## How to Use

1. Run the program in a compatible environment.
2. Follow the on-screen prompts to set up and conduct experiments.
3. Observe the outcomes and see how switching or sticking affects your chances of winning.

## Features

- Explore the Monty Hall Paradox and its counterintuitive probability effect.
- Conduct experiments to better understand the paradox and its variants.
- Visualize the impact of switching or sticking with your initial choice.

## Instructions

1. Open a terminal or command prompt.
2. Navigate to the program's directory.
3. Run the program using `python monty_hall_paradox.py`.
4. Follow the program's prompts to set up and conduct experiments.
5. Observe the results and see how your choices affect your chances of winning.

## Sample Output

```

    +------+  +------+  +------+
    |      |  |      |  |      |
    |   1  |  |   2  |  |   3  |
    |      |  |      |  |      |
    |      |  |      |  |      |
    |      |  |      |  |      |
    +------+  +------+  +------+

    +------+  +------+  +------+
    |  ((  |  |      |  |      |
    |  oo  |  |   2  |  |   3  |
    | /_/|_|  |      |  |      |
    |    | |  |      |  |      |
    |GOAT|||  |      |  |      |
    +------+  +------+  +------+

    +------+  +------+  +------+
    |      |  |  ((  |  |      |
    |   1  |  |  oo  |  |   3  |
    |      |  | /_/|_|  |      |
    |      |  |    | |  |      |
    |      |  |GOAT|||  |      |
    +------+  +------+  +------+

    +------+  +------+  +------+
    |      |  |      |  |  ((  |
    |   1  |  |   2  |  |  oo  |
    |      |  |      |  | /_/|_|
    |      |  |      |  |    | |
    |      |  |      |  |GOAT|||
    +------+  +------+  +------+

    +------+  +------+  +------+
    | CAR! |  |  ((  |  |  ((  |
    |    __|  |  oo  |  |  oo  |
    |  _/  |  | /_/|_|  | /_/|_|
    | /_ __|  |    | |  |    | |
    |   O  |  |GOAT|||  |GOAT|||
    +------+  +------+  +------+

    +------+  +------+  +------+
    |  ((  |  | CAR! |  |  ((  |
    |  oo  |  |    __|  |  oo  |
    | /_/|_|  |  _/  |  | /_/|_|
    |    | |  | /_ __|  |    | |
    |GOAT|||  |   O  |  |GOAT|||
    +------+  +------+  +------+

    +------+  +------+  +------+
    |  ((  |  |  ((  |  | CAR! |
    |  oo  |  |  oo  |  |    __|
    | /_/|_|  | /_/|_|  |  _/  |
    |    | |  |    | |  | /_ __|
    |GOAT|||  |GOAT|||  |   O  |
    +------+  +------+  +------+
```

## Note

The Monty Hall Paradox Simulator offers an interactive way to grasp the intriguing world of probability. Experiment and see firsthand how changing your choice can dramatically impact your odds of winning the car.

*For a deeper understanding of this paradox and its variations, read the detailed article on [Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem).*
