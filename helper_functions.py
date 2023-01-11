def possible_moves(move, path, max_location):
    """ This function returns all the possible and legal moves for a given coordinate """
    legal_move = []
    direction_list = [(1, 0), (0, 1), (-1, 0), (0, -1),
                     (-1, -1), (-1, 1), (1, 1), (1, -1)]
    for possible_move in direction_list:
        if 0 <= possible_move[0] + move[0] < max_location[0] and 0 <= possible_move[1] + move[1] < max_location[1]:
            if (possible_move[0] + move[0], possible_move[1] + move[1]) not in path:
                legal_move.append((possible_move[0] + move[0], possible_move[1] + move[1]))
    return legal_move


def is_word(path):
    return True


def start_coord(board):
    """ THis function returns a list of all coordinates in a board """
    coord_of_all = []
    for i in range(len(board)):
        for j in range(board[0]):
            coord_of_all.append(i,j)
    return coord_of_all