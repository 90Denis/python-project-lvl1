from random import randint, choice


GAME_RULE = 'What number is missing in the progression?'


def get_task_and_solution():
    start, end, step = randint(0, 20), randint(40, 60), randint(2, 5)
    sequence = list(range(start, end, step))

    correct_answer = choice(sequence)
    task = ' '.join(
        '..' if number == correct_answer else str(number) for number in sequence    
    )

    return task, str(correct_answer)
