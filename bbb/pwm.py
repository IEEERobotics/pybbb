"""Access PWM devices via SysFS interface."""


class PWM(object):

    def __init__(self, num, base_dir='/sys/class/pwm/pwm'):
        self.num = num
        self.sysfs = base_dir + str(num)

    def __str__(self):
        return "PWM #{}: {}/{}, pol:{}".format(self.num, self.duty,
                                               self.period, self.polarity)

    @property
    def duty(self):
        with open(self.sysfs + '/duty_ns', 'r') as f:
            return int(f.read())

    @duty.setter
    def duty(self, duty):
        with open(self.sysfs + '/duty_ns', 'w') as f:
            f.write(str(duty) + '\n')

    @property
    def period(self):
        with open(self.sysfs + '/period_ns', 'r') as f:
            return int(f.read())

    @period.setter
    def period(self, period):
        with open(self.sysfs + '/period_ns', 'w') as f:
            f.write(str(period) + '\n')

    @property
    def polarity(self):
        with open(self.sysfs + '/polarity', 'r') as f:
            return int(f.read())

    @polarity.setter
    def polarity(self, polarity):
        # TODO: Verify that the stop/start is actually necessary
        self.stop()
        with open(self.sysfs + '/polarity', 'w') as f:
            f.write(str(polarity) + '\n')
        self.start()

    def stop(self):
        with open(self.sysfs + '/run', 'w') as f:
            f.write('0\n')

    def start(self):
        with open(self.sysfs + '/run', 'w') as f:
            f.write('1\n')
