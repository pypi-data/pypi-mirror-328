import subprocess

FIRMATA_SCRIPT = "./firmata/StandardFirmata.hex"

def init_arduino(port: str, hex_file: str = FIRMATA_SCRIPT, mcu: str = "atmega328p") -> bool:
    """
    Uploads a compiled .hex file to an Arduino using avrdude.

    :param port: The serial port where the Arduino is connected (e.g., "COM3" or "/dev/ttyUSB0").
    :param hex_file: The path to the .hex file to upload.
    :param mcu: The microcontroller type (default: "atmega328p" for Arduino Uno).
    :return: True if upload is successful, False otherwise.
    """
    avrdude_path="avrdude"
    avrdude_cmd = [
        avrdude_path,
        "-p", "atmega328p",
        "-c", "arduino",
        "-P", "COM8",
        "-b", "115200",
        "-U", "flash:w:C:/Users/Amaury/Documents/tools/arduino-snt/arduinoSNT/firmata/StandardFirmata.hex:i"
    ]

    try:
        result = subprocess.run(avrdude_cmd, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        return False