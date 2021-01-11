#Jan 12, 0952 version 

import random
import math

#### Othello Shell
#### P. White 2016-2018

EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'

# To refer to neighbor squares we can add a direction to a square.
N,S,E,W = -10, 10, 1, -1
NE, SE, NW, SW = N+E, S+E, N+W, S+W
DIRECTIONS = (N,NE,E,SE,S,SW,W,NW)
PLAYERS = {BLACK: "Black", WHITE: "White"}
NEXT = {BLACK: WHITE, WHITE: BLACK}

########## ########## ########## ########## ########## ##########
# The strategy class for your AI
# You must implement this class
# and the method best_strategy
# Do not tamper with the init method's parameters, or best_strategy's parameters
# But you can change anything inside this you want otherwise
#############################################################

class Strategy():

    def __init__(self):
        pass

    def get_starting_board(self):
        """Create a new board with the initial black and white positions filled."""
        #print("in get starting board method")
        state = OUTER*10 + (OUTER + EMPTY*8 + OUTER)*8 + OUTER*10
        board = list(state)
        board[45], board[54] = BLACK, BLACK
        board[44], board[55] = WHITE, WHITE
        toRet = "".join(board)
        return toRet
	#toRet = "???????????........??........??........??...o@...??...@o...??........??........??........???????????"
	#print(toRet)
	
    def get_pretty_board(self, board):
        """Get a string representation of the board."""
        # print("in get pretty board method")
        # state = list(board)
        # print("before for")
        
        print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" % ( board[:10],board[10:20],board[20:30], board[30:40], board[40:50], board[50:60], board[60:70], board[70:80], board[80:90], board[90:]))
        
        # for i in range(10, len(board) + 1, 10):
        #     state.insert(i, "\n")
        # print("after for")
        # state = "".join(state)
        # print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" % ( state[:10],state[10:20],state[20:30], state[30:40], state[40:50], state[50:60], state[60:70], state[70:80], state[80:90], state[90:]))
        # print("returned")
        return board

    def opponent(self, player):
        """Get player's opponent."""
        pass

    def find_bracket(self, board, player, square, direction):
        """
        Find a square that forms a match with `square` for `player` in the given
        `direction`.  Returns None if no such square exists.

        Assumes that 'square' is a blank. Direction is one of the eight valid
        directions. Return the index of a square in 'player''s color
        so that there is a string of opponent pieces in between.
        """
        pass
    #def is_move_valid(self, board, player, move):
		#"""Is this a legal move for the player?"""
		#pass
    
    def get_valid_moves(self, board, player):
        BLANKS = [i for i in range(len(board)) if board[i] == EMPTY]
        valid_pos = []
        for x in BLANKS:
            if self.check_Adjacencies(board, player, x):
                valid_pos.append(x)
        return valid_pos

    def check_Adjacencies(self, board, player, index):
        for direction in DIRECTIONS:
            curI = direction + index
            if board[curI] == NEXT[player]:
                while board[curI] != EMPTY or board[curI] != OUTER:
                    if board[curI] == EMPTY or board[curI] == OUTER:
                        break
                    if board[curI] == player:
                        return True
                    curI = curI + direction
                    if board[curI] == OUTER:
                        break
        return False

    def has_any_valid_moves(self, board, player):
        """Can player make any moves?"""
        pass

    def make_move(self, board, player, move):
        """Update the board to reflect the move by the specified player."""
        # returns a new board/string
        #return "".join(state)
        #print(direction)
        state = list(board)
        state[move] = str(player)
        for direction in DIRECTIONS:
            boolean = False
            curI = direction + move
            while state[curI] == NEXT[player]:
                #print("Current Index: " + str(curI))
                curI = curI + direction
                if state[curI] == player:
                    boolean = True
                    break
                if state[curI] == OUTER or state[curI] == EMPTY:
                    break
            curI = direction + move
            if boolean:
                while state[curI] == NEXT[player]:
                    state[curI] = player
                    curI = curI + direction
                    if state[curI] == player:
                        break
        toRet = "".join(state)
        return toRet
    
    def next_player(self, board, prev_player):
        """Which player should move next?  Returns None if no legal moves exist."""
        #print("In next player method")
        opp_player = NEXT[prev_player]
        opp_player_moves = self.get_valid_moves(board, opp_player)
        prev_player_moves = self.get_valid_moves(board, prev_player)
        if len(opp_player_moves) == 0:
            if len(prev_player_moves) == 0:
                return None
            else:
                return prev_player
        return opp_player
    def end_score(self, board, player):
        player_pieces = [i for i in range(len(board)) if board[i] == player]
        opponent_pieces = [i for i in range(len(board)) if board[i] == NEXT[player]]
        score = len(player_pieces) - len(opponent_pieces)
        return score

    def score(self, board, player):
        """Compute player's score (number of player's pieces minus opponent's)."""
        p = 0
        c = 0
        l = 0
        m = 0
        
        black_tiles = len([i for i in range(len(board)) if board[i] == BLACK])
        white_tiles = len([i for i in range(len(board)) if board[i] == WHITE])
        if black_tiles > white_tiles:
            p = (100.0 * black_tiles)/(black_tiles + white_tiles)
        elif black_tiles < white_tiles:
            p = -(100.0 * white_tiles)/(black_tiles + white_tiles)
        else:
            p = 0
	
        black_corner = len([i for i in [11, 18, 81, 88] if board[i] == BLACK])
        white_corner = len([i for i in [11, 18, 81, 88] if board[i] == WHITE])
        c = 25 * (black_corner - white_corner)
        
        black_close_corner = 0
        white_close_corner = 0
        if board[11] == EMPTY:
            black_close_corner = black_close_corner + len([i for i in [12, 21, 22] if board[i] == BLACK])
            white_close_corner = white_close_corner + len([i for i in [12, 21, 22] if board[i] == WHITE])
        if board[18] == EMPTY:
            black_close_corner = black_close_corner + len([i for i in [17, 28, 27] if board[i] == BLACK])
            white_close_corner = white_close_corner + len([i for i in [17, 28, 27] if board[i] == WHITE])
        if board[81] == EMPTY:
            black_close_corner = black_close_corner + len([i for i in [71, 82, 72] if board[i] == BLACK])
            white_close_corner = white_close_corner + len([i for i in [71, 82, 72] if board[i] == WHITE])
        if board[88] == EMPTY:
            black_close_corner = black_close_corner + len([i for i in [87, 77, 78] if board[i] == BLACK])
            white_close_corner = white_close_corner + len([i for i in [87, 77, 78] if board[i] == WHITE])       
        l = -12.5 * (black_close_corner - white_close_corner)
        
        
        black_mob = len(self.get_valid_moves(board, BLACK))
        white_mob = len(self.get_valid_moves(board, WHITE))        
        if black_mob > white_mob:
            m = (100.0 * black_mob)/(black_mob + white_mob);
        elif black_mob < white_mob:
            m = -(100.0 * white_mob)/(black_mob + white_mob);
        else:
            m = 0
	      
        score = (10 * p) + (801.724 * c) + (382.026 * l) + (78.922 * m)
        
        # 
        # black_tiles = len([i for i in range(len(board)) if board[i] == BLACK])
        # white_tiles = len([i for i in range(len(board)) if board[i] == WHITE])
        # score = black_tiles - white_tiles
        
        return score

    def game_over(self, board, player):
        """Return true if player and opponent have no valid moves"""
        pass

    ### Monitoring players

    class IllegalMoveError(Exception):
        def __init__(self, player, move, board):
            self.player = player
            self.move = move
            self.board = board

        def __str__(self):
            return '%s cannot move to square %d' % (PLAYERS[self.player], self.move)

    ################ strategies #################

    def minmax_search(self, node, player, depth):
        # determine best move for player recursively
        # it may return a move, or a search node, depending on your design
        # feel free to adjust the parameters
        best = {BLACK:max, WHITE:min}
        board = node[0]
        if depth == 0:
            #print("Depth == 0")
            tup1 = (node[0], node[1], self.score(board, player))
            #node[2] = self.score(board, player)
            return tup1
            
        children = []
        my_moves = self.get_valid_moves(board, player)
        for move in my_moves:
            next_board = self.make_move(board, player, move)
            next_player = self.next_player(next_board, player)
            if next_player == None:
                c = (next_board, move, 1000*self.score(board, player))
                children.append(c)
            else:
                a = (next_board, move, None)
                tup2 = self.minmax_search(a, next_player, depth = depth - 1)
                c = (next_board, move, tup2[2])
                #c = (next_board, move)
                #c[2] = self.minmax_search(c, next_player, depth = depth - 1)[2]
                children.append(c)
        #print("Children: ------------")
        #print(children)
        winner = best[player](children, key = lambda x: x[2]) 
        new_node = (node[0], node[1], winner[2])
        #node[2] = winner[2]
        return winner
        
    def alphabeta(self, node, player, depth, alpha, beta):
        best = {BLACK:max, WHITE:min}
        board = node[0]
        if depth == 0:
            tup1 = (node[0], node[1], self.score(board, player))
            return tup1
        children = []
        my_moves = self.get_valid_moves(board, player)
        for move in my_moves:
            next_board = self.make_move(board, player, move)
            next_player = self.next_player(next_board, player)
            if  next_player == None:
                c = (next_board, move, 1000*self.score(board, player))
                children.append(c)
            else:
                a = (next_board, move, None)
                tup2 = self.alphabeta(a, next_player, depth - 1, alpha, beta)
                c = (next_board, move, tup2[2])
                children.append(c)
            if player == BLACK:
                alpha = max(alpha, c[2])
            elif player == WHITE:
                beta = min(beta, c[2])
            if alpha >= beta:
                break
        winner = best[player](children, key = lambda x: x[2])
        new_node = (node[0], node[1], winner[2])
        return winner
           

    def alphabeta_strategy(self, board, player, depth):
        node = (board, None, None)
        alpha = float('inf') * -1
        beta = float('inf')
        tup = self.alphabeta(node, player, depth, alpha, beta)
        return tup[1]
        
    def minmax_strategy(self, board, player, depth):
        # calls minmax_search
        # feel free to adjust the parameters
        # returns an integer move
        
        #tup, node = (next_board, move, score)
        #print("in minmax strategy board")
        node = (board, None, None)
        tup = self.minmax_search(node, player, depth)
        #print("Returning node" + str(tup))
        return tup[1]
    
    def random_strategy(self, board, player, depth):
        return random.choice(self.get_valid_moves(board, player))

    def best_strategy(self, board, player, best_move, still_running): #change the strategy instead this when uploading to ion
        ## THIS IS the public function you must implement
        ## Run your best search in a loop and update best_move.value
        depth = 1
        while(still_running):
            ## doing random in a loop is pointless but it's just an example
            best_move.value = self.alphabeta_strategy(board, player, depth)
            depth += 1

    standard_strategy = alphabeta_strategy #change standard_strategy whenever i want to play on here
    #standard_strategy = minmax_strategy

