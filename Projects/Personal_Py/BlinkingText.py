import sys
import time

def blink_text(text):
    count = 1
    while True:
        sys.stdout.write('\033[5m' + text + '\033[0m')
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
        time.sleep(0.5)

blink_text('text')
