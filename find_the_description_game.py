from random import choice, randint, sample

from helpers import (
    check_answer,
    print_question,
    print_result,
)


def _validate_input(max_num):
    while True:
        try:
            answer = int(input())
            if answer > max_num:
                raise ValueError
            break
        except ValueError:
            print(
                'Enter number from 1 to {}'.format(max_num))
    return answer


def _get_patterns_for_question(patterns, question_pattern, num_of_answers):
    current_patterns = sample(patterns.keys(), num_of_answers)

    if question_pattern in current_patterns:
        return current_patterns

    current_patterns = current_patterns[:-1]
    current_patterns.insert(randint(0, num_of_answers),
                            question_pattern)
    return current_patterns


def find_the_description(patterns, *, num_of_questions=10, num_of_answers=4):

    question_text = 'What is the description of {} pattern?'
    result = 0
    all_patterns = list(patterns.keys())

    if num_of_questions > len(patterns):
        num_of_questions = len(patterns)

    for i in range(num_of_questions):

        question_pattern = choice(all_patterns)
        all_patterns.remove(question_pattern)
        current_patterns = _get_patterns_for_question(patterns,
                                                      question_pattern,
                                                      num_of_answers)

        print_question(
            i + 1,
            question_text.format(question_pattern),
            [patterns[name]['description'].replace(name, '*' * 5)
             for name in current_patterns]
        )

        answer = _validate_input(len(current_patterns))
        answer = patterns[current_patterns[answer - 1]]

        result += check_answer(answer['description'],
                               patterns[question_pattern]['description'])

    print_result(result, num_of_questions)