###############################################
# The main game-playing code
# You can probably run this without modification
################################################
import time
from multiprocessing import Value, Process
import os, signal
silent = False


#################################################
# StandardPlayer runs a single game
# it calls Strategy.standard_strategy(board, player)
#################################################
class StandardPlayer():
    def __init__(self):
        pass

    def play(self):
        ### create 2 opponent objects and one referee to play the game
        ### these could all be from separate files
        ref = Strategy()
        black = Strategy()
        white = Strategy()
        depth = 5

        print("Playing Standard Game")
        board = ref.get_starting_board()
        player = BLACK
        strategy = {BLACK: black.standard_strategy, WHITE: white.random_strategy}
        print("Pretty Board: " + ref.get_pretty_board(board))

        while player is not None:
        #for x in range(0, 1):
            move = strategy[player](board, player, depth)
            print(move)
            print("Player %s chooses %i" % (player, move))
            board = ref.make_move(board, player, move)
            print(ref.get_pretty_board(board))
            player = ref.next_player(board, player)

        #print("Final Score %i." % ref.score(board), end=" ")
        
        #print("%s wins" % ("Black" if ref.score(board, BLACK)>0 else "White")) #this is the original in file
        print ("%s wins" % ("Black" if ref.end_score(board, BLACK)>0 else "White"))



