import logging
from simple_signal_bot.signal_bot import SignalBot

from handler.ping import registerPingHandler
from handler.test import registerTestHandler
from handler.translate import registerTranslateHandler


def main():
    logging.basicConfig(handlers=[logging.StreamHandler()],
                        level=logging.DEBUG)
    bot = SignalBot()

    @bot.Message(regex="^/ping$")
    def ping(source_information, data_message, context, message):
        bot.sender.sendText(context, "Pong!")
    registerPingHandler(bot)
    registerTranslateHandler(bot)
    registerTestHandler(bot)

    bot.run()


if __name__ == '__main__':
    main()
