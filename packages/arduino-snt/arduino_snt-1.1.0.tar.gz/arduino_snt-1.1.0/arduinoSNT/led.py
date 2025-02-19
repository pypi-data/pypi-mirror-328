import pyfirmata

class Led:
    def __init__(self, board, pin: int) -> None:
        try:
            self.pin = pin
            self.led = board.board.digital[pin]
            self.led.mode = pyfirmata.OUTPUT
        except Exception as e:
            print(f"An error as occurred during the instantiation of the class Led:\n{e}")
            quit()

    def get_pin(self) -> int:
        return self.pin

    def turn_on(self) -> None:
        self.led.write(True)

    def turn_off(self) -> None:
        self.led.write(False)