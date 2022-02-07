from math import gcd
from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_task_and_solution():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    correct_answer = gcd(number1, number2)
    task = '{0} {1}'.format(number1, number2)

    return task, str(correct_answer)
