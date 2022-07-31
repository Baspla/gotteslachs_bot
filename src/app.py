import logging
import os

from simple_signal_bot.signal_bot import SignalBot

from handler.help import registerHelpHandler
from handler.version import registerVersionHandler
from handler.stats import registerStatsHandler
from handler.translate import registerTranslateHandler


def main():
    logging.basicConfig(handlers=[logging.StreamHandler()],
                        level=os.environ.get('LOG_LEVEL', "INFO"))
    bot = SignalBot()

    registerHelpHandler(bot)
    registerTranslateHandler(bot)
    registerVersionHandler(bot)
    registerStatsHandler(bot)

    bot.run()


if __name__ == '__main__':
    main()
