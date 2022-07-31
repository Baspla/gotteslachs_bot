import logging

from app_version import APP_VERSION

logger = logging.getLogger("version")


def registerVersionHandler(bot):
    @bot.Command(cmd="version")
    def version(source_information, data_message, context, message, args):
        bot.sender.sendText(context, f"Gotteslachs Bot {APP_VERSION}")
