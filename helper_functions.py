from typing import List, Tuple, Iterable, Optional

Board = List[List[str]]
Path = List[Tuple[int, int]]

def possible_moves(move: Tuple[int, int], path: Path, max_location: Tuple[int, int]):
    """ This function returns all the possible and legal moves for a given coordinate """
    legal_move = []
    direction_list = [(1, 0), (0, 1), (-1, 0), (0, -1),
                     (-1, -1), (-1, 1), (1, 1), (1, -1)]
    for possible_move in direction_list:
        if 0 <= possible_move[0] + move[0] < max_location[0] and 0 <= possible_move[1] + move[1] < max_location[1]:
            if (possible_move[0] + move[0], possible_move[1] + move[1]) not in path:
                legal_move.append((possible_move[0] + move[0], possible_move[1] + move[1]))
    return legal_move


def all_possible_moves(move: Tuple[int, int]):
    legal_move = []
    direction_list = [(1, 0), (0, 1), (-1, 0), (0, -1),
                      (-1, -1), (-1, 1), (1, 1), (1, -1)]
    for possible_move in direction_list:
        legal_move.append((possible_move[0] + move[0], possible_move[1] + move[1]))
    return legal_move


def is_word(path, board, words):
    """ This function gets a path and checks if the word formed by the given path forms a word in our dictionary """
    return form_word(path, board) in words


def form_word(path: Path, board: Board):
    """ This function forms the word we want """
    my_word = ""
    for coordinate in path:
        my_word += board[coordinate[0]][coordinate[1]]
    return my_word


def start_coord(board: Board):
    """ THis function returns a list of all coordinates in a board """
    coord_of_all = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            coord_of_all.append((row, col))
    return coord_of_all


def filtered(words: list, string: str):
    """ This function returns a filtered version of words """
    new_words = list(filter(lambda word: word.startswith(string), words))
    return new_words

def remove_word(word_list: list, string: str):
    """ This function returns a list containing only words that are different from the string the function received """
    new_words = list(filter(lambda word: word != string, word_list))
    return new_words


