import logging

logger = logging.getLogger("ping")


def registerTestHandler(bot):
    @bot.Command(cmd="test1")
    def test(source_information, data_message, context, message, args):
        bot.sender.sendText(context, f"args: {args}")

    @bot.Command()
    def test2(source_information, data_message, context, message, args):
        bot.sender.sendText(context, f"args: {args}")
