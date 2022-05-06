import RPi.GPIO as GPIO
from time import sleep

from toggle.toggle import Toggle


class PressToggle(Toggle):

    def __init__(self, id: str, pin: int) -> None:
        super().__init__()
        self.id = id
        self.pin = pin

    def execute(self, args):
        if len(args) == 0:
            raise AttributeError("No args")

        if str(args[0]).lower() == "off":
            state = False
        elif str(args[0]).lower() == "on":
            state = True
        else:
            return "Unknown state: {}".format(str(args[0]))

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

        GPIO.output(self.pin, state)

        return "{} - {}: DONE!".format(self.id, str(args[0]))
