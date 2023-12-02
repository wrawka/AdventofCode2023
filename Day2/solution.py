from pathlib import Path


class Game:
    """A single game with the stupid elf bag."""

    MAX_REDS = 12
    MAX_GREENS = 13
    MAX_BLUES = 14

    def __init__(self, input: str) -> None:
        self.game_number = self._get_game_number(input)
        self.__cubes_sets = self._get_cubes_sets(input)
        self.__max_cubes_count_by_colour = {'red': 0, 'green': 0, 'blue': 0}

    @staticmethod
    def _get_game_number(input: str) -> int:
        """Parses game number from game input string."""
        return int(input.split(':')[0].split()[1])

    @staticmethod
    def _get_cubes_sets(input: str) -> list[str]:
        """Isolates cubes sets from game input, as strings."""
        return input.split(':')[1].split(';')

    def count_cubes(self) -> None:
        """Counts cubes by colour."""
        for cubes_set in self.__cubes_sets:
            for cubes in cubes_set.split(','):
                [count, colour] = cubes.split()
                self.__max_cubes_count_by_colour[colour] = max(int(count), self.__max_cubes_count_by_colour[colour])

    @property
    def red_count(self):
        return self.__max_cubes_count_by_colour['red']

    @property
    def green_count(self):
        return self.__max_cubes_count_by_colour['green']

    @property
    def blue_count(self):
        return self.__max_cubes_count_by_colour['blue']

    def is_valid(self, max_reds: int = MAX_REDS, max_greens: int = MAX_GREENS, max_blues: int = MAX_BLUES):
        return self.red_count <= max_reds and self.green_count <= max_greens and self.blue_count <= max_blues


if __name__ == '__main__':
    TEST_INPUT_PATH = Path(__file__).resolve().parent.joinpath('test_input.txt')
    TEST_ANSWER = 8
    INPUT_PATH = Path(__file__).resolve().parent.joinpath('input.txt')

    sum_of_ids = 0

    ids = []

    with open(INPUT_PATH) as input_file:
        for game_input in input_file:
            new_game = Game(game_input)
            new_game.count_cubes()
            if new_game.is_valid():
                ids.append(new_game.game_number)
                sum_of_ids += new_game.game_number

    # assert sum_of_ids == TEST_ANSWER, f'{sum_of_ids} is not {TEST_ANSWER}'

    print(sum_of_ids)
    print(ids)
