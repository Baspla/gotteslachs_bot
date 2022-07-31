import logging

logger = logging.getLogger("help")


def registerHelpHandler(bot):
    @bot.Command(cmd="help")
    def _help(source_information, data_message, context, message, args):
        bot.sender.sendText(source_information.source_uuid, "Hier sind alle Befehle die ich bisher kann\n"
                                                            "/help\n"
                                                            "/stats\n"
                                                            "/version")
