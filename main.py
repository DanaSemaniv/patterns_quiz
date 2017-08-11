from config import games
from helpers import get_patterns, validate_input


def print_games(games):
    print('\nEnter the number of game you want to play:\n')

    for game in games:
        print('Game {}. {}\n'.format(game, games[game].__name__.capitalize()))

if __name__ == '__main__':
    patterns = get_patterns('patterns.json')

    print_games(games)
    game = validate_input(len(games))

    games[game](patterns)
