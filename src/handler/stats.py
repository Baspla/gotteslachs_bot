import logging

logger = logging.getLogger("stats")


def registerStatsHandler(bot):
    @bot.Command(cmd="stats")
    def stats(source_information, data_message, context, message, args):
        bot.sender.sendText(context, "Work in Progress. Aber trust me, alle sind broke.")
