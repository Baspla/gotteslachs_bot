import logging

logger = logging.getLogger("ping")


def registerPingHandler(bot):
    @bot.Message(regex="^/ping$")
    def ping(source_information, data_message, context, message):
        bot.sender.sendText(context, "Pong!")