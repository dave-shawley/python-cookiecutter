import signal
import sys


def run():
    def _handler(signo, frame):
        print('Signal', signo, 'received, exiting')

    signal.signal(signal.SIGINT, _handler)
    signal.signal(signal.SIGTERM, _handler)
    print('Running, press Ctrl+C to exit.')
    signal.pause()
    sys.exit(0)
