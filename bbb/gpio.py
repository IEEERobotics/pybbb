"""Access GPIO pins via SysFS interface."""


class gpio(object):

    def __init__(self, num, base_dir='/sys/class/gpio/gpio'):
        self.sysfs = base_dir + str(num)
        self._value = None

    @property
    def value(self):
        with open(self.sysfs + '/value', 'r') as f:
            return int(f.read())

    @value.setter
    def value(self, value):
        with open(self.sysfs + '/value', 'w') as f:
            f.write(str(value) + '\n')

    def input(self):
        with open(self.sysfs + '/direction', 'w') as f:
            f.write('in\n')

    def output(self):
        with open(self.sysfs + '/direction', 'w') as f:
            f.write('out\n')
