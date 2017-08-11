from config import games
from helpers import get_patterns, validate_input


def print_games(games):
    print('\nEnter the number of game you want to play:\n')

    for game_num, game in enumerate(games):
        print('Game {}. {}\n'.format(game_num + 1,
                                     game.__name__.capitalize()))

    print('{}. Exit game'.format(len(games) + 1))

if __name__ == '__main__':
    patterns = get_patterns('patterns.json')

    games_num = len(games) + 1

    while True:
        print_games(games)
        game = validate_input(games_num)
        if game == games_num:
            break
        games[game - 1](patterns)
