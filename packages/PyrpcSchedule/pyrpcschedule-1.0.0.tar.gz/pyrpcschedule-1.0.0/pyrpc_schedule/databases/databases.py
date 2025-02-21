# -*- encoding: utf-8 -*-

from pyrpc_schedule.databases.client import Client


class DatabaseTasks(Client):
    """
    DatabaseTasks class is used to manage database task - related operations.
    It inherits from the Client class and uses the singleton pattern to ensure there is only one instance globally.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Override the __new__ method to implement the singleton pattern.
        If the instance does not exist, create a new instance and initialize it;
        otherwise, return the existing instance.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Singleton instance
        """
        if cls._instance is None:
            cls._instance = super(DatabaseTasks, cls).__new__(cls)
            cls._instance._initialize(*args, **kwargs)
        return cls._instance

    def __init__(self, config: dict, table_name: str):
        """
        Initialize the database connection and other related configurations.

        :param config: A dictionary containing the database connection configuration information.
        :param table_name: The name of the database table to be operated on.
        """
        pass


class DatabaseNodes(Client):
    """
    DatabaseNodes class is used to manage database node - related operations.
    It inherits from the Client class and uses the singleton pattern to ensure there is only one instance globally.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Override the __new__ method to implement the singleton pattern.
        If the instance does not exist, create a new instance and initialize it;
        otherwise, return the existing instance.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Singleton instance
        """
        if cls._instance is None:
            cls._instance = super(DatabaseNodes, cls).__new__(cls)
            cls._instance._initialize(*args, **kwargs)
        return cls._instance

    def __init__(self, config: dict, table_name: str):
        """
        Initialize the database connection and other related configurations.

        :param config: A dictionary containing the database connection configuration information.
        :param table_name: The name of the database table to be operated on.
        """
        pass


class DatabaseServices(Client):
    """
    DatabaseServices class is used to manage database service - related operations.
    It inherits from the Client class and uses the singleton pattern to ensure there is only one instance globally.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Override the __new__ method to implement the singleton pattern.
        If the instance does not exist, create a new instance and initialize it;
         otherwise, return the existing instance.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Singleton instance
        """
        if cls._instance is None:
            cls._instance = super(DatabaseServices, cls).__new__(cls)
            cls._instance._initialize(*args, **kwargs)
        return cls._instance

    def __init__(self, config: dict, table_name: str):
        """
        Initialize the database connection and other related configurations.

        :param config: A dictionary containing the database connection configuration information.
        :param table_name: The name of the database table to be operated on.
        """
        pass
