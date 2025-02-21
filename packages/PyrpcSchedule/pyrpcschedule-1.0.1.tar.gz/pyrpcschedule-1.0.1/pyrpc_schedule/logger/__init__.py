# -*- encoding: utf-8 -*-
import logging
from pyrpc_schedule.logger.logger import _Logger, _DistributedLog


class Logger(_Logger):
    """
    A singleton class for managing logging configurations and providing a logger instance.
    """

    def logger(self, filename: str, task_id: str = None) -> logging:
        """
        Get a logger instance with the specified filename and task ID.
        :param filename: The name of the log file.
        :param task_id: The task ID associated with the log.
        :return: A logger instance.
        """
        return super().logger(filename, task_id)


class DistributedLog(_DistributedLog):
    """
    A singleton class for managing logging configurations and providing a logger instance.
    """

    def info(self, message):
        """
        Log an informational message.
        :param message: The message to be logged.
        """
        return super().info(message)

    def error(self, message):
        """
        Log an error message.
        :param message: The message to be logged.
        """
        return super().error(message)

    def warning(self, message):
        """
        Log a warning message.
        :param message: The message to be logged.
        """
        return super().warning(message)

    def debug(self, message):
        """
        Log a debug message.
        :param message: The message to be logged.
        """
        return super().debug(message)
