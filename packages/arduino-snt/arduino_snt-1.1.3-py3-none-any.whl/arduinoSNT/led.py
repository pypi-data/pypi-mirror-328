import pyfirmata

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .board import Board

class Led:
    def __init__(self, board: "Board", pin: int) -> None:
        try:
            self.pin = pin
            self.led = board.board.digital[pin]
            self.led.mode = pyfirmata.OUTPUT

            board.add_led(self)

        except Exception as e:
            print(f"An error as occurred during the instantiation of the class Led:\n{e}")
            quit()

    def get_pin(self) -> int:
        return self.pin

    def turn_on(self) -> None:
        self.led.write(True)

    def turn_off(self) -> None:
        self.led.write(False)