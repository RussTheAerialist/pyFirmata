from pyfirmata import *
from boards import BOARDS

__version__ = '0.10.0'  # Don't forget to change in setup.py!

# shortcut classes

class AutoDetect(Board):
    def __init__(self, *args, **kwargs):
        args = list(args)
        args.append('Auto')
        super(AutoDetect, self).__init__(*args, **kwargs)

    def __str__(self):
        return 'AutoDetected: {name} on {port}'.format(
            name=self.name,
            port=self.sp.port
        )

class Arduino(Board):
    """
    A board that wil set itself up as a normal Arduino.
    """
    def __init__(self, *args, **kwargs):
        args = list(args)
        args.append(BOARDS['arduino'])
        super(Arduino, self).__init__(*args, **kwargs)

    def __str__(self):
        return 'Arduino {name} on {port}'.format(
            name=self.name,
            port=self.sp.port
        )


class ArduinoMega(Board):
    """
    A board that wil set itself up as an Arduino Mega.
    """
    def __init__(self, *args, **kwargs):
        args = list(args)
        args.append(BOARDS['arduino_mega'])
        super(ArduinoMega, self).__init__(*args, **kwargs)

    def __str__(self):
        return 'Arduino Mega {name} on {port}'.format(
            name=self.name,
            port=self.sp.port
        )
