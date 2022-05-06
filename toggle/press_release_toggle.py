import RPi.GPIO as GPIO
from time import sleep

from toggle.toggle import Toggle


class PressReleaseToggle(Toggle):

    def __init__(self, id: str, pin: int, duration: float) -> None:
        super().__init__()
        self.id = id
        self.pin = pin
        self.duration = duration

    def execute(self, args):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

        GPIO.output(self.pin, True)
        sleep(self.duration)
        GPIO.output(self.pin, False)

        return "{}: DONE!".format(self.id)