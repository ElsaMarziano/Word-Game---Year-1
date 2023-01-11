from helper_functions import *
from boggle_board_randomizer import *

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
    """ This function returns all the paths of size n that form a legal word """
    pass


def find_length_helper(n: int, loc: tuple, list_of_paths: list[tuple], this_path: list, start_board_coords: list[tuple],\
    words: list, filtered_words: list, board):
    """ This function finds all possible combinations of path """
    # Backtracking - check there are words starting with those letters, else return
    filtered_words = filtered(filtered_words, form_word(this_path, board))
    if len(filtered_words) == 0: 
        return list_of_paths
    this_path.append(loc)
    if len(this_path) == n:
        if is_word(this_path, board, words):
            list_of_paths.append(this_path)
            return list_of_paths
        if len(start_board_coords) > 0:
            # Call the function from the the next tuple,start[1:] and start from there
            list_of_paths = find_length_helper(n, start_board_coords[0], list_of_paths, [], start_board_coords[1:], words, words, board)
        else:
            return list_of_paths
        # has the tuple [len[board],len[board[0]]
    else:
        for next_loc in possible_moves(loc, this_path, start_board_coords[-1]):
            list_of_paths = find_length_helper(n, next_loc, list_of_paths, this_path, start_board_coords[1:], \
                words, filtered_words , board)
    return list_of_paths
            

def find_length_n_words(n, board, words):
    """ This function returns all the possible paths for each word in the words dictionary """
    #TODO Add case insensitive ???
    new_words = list(filter(lambda word: len(word) >= n, words))
    return find_length_helper(n, (0, 0), [], [], start_coord(board), new_words, new_words, board)


board = [['QU', 'I', 'T', 'F'], ['S', 'A', 'Y', 'L'], ['E', 'E', 'X', 'L'], ['E', 'H', 'I', 'H']]
print(board)
print(find_length_n_words(2, board , ["SA"] ))

def max_score_paths(board, words):
    """ This function returns the maximal possible score for all the path in the words dictionary """
    pass

    # def find_length_n_paths(n, board, words):
    #     # Function to check if a move is valid
    #     def is_valid_move(x, y, visited):
    #         # check if the current cell is in the board and hasn't been visited before
    #         if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or visited[x][y]:
    #             return False
    #         return True
    #
    #     # Function that does the DFS
    #     def dfs(x, y, visited, word):
    #         # add the current letter to the word and mark the cell as visited
    #         word += board[x][y]
    #         visited[x][y] = True
    #         # if the word has reached the desired length, check if it's a legal word
    #         if len(word) == n:
    #             if word in words:
    #                 legal_paths.append(word)
    #             visited[x][y] = False
    #             return
    #         # check all adjacent cells
    #         for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
    #             new_x, new_y = x + dx, y + dy
    #             if is_valid_move(new_x, new_y, visited):
    #                 dfs(new_x, new_y, visited, word)
    #         # backtrack
    #         visited[x][y] = False
    #
    #     legal_paths = []
    #     visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    #     # starting from every cell on the board
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             dfs(i, j, visited, "")
    #     return legal_paths
