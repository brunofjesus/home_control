#!/usr/bin/env python

from flask import Flask
import logging

from telegram.ext import Updater

import config
from toggle import toggle_factory

logger = logging.getLogger(__name__)
app = Flask(__name__)

telegramUpdater = Updater(config.token())


@app.route("/event/<item>/<value>", methods=["POST"])
def report_event(item: str, value: str):
    logger.info("Event: {} - {}".format(item, value))
    telegramUpdater.bot.send_message(chat_id=config.chat_id(), text="Event: {} - {}".format(item, value))
    return "OK"


@app.route("/action/toggle/<item>/<value>", methods=["POST"])
def action_toggle_value(item: str, value: str):
    logger.info("Action Toggle Value: {} - {}".format(item, value))
    toggle_obj = toggle_factory.create(item)
    return toggle_obj.execute([value])


@app.route("/action/toggle/<item>", methods=["POST"])
def action_toggle(item: str):
    logger.info("Action Toggle: {}".format(item))
    toggle_obj = toggle_factory.create(item)
    return toggle_obj.execute(None)


def main():
    app.run(host=config.host(), port=config.port())


if __name__ == "__main__":
    main()
