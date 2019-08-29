import sys
import time
class CountSleep():
    def countdown(t, step=1, msg='Спим'):  # in seconds
        pad_str = ' ' * len('%d' % step)
        for i in range(t, 0, -step):
            sys.stdout.write( '%s следующие %d секунды %s\r' % (msg, i, pad_str),)
            sys.stdout.flush()
            time.sleep(step)
        sys.stdout.write("\r Выполнено! ыыыыыыыыыы   \n")
