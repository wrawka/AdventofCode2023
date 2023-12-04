from pathlib import Path


class ScratchCard:
    """Scratch card in all it's glory."""

    def __init__(self, card: str) -> None:
        self.card = card

    @property
    def value(self):
        value = 0
        [winning, current] = self.card[self.card.find(':') + 1:].split('|')
        for number in winning.split():
            if number in current.split():
                value = value * 2 if value else 1
        return value


if __name__ == '__main__':
    TEST_INPUT_PATH = Path(__file__).resolve().parent.joinpath('test_input.txt')
    TEST_ANSWER = 13
    INPUT_PATH = Path(__file__).resolve().parent.joinpath('input.txt')

    with open(INPUT_PATH) as input_file:
        total = 0
        for card in input_file:
            scratch_card = ScratchCard(card)
            total += scratch_card.value

        print(total)
