def print_board(board):
    for row in board:
        print("|".join(row))
    print(" 1 2 3 4 5 6 7")


def is_valid_move(board, column):
    return board[0][column] == ' '


def make_move(board, column, player):
    for row in range(5, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = player
            break


def check_winner(board, player):
    # Check horizontally
    for row in range(6):
        for col in range(4):
            if (
                board[row][col] == player
                and board[row][col + 1] == player
                and board[row][col + 2] == player
                and board[row][col + 3] == player
            ):
                return True

    # Check vertically
    for row in range(3):
        for col in range(7):
            if (
                board[row][col] == player
                and board[row + 1][col] == player
                and board[row + 2][col] == player
                and board[row + 3][col] == player
            ):
                return True

    # Check positively sloped diagonals
    for row in range(3):
        for col in range(4):
            if (
                board[row][col] == player
                and board[row + 1][col + 1] == player
                and board[row + 2][col + 2] == player
                and board[row + 3][col + 3] == player
            ):
                return True

    # Check negatively sloped diagonals
    for row in range(3):
        for col in range(3, 7):
            if (
                board[row][col] == player
                and board[row + 1][col - 1] == player
                and board[row + 2][col - 2] == player
                and board[row + 3][col - 3] == player
            ):
                return True

    return False


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def get_human_move(board, player):
    while True:
        try:
            print_board(board)
            column = int(input(f"Player {player}, choose a column (1-7): ")) - 1
            if not (0 <= column < 7) or not is_valid_move(board, column):
                print("Invalid move. Try again.")
            else:
                return column
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_computer_move(board, computer_player):
    best_score = float('-inf')
    best_move = None

    for col in range(7):
        if is_valid_move(board, col):
            make_move(board, col, computer_player)

            score = minimax(board, 4, False, computer_player)
            undo_move(board, col)

            if score > best_score:
                best_score = score
                best_move = col

    return best_move



def minimax(board, depth, maximizing_player, computer_player):
    if depth == 0 or check_winner(board, 'X') or check_winner(board, 'O') or is_board_full(board):
        return evaluate(board, computer_player)

    if maximizing_player:
        max_eval = float('-inf')
        for col in range(7):
            if is_valid_move(board, col):
                # row = get_next_open_row(board, col)
                make_move(board, col, computer_player)
                eval = minimax(board, depth - 1, not maximizing_player, computer_player)
                undo_move(board, col)
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for col in range(7):
            if is_valid_move(board, col):
                opponent_player = 'O' if computer_player == 'X' else 'X'
                make_move(board, col, opponent_player)
                eval = minimax(board, depth - 1, not maximizing_player, computer_player)
                undo_move(board, col)
                min_eval = min(min_eval, eval)
        return min_eval


def undo_move(board, col):
    for row in range(6):
        if board[row][col] != ' ':
            board[row][col] = ' '
            break


def evaluate(board, computer_player):
    if check_winner(board, computer_player):
        return 100
    elif check_winner(board, 'X' if computer_player == 'O' else 'O'):
        return -100
    else:
        return 0


def connect_four():
    board = [[' ' for _ in range(7)] for _ in range(6)]

    human_player = input("Choose your color (X or O): ").upper()
    computer_player = 'X' if human_player == 'O' else 'O'

    while True:
        # Human player's turn
        player_move = get_human_move(board, human_player)
        make_move(board, player_move, human_player)

        if check_winner(board, human_player):
            print(f"Player {human_player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        player_move = get_computer_move(board, computer_player)
        make_move(board, player_move, computer_player)


        if check_winner(board, computer_player):
            print(f"Player {computer_player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break
    print_board(board)


if __name__ == "__main__":
    connect_four()






