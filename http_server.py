#!/usr/bin/env python

from flask import Flask
import logging

from telegram.ext import Updater

import config

logger = logging.getLogger(__name__)
app = Flask(__name__)

telegramUpdater = Updater(config.token())


@app.route("/event/<item>/<value>", methods=["POST"])
def report_event(item: str, value: str):
    logger.info("Event: {} - {}".format(item, value))
    telegramUpdater.bot.send_message(chat_id=config.chat_id(), text="Event: {} - {}".format(item, value))
    return "OK"


def main():
    app.run(host=config.host(), port=config.port())


if __name__ == "__main__":
    main()
