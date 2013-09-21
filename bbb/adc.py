"""Access ADCs vias SysFS interface."""

import glob


class ADC(object):

    def __init__(self, num, base_filename='/sys/devices/ocp.*/helper.*/AIN'):
        self.num = num
        # Need to read a glob here, since numbering is not consistent
        # TODO: Verify num is reasonable (0-6)
        self.sysfs = glob.glob(base_filename + str(num))[0]

    def __str__(self):
        out = "ADC#%d (%s)" % (self.num, self.sysfs)
        return out

    def read(self):
        with open(self.sysfs, 'r') as f:
            f.read()
        val = None
        # Read a second time to ensure current value (bug in ADC driver)
        while not val:
            try:
                with open(self.sysfs, 'r') as f:
                    val = f.read()
            except:
                pass
        return int(val)
