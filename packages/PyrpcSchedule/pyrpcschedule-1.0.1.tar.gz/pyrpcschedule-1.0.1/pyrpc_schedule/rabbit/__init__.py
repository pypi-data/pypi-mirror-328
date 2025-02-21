# -*- encoding: utf-8 -*-

from pyrpc_schedule.rabbit.rabbit import _RabbitMQ


class RabbitMQ(_RabbitMQ):
    """
    A class for interacting with RabbitMQ.
    """

    def send_message(self, queue, message):
        """
        Sends a message to the specified queue.
        Args:
            queue (str): The name of the queue to send the message to.
            message (dict): The message to be sent.
        """
        super().send_message(queue, message)

    def get_message(self, queue, callback):
        """
        Retrieves a message from the specified queue.
        Args:
            queue (str): The name of the queue to retrieve the message from.
            callback (function): The callback function to be called when a message is received.
        """
        super().get_message(queue, callback)
