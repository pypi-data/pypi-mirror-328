from board import Board, Led

board = Board("8")
board.start()

button_right = board.create_button(2)
button_turn = board.create_button(3)
led1 = board.create_led(13)

led2 = Led(board, 13)
board.add_led(led2)