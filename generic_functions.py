""" This file will contain the four functions we have to write according to the exercise's pdf """

def possible_move(move,board):
    legal_move = []
    dirction_list = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]
    for possible_move in dirction_list:
        if 0 <= possible_move[0] + move[0] < len(board) and 0 <= possible_move[1] + move[1] <len(board[0]):
            legal_move.append(move)
    return legal_move

def start_board_coords(board):
    """give all the locations in board"""
    coord_of_all = []
    for i in range(len(board)):
        for j in range(board[0]):
            coord_of_all.append(i,j)
    return coord_of_all

def is_valid_path(board, path, words):
    """ This function receives a board, a path and a list of words, check if the path is legal and
    if so, returns the word we formed, if it exists in the words dictionary """

    pass 

def find_length_n_paths(n, board, words):
    """ This function returns all the paths of size n that form a legal word """
    pass

def find_length_helper(n,loc,list_of_paths,this_path,start_board_coords,words):
    this_path.append(loc)
    if len(this_path) == n:
        if is_word(this_path):
            list_of_paths.append(this_path)
            return list_of_paths
            if len(start_board_coords) > 0:
                list_of_paths = find_length_helper(n, start_board_coords[0] , list_of_paths, [],/
                                        start_board_coords[1:], words)
            else:
                return list_of_paths
            for next_loc in possiable_location(loc,this_path,board,start_board_coords[-1]) # has the tuple [len[board],len[board[0]]
                list_of_paths = find_length_helper(n, next_loc, list_of_paths, [],/
                                start_board_coords[1:], words)









def find_length_n_words(n, board, words):
    """ This function returns all the possible paths for each word in the words dictionary """
    pass
    
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
