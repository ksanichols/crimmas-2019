import random

RED   = "\033[1;31m"
GREEN = "\033[1;32m"
DEFAULT_COLOR = "\033[00m"

def get_holiday_color():
    return random.choice([GREEN, RED])

if __name__ == "__main__":
    print(get_holiday_color())
