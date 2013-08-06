"""Access PWM devices via SysFS interface."""


class pwm(object):

    def __init__(self, num):
        self.num = num
        self.sysfs = '/sys/class/pwm/pwm' + str(num)
        with open(self.sysfs + '/duty_ns', 'r') as f:
            self._duty = int(f.read())
        with open(self.sysfs + '/period_ns', 'r') as f:
            self._period = int(f.read())
        with open(self.sysfs + '/polarity', 'r') as f:
            self._polarity = int(f.read())

    def __str__(self):
        return "PWM #{}: {}/{}, pol:{}".format(self.num, self.duty,
                                               self.period, self.polarity)

    @property
    def duty(self):
        with open(self.sysfs + '/duty_ns', 'r') as f:
            return int(f.read(str(ds))

    @duty.setter
    def duty(self, duty):
        with open(self.sysfs + '/duty_ns', 'w') as f:
            f.write(str(duty) + '\n')
        self._duty = duty # TODO(dfarrell07): Can this be removed?

    @property
    def period(self):
        with open(self.sysfs + '/period_ns', 'r') as f:
            return int(f.read())

    @period.setter
    def period(self, period):
        with open(self.sysfs + '/period_ns', 'w') as f:
            f.write(str(period) + '\n')
        self._period = period # TODO(dfarrell07): Can this be removed?

    @property
    def polarity(self):
        with open(self.sysfs + '/polarity', 'r') as f:
            return int(f.read())

    @polarity.setter
    def polarity(self, polarity):
        # TODO: Verify that the stop/start is actually necessary
        self.stop()
        with open(self.sysfs + '/polarity', 'w') as f:
            f.write(str(val) + '\n')
        self._polarity = polarity # TODO(dfarrell07): Can this be removed?
        self.start()

    def stop(self):
        with open(self.sysfs + '/run', 'w') as f:
            f.write('0\n')

    def start(self):
        with open(self.sysfs + '/run', 'w') as f:
            f.write('1\n')
