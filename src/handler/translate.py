import logging

from gpytranslate import Translator
from random import randint
import asyncio

logger = logging.getLogger("translate")


def registerTranslateHandler(bot):
    @bot.Message()
    def translate(source_information, data_message, context, message):
        async def translator():
            t = Translator()
            logger.debug("Von: %s", message)
            foerign1 = await t.translate(message, targetlang="it")
            logger.debug("Über: %s", foerign1.text)
            foerign2 = await t.translate(foerign1.text, targetlang="ru")
            logger.debug("Über: %s", foerign2.text)
            foerign3 = await t.translate(foerign1.text, targetlang="ja")
            logger.debug("Über: %s", foerign3.text)
            result = await t.translate(foerign2.text, targetlang="de")
            logger.debug("Zu: %s", result.text)
            # language = await t.detect(result.text)
            bot.sender.sendText(context, f"Meintest du: {result.text}")
            pass

        if randint(0, 99) < 2:
            asyncio.run(translator())
        else:
            message = str(message)
            if message.startswith("$$"):
                message = message[2:]
                asyncio.run(translator())
