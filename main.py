#!/usr/bin/env python
# pylint: disable=C0116,W0613

"""
Simple Bot to handle small home automation tasks.
Greets new users & keeps track of which chats the bot is in.
Usage:
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
)

import config
from decorators import require_allowed_user

# Enable logging
from toggle import Toggle

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


@require_allowed_user
def toggle(update: Update, context: CallbackContext):
    if not context or not context.args or len(context.args) == 0:
        update.effective_message.reply_text("Context needed")

    try:
        toggle_obj = Toggle(context.args[0])
    except AttributeError as e:
        update.effective_message.reply_text(str(e))
        return

    update.effective_message.reply_text(toggle_obj.press())


def main() -> None:
    """Start the bot."""
    updater = Updater(config.token())

    dispatcher = updater.dispatcher

    # Garage handling
    dispatcher.add_handler(CommandHandler("toggle", toggle))
    dispatcher.add_handler(CommandHandler("tg", toggle))

    # Start the Bot
    updater.bot.send_message(chat_id=config.chat_id(), text="Hello world")

    updater.start_polling(allowed_updates=Update.ALL_TYPES)
    updater.idle()


if __name__ == "__main__":
    main()
