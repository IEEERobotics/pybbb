"""Access GPIO pins via SysFS interface."""

import time


class GPIO(object):

    def __init__(self, num, base_dir='/sys/class/gpio/gpio'):
        self.num = num
        self.sysfs = base_dir + str(self.num)

    def __str__(self):
        return "GPIO #{}: value:{}, direction:{}".format(self.num, self.value,
                                                         self.direction)

    @property
    def value(self):
        with open(self.sysfs + '/value', 'r') as f:
            return int(f.read())

    @value.setter
    def value(self, value):
        with open(self.sysfs + '/value', 'w') as f:
            f.write(str(value) + '\n')

    @property
    def direction(self):
        with open(self.sysfs + '/direction', 'r') as f:
            direction = f.read()
            # Remove trailing newline for readability
            if direction[-1] == "\n":
                direction = direction[:-1]
            return direction

    def input(self):
        with open(self.sysfs + '/direction', 'w') as f:
            f.write('in\n')

    def output(self):
        with open(self.sysfs + '/direction', 'w') as f:
            f.write('out\n')

    def pulse(self, duration=0.1):
        """Actuate GPIO pin for a given duration.

        :param duration: How long to keep the pin on (secs.).
        :type duration: float

        """
        # Use try-finally in case we are interrupted in sleep
        try:
            self.value = 1
            time.sleep(duration)
        finally:
            self.value = 0
