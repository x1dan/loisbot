from modules.sentry import Sentry
from core.app import App
from dotenv import load_dotenv
from colorama import init
import sys
import signal
if __name__ == '__main__':
    load_dotenv()
    Sentry.init()
    init(convert=True)
    App.start()