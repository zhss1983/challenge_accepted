import getch


def get_numbers(stop_chars: str = ""):
    """Генериркет список чисел вводимых с клавиатуры в реальном времени."""
    while True:
        char = getch.getch()
        if char in stop_chars:
            return
        if char in "0123456789":
            yield int(char)
        if char == "\n":
            yield char
