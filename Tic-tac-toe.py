import turtle

# ----- Setup Window -----
wn = turtle.Screen()
wn.title("Tic-Tac-Toe Human vs Human")
wn.setup(width=600, height=700)
wn.tracer(0)

# ----- Draw Board -----
board_drawer = turtle.Turtle()
board_drawer.hideturtle()
board_drawer.pensize(5)

def draw_board():
    board_drawer.clear()
    # Grid lines
    for x in [-100, 100]:
        board_drawer.penup()
        board_drawer.goto(x, 250)
        board_drawer.pendown()
        board_drawer.goto(x, -350)
    for y in [50, -150]:
        board_drawer.penup()
        board_drawer.goto(-300, y)
        board_drawer.pendown()
        board_drawer.goto(300, y)

draw_board()

# ----- Game State -----
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

# ----- Drawers -----
pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(3)
writer = turtle.Turtle()
writer.hideturtle()
writer.color("red")
turn_indicator = turtle.Turtle()
turn_indicator.hideturtle()

# ----- Draw X / O -----
def draw_x(x, y):
    pen.penup()
    pen.goto(x - 60, y - 60)
    pen.pendown()
    pen.goto(x + 60, y + 60)
    pen.penup()
    pen.goto(x - 60, y + 60)
    pen.pendown()
    pen.goto(x + 60, y - 60)

def draw_o(x, y):
    pen.penup()
    pen.goto(x, y - 70)
    pen.pendown()
    pen.circle(70)

def show_message(message):
    writer.clear()
    writer.penup()
    writer.goto(0, 100)
    writer.write(message, align="center", font=("Arial", 28, "bold"))

def update_turn_indicator():
    turn_indicator.clear()
    turn_indicator.penup()
    turn_indicator.goto(0, 270)
    turn_indicator.write(f"Turn: {current_player}", align="center", font=("Arial", 20, "bold"))

update_turn_indicator()  # initial display

# ----- Game Logic -----
def check_winner():
    global game_over
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            game_over = True
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            game_over = True
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        game_over = True
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        game_over = True
        return board[0][2]
    if all(board[i][j] != "" for i in range(3) for j in range(3)):
        game_over = True
        return "Draw"
    return None

def display_winner(winner):
    if winner == "Draw":
        show_message("It's a Draw! Press R")
    else:
        show_message(f"Winner: {winner}! Press R")

# ----- Human Click -----
def click_handler(x, y):
    global current_player
    if game_over:
        return

    col = int((x + 300) // 200)
    row = int((250 - y) // 200)
    if row < 0 or row > 2 or col < 0 or col > 2:
        return
    if board[row][col] != "":
        return

    board[row][col] = current_player
    if current_player == "X":
        draw_x(-200 + col*200, 150 - row*200)
        current_player = "O"
    else:
        draw_o(-200 + col*200, 150 - row*200)
        current_player = "X"

    update_turn_indicator()

    winner = check_winner()
    if winner:
        display_winner(winner)

# ----- Restart Game -----
def restart_game():
    global board, current_player, game_over
    pen.clear()
    writer.clear()
    draw_board()
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    update_turn_indicator()

# ----- Bind -----
wn.onclick(click_handler)
wn.listen()
wn.onkey(restart_game, "r")

# ----- Main Loop -----
while True:
    wn.update()
