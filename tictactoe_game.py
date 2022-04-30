'''
Name : Tic-Tac-Toe
Objective Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, 
          a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.
Author: Peter Babcock
Class: CSE 210 Spring 2022
'''
import os

def main():

  clear_screen()
  board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  we_have_a_winner = False
  players_symbol = ["x", "o"]
  player = 0

  while count_spaces(board) and not we_have_a_winner:
      clear_screen()
      print_board(board)
      #board = players_selections(player,board,players_symbol)
      players_selections(player,board,players_symbol)
      we_have_a_winner = check_result(board,players_symbol)
      if we_have_a_winner is True:
        exit()
      count_spaces(board)
      player = int(not player)
  if check_result(board,players_symbol) is False:
    print()
    print("WE HAVE A DRAW")
    print()
    print("Your both Champs, Play again to see if you can get a winner!")

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def count_spaces(board):
  spaces_filled = board.count("x") + board.count("o")
  if spaces_filled != 9:
      return True
  else:
      return False

def check_result(board,players_symbol):
  winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
  for check in winning_positions:
      win_symbol = board[check[0]]
      if win_symbol != " ":
          won = True
          for point in check:
              if board[point] != win_symbol:
                  won = False
                  break
          if won:
              we_have_a_winner = True
              print()
              print("WE HAVE A WINNER")
              if win_symbol == players_symbol[0]:
                print("Well Done player 1 you are our champ") 
              else:
                print("Well Done player 2 you are our champ") 
              print()
              return we_have_a_winner
      else:
          won = False
  return won


def print_board(board):
  print(board[0], "|", board[1], "|", board[2])
  print("--*---*---")
  print(board[3], "|", board[4], "|", board[5])
  print("--*---*---")
  print(board[6], "|", board[7], "|", board[8])


def players_selections(player,board,players_symbol):
  correct_input = True
  player_to_play = player + 1
  pos_selection = input(f"Player {player_to_play} please make your selections [1-9] : ")
  if not pos_selection.isnumeric() or pos_selection == "" or int(pos_selection) > 9 or int(pos_selection) < 1:
      clear_screen()
      print("Thats was an incorrect selections")
      print_board(board)
      players_selections(player,board,players_symbol)
  else:
      block_position = int(pos_selection) - 1
      if board[block_position] == "x" or board[block_position] == "o":
        clear_screen()
        print("The block you try to select has been taken, Please try again")
        print()
        print_board(board)
        players_selections(player,board,players_symbol)
      else:
        board[block_position] = players_symbol[player]


if __name__ == "__main__":
    main()