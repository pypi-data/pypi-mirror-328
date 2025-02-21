from .exceptions import PinAlreadyUsedError, PinNotUsedError

import pyfirmata
import pyfirmata.util

from .button import Button
from .led import Led

class Board:
    def __init__(self, port) -> None:
        try:
            self.port = f"COM{port}"
            self.board = pyfirmata.Arduino(self.port)

            self.iterator = pyfirmata.util.Iterator(self.board)

            self.pins = {"buttons": {}, "leds": {}}

        except Exception as e:
            print(f"An error as occurred during the instantiation of the class Board:\n{e}")
            quit()

    def start(self) -> None:
        self.iterator.start()

    def close(self) -> None:
        for led in self.pins["leds"].values():
            led.turn_off()

    def pin_already_used(self, pin: int) -> bool:
        for used_pin in self.pins["leds"].keys():
            if used_pin == pin:
                return True

        for used_pin in self.pins["buttons"].keys():
            if used_pin == pin:
                return True

        return False

    def get_port(self) -> str:
        return self.port

    def create_button(self, pin: int) -> Button:
        if self.pin_already_used(pin):
            raise PinAlreadyUsedError("Another component is already connected to this pin.")

        button = Button(self, pin)
        self.pins["buttons"][pin] = button
        return button

    def add_button(self, button: Button) -> None:
        if self.pin_already_used(button.get_pin()):
            raise PinAlreadyUsedError("Another component is already connected to this pin.")

        self.pins["buttons"][button.get_pin()] = button

    def remove_button(self, button: Button) -> None:
        if self.pin_already_used(button.get_pin()):
            self.pins["buttons"].pop(button.get_pin())

        else:
            raise PinNotUsedError("No component connected to this pin.")

    def create_led(self, pin: int) -> Led:
        if self.pin_already_used(pin):
            raise PinAlreadyUsedError("Another component is already connected to this pin.")

        led = Led(self, pin)
        self.pins["leds"][pin] = led
        return led

    def add_led(self, led: Led) -> None:
        if self.pin_already_used(led.get_pin()):
            raise PinAlreadyUsedError("Another component is already connected to this pin.")

        self.pins["leds"][led.get_pin()] = led

    def remove_led(self, led: Led) -> None:
        if self.pin_already_used(led.get_pin()):
            self.pins["leds"].pop(led.get_pin())

        else:
            raise PinNotUsedError("No component connected to this pin.")