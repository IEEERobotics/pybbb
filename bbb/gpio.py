"""Access GPIO pins via SysFS interface."""


class gpio(object):

    def __init__(self, num):
        self.sysfs = '/sys/class/gpio/gpio' + str(num)
        self._value = None

    @property
    def value(self):
        with open(self.sysfs + '/value', 'r') as f:
            return int(f.read())

    @value.setter
    def value(self, value):
        with open(self.sysfs + '/value', 'w') as f:
            f.write(str(value) + '\n')
        self._value = value # TODO(dfarrell07): Can this be removed?

    def input(self):
        with open(self.sysfs + '/direction', 'w') as f:
            f.write('in\n')

    def output(self):
        with open(self.sysfs + '/direction', 'w') as f:
            f.write('out\n')
