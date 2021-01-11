# Othello-AI

This project uses the minimax algorithm along with alpha beta pruning and tested, complex heuristics to develop an efficient Othello game AI.

## Usage

Download the file strategy.py and simply run the code on your local machine. The output will be a step-by-step walkthrough of an othello game.
The option to play against the AI I developed will be added shortly as well as the development of other AIs using other heuristics.

## Algorithm Overview

The minimax algorithm essentially a recursive algorithm for choosing the next move. At each turn, a game tree (depicted by game states as nodes 
and valid moves as edges) is created up until a certain depth that is user-specified. Values are calculated for each leaf using the score function
detailed down below and the algorithm backtracks to select the best move for the current player. The alpha beta pruning optimizes the algorithm by 
cutting off branches of the game tree that do not need to be explored since they have been shown to always result in a worse case.

## Heuristics and Scoring

As mentioned earlier, the minimax algorithm uses a scoring function to calculate a score for a particular game state (board and player). This function calculates
corner heuristics, close corner values, mobility, and total pieces using a weight vector to assign levels of importance to each of these values.

## Further Developments

In addition to the strategy and heuristics already coded, I would like to extend the algorithm by 
- conducting tests and analysis to determine the best depth values of a game tree for accuracy and efficiency
- using other heuristics such as stability
- employing iterative deepening as well as a shallow search for quick solutions
