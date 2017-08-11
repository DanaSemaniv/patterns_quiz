from json import load
from termcolor import colored


def get_patterns(filepath):
    with open(filepath) as file:
        result = load(file)
    return result


def print_question(num, question, answers):
    print(colored('\nQuestion {}:'.format(num), 'green'), question)
    print(colored('\nAnswers:', 'green'))
    for i in range(len(answers)):
        print('{}. {}'.format(i + 1, answers[i]))


def check_answer(actual, supposed):
    if actual == supposed:
        print(colored('Good!', 'green'))
        return True
    else:
        print(colored('Not quite', 'red'))
        print(colored('The right answer is:', 'blue'), supposed)
        return False


def print_result(right_answers, all_answers):
    attrs = ['bold', 'underline']

    print('\nResult: {}/{}'.format(right_answers, all_answers))

    res = right_answers / all_answers

    if res < 0.5:
        print(colored('So bad :(', 'red', attrs=attrs))
    elif res < 0.75:
        print(colored('Not bad!', 'yellow', attrs=attrs))
    elif res < 0.93:
        print(colored('Almost perfect!!', 'cyan', attrs=attrs))
    else:
        print(colored('You did it!!!', 'green', attrs=attrs))


def validate_input(max_num):
    while True:
        try:
            answer = int(input())
            if answer not in range(1, max_num + 1):
                raise ValueError
            break
        except ValueError:
            print(
                'Enter number from 1 to {}'.format(max_num))
    return answer
