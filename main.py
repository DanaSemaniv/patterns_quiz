from find_the_description_game import find_the_description
from helpers import get_patterns


if __name__ == '__main__':
    patterns = get_patterns('patterns.json')
    find_the_description(patterns, num_of_questions=3, num_of_answers=5)
