from unittest import TestCase, expectedFailure
from bbb import PWM

class TestPWM(TestCase):

    @expectedFailure
    def test_init(self):
        pwm = PWM(1)
        self.assertIsInstance(pwm, PWM)

    def test_bad_init(self):
        with self.assertRaises(ValueError):
            pwm = PWM(0)

    def test_value_of_duty_cycle(self):
        pwm = PWM(1)
        for test_duty_cycle in range (0,100):
            pwm.set_duty_percent(test_duty_cycle)
            assert pwm.duty_percent == test_duty_cycle            