#################################################
# ParallelPlayer simulated tournament play
# With parallel processes and time limits
# this may not work on Windows, because, Windows is lame
# This calls Strategy.best_strategy(board, player, best_shared, running)
##################################################
class ParallelPlayer():

    def __init__(self, time_limit = 5):
        self.black = Strategy()
        self.white = Strategy()
        self.time_limit = time_limit

    def play(self):
        ref = Strategy()
        print("play")
        board = ref.get_starting_board()
        player = BLACK

        print("Playing Parallel Game")
        strategy = lambda who: self.black.best_strategy if who == BLACK else self.white.best_strategy
        while player is not None:
            best_shared = Value("i", -99)
            best_shared.value = -99
            running = Value("i", 1)

            p = Process(target=strategy(player), args=(board, player, best_shared, running))
            # start the subprocess
            t1 = time.time()
            p.start()
            # run the subprocess for time_limit
            p.join(self.time_limit)
            # warn that we're about to stop and wait
            running.value = 0
            time.sleep(0.01)
            # kill the process
            p.terminate()
            time.sleep(0.01)
            # really REALLY kill the process
            if p.is_alive(): os.kill(p.pid, signal.SIGKILL)
            # see the best move it found
            move = best_shared.value
            if not silent: print("move = %i , time = %4.2f" % (move, time.time() - t1))
            if not silent:print(board, ref.get_valid_moves(board, player))
            # make the move
            board = ref.make_move(board, player, move)
            if not silent: print(ref.get_pretty_board(board))
            player = ref.next_player(board, player)

        #print("Final Score %i." % ref.score(board), end=" ")
        print("%s wins" % ("Black" if ref.score(board) > 0 else "White"))

if __name__ == "__main__":
    # game =  ParallelPlayer(0.1)
    game = StandardPlayer()
    game.play()
