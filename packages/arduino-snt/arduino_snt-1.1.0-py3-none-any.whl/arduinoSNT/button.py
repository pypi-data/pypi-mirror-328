from shutil import Error

import pyfirmata

class Button:
    def __init__(self, board, pin: int) -> None:
        try:
            self.pin = pin
            self.button = board.board.digital[pin]
            self.button.mode = pyfirmata.INPUT
        except Exception as e:
            print(f"An error as occurred during the instantiation of the class Button:\n{e}")
            quit()

    def get_pin(self) -> int:
        return self.pin

    def is_pressed(self) -> bool:
        return self.button.read()

    def is_released(self) -> bool:
        return not self.button.read()