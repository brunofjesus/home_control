import logging

from telegram import Update

import config

logger = logging.getLogger(__name__)


def require_allowed_user(func):
    """
    Decorator allowing only allowed users to execute the decorated function
    """

    def wrapper_func(*args, **kwargs):
        update = None
        username = None

        for arg in args:
            if isinstance(arg, Update):
                update = arg
                username = update.effective_user.username
                break

        if username is None:
            logger.warning("Cannot find message username")
            return

        logger.info("Got message from {}".format(username))

        if username not in config.allowed_users():
            logger.warning("{} is not allowed to send commands".format(username))
            update.effective_message.reply_text("Fuck you I won't do what you tell me")
            return

        func(*args, **kwargs)

    return wrapper_func
