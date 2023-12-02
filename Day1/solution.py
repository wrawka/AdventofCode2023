from pathlib import Path

DIGITS = '0123456789'

WORDY_DIGITS = ['one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight', 'nine']


def extract_numbers(input: str) -> list[int]:
    """Extracts all numbers from `input` and returns them inside a list (in order)."""
    collected_numbers = []

    for simbol in input:
        if simbol in DIGITS:
            collected_numbers.append(simbol)

    return collected_numbers


def get_line_value(input: str) -> int:
    """Returns sum the first and last digits in the string."""

    line_numbers = extract_numbers(input)
    if line_numbers:
        return int(line_numbers[0] + line_numbers[-1])
    return 0


def extract_tricky_numbers(input: str) -> dict[int: str]:
    """
    Extract digits and word-y digits from `input` and returns them inside a map,
    where key is item index in the `input` sequence.
    """

    collected_numbers = dict()

    for idx, simbol in enumerate(input):
        if simbol in DIGITS:
            collected_numbers.update({idx: simbol})
    for wordy_digit in WORDY_DIGITS:
        idx = input.find(wordy_digit)
        offset = 0
        while idx != -1:
            collected_numbers.update(
                {idx + offset: str(WORDY_DIGITS.index(wordy_digit) + 1)})
            offset += idx + len(wordy_digit)
            input_slice = input[offset:]
            idx = input_slice.find(wordy_digit)

    return collected_numbers


def get_better_line_value(input: str) -> int:
    """Returns sum the first and last digits in the string (with a twist)."""

    line_numbers = extract_tricky_numbers(input)
    first = min(line_numbers.keys())
    last = max(line_numbers.keys())
    if line_numbers:
        return int(line_numbers[first] + line_numbers[last])
    return 0


if __name__ == '__main__':
    INPUT_PATH = Path(__file__).resolve().parent.joinpath('input.txt')

    elf_calibration = 0

    with open(INPUT_PATH, 'r') as file_input:
        for line in file_input:
            elf_calibration += get_better_line_value(line)

    print('Calibration ready: ', elf_calibration)
