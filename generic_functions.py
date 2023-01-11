from typing import Tuple

from helper_functions import *
from boggle_board_randomizer import *
import copy

""" This file will contain the four functions we have to write according to the exercise's pdf """


def is_valid_path(board, path, words):
    """ This function receives a board, a path and a list of words, check if the path is legal and
    if so, returns the word we formed, if it exists in the words dictionary """
    word = ""
    for step in range(len(path)):
        if step == len(path) -1:
            if word in words:
                return word
            return
        if path[step +1] not in possible_moves(step,path[:step+1],(len(board) - 1,len(board[0]) - 1)):
            return
        else:
            word += str(board[path[0][path[1]]])
    return word





    pass


def find_length_n_paths(n, board, words):
    # TODO Add case insensitive ???
    new_words = list(filter(lambda word: len(word) >= n, words))
    return find_length_helper(n, (0, 0), [], [], start_coord(board)[1:], new_words, new_words, board)
    """ This function returns all the paths of size n that form a legal word """

def find_length_helper(n: int, loc: tuple, list_of_paths: List[Tuple[int, int]], this_path: list, start_board_coords: List[Tuple[int, int]],
    words: list, filtered_words: list, board):
    """ This function finds all possible combinations of path """
    # Backtracking - check there are words starting with those letters, else return
    this_path.append(loc)
    filtered_words = filtered(filtered_words, form_word(this_path, board))
    if len(filtered_words) == 0: 
        if len(this_path) == 1 and not is_word(this_path,board,words):
            if len(start_board_coords) == 0:
                return list_of_paths
            return find_length_helper(n, start_board_coords[0], list_of_paths, [], start_board_coords[1:], words, words, board)
        else:
            return list_of_paths

    if len(this_path) == n:
        if is_word(this_path, board, words):
            list_of_paths.append(copy.deepcopy(this_path))
        return list_of_paths

    else:
        # has the tuple [len[board],len[board[0]]
        for next_loc in possible_moves(loc, this_path, start_board_coords[-1]):
            list_of_paths = find_length_helper(n, next_loc, list_of_paths, this_path, start_board_coords, words, filtered_words, board)
            this_path.pop()

        list_of_paths = find_length_helper(n, start_board_coords[0], list_of_paths, [], start_board_coords[1:], words, words, board)

    return list_of_paths
            


def find_length_n_words(n, board, words):
    """
    This function returns all the possible paths for each word in the words dictionary
    """
    #TODO Add case insensitive
    new_words = list(filter(lambda word: len(word) >= n, words)) # > instad of =>
    return find_length_helper_n(n, (0, 0), [], [], start_coord(board)[1:], new_words, new_words, board)




def find_length_helper_n(n, loc, list_of_paths, this_path, start_board_coords, words, filtered_words, board):
    """
    This function finds all possible combinations of path
    """

    this_path.append(loc)
    filtered_words = filtered(filtered_words, form_word(this_path, board))
    if len(filtered_words) == 0:
        if len(this_path) == 1 and not is_word(this_path, board, words) :
            if len(start_board_coords) == 0:
                return list_of_paths
            return find_length_helper_n(n, start_board_coords[0], list_of_paths, [], start_board_coords[1:], words, words,
                                      board)
        else:
            return list_of_paths

    if len(form_word(this_path,board)) == n:
        if is_word(this_path, board, words):
            list_of_paths.append(copy.deepcopy(this_path))
        return list_of_paths

    else:
        # has the tuple [len[board],len[board[0]]
        for next_loc in possible_moves(loc, this_path, start_board_coords[-1]):
            list_of_paths = find_length_helper_n(n, next_loc, list_of_paths, this_path, start_board_coords, words,
                                               filtered_words, board)
            this_path.pop()
        list_of_paths = find_length_helper_n(n, start_board_coords[0], list_of_paths, [], start_board_coords[1:], words,
                                         words, board)


    return list_of_paths

board = [['S', 'I', 'T', 'F'], \
        ['S', 'A', 'Y', 'L'], \
        ['EA', 'E', 'X', 'L'], \
        ['E', 'H', 'I', 'H']]

words = ["EA", "SA", "SASS", "XL"]

print(find_length_n_paths(2, board , words))
print(find_length_n_words(2, board , words))







def max_score_paths(board, words):
    """ This function returns the maximal possible score for all the path in the words dictionary """
    pass

