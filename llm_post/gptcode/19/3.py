def sort_numbers(numbers: str) -> str:
    numberals = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = numbers.split()
    numbers.sort(key=lambda x: numberals.index(x))
    return ' '.join(numbers)