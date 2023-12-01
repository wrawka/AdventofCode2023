from pathlib import Path

def get_line_value(input: str) -> int:
    """Returns sum the first and last digits in the string."""

    def extract_numbers(input: str) -> list[int]:
        """Extracts all numbers from `input` and returns them in a list (in order)."""
        DIGITS = '0123456789'
        collected_numbers = []

        for simbol in input:
            if simbol in DIGITS:
                collected_numbers.append(simbol)

        return collected_numbers
    
    line_numbers = extract_numbers(input)
    if line_numbers:
        return int(line_numbers[0] + line_numbers[-1])
    return 0
            

if __name__ == '__main__':
    INPUT_PATH = Path(__file__).resolve().parent.joinpath('input.txt')
    
    elf_calibration = 0

    with open(INPUT_PATH, 'r') as file_input:
        for line in file_input:
            elf_calibration += get_line_value(line)
    
    print('Calibration ready: ', elf_calibration)
