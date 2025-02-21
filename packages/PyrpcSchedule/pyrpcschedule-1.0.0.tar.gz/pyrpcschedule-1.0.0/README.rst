PyrpcSchedule Description Document
==================================

Assist developers/testers in quickly building distributed task systems.

1. Introduction
---------------

Integrated service discovery, service registration, service governance, workflow, task scheduling, system monitoring, and distributed logging.

Supports priority queue, sharded tasks, and automatic synchronization of subtask status.

2. QuickStart
-------------

To help you quickly learn how to use PyrpcSchedule, please follow the steps below to create a test project.

2.1 Install
~~~~~~~~~~~

.. code-block:: bash

   pip install PyrpcSchedule

   # Install RabbitMQ and initialize the administrator account
   rabbitmqctl add_user scheduleAdmin scheduleAdminPasswrd
   rabbitmqctl set_user_tags scheduleAdmin administrator
   rabbitmqctl set_permissions -p / scheduleAdmin ".*" ".*" ".*"
   rabbitmqctl list_users

   # Install MongoDB and initialize the administrator account
   mongo
   use admin
   db.createUser({user: "scheduleAdmin", pwd: "scheduleAdminPasswrd", roles: [{role: "root", db: "admin"}]})

**Note:** Use higher security passwords in production environments.

2.2 Create a Test Project
~~~~~~~~~~~~~~~~~~~~~~~~~

Please create folders and Python files according to the instructions:

.. code-block:: text

   .
   ├── test_server
   │   ├── test_server_1
   │   │   ├── test_server_1.py
   │   ├── test_server_2
   │   │   ├── test_server_2.py
   │   ├── test_server_3.py
   ├── pyrpc_schedule_test.py

2.3 test_server.x Python File Content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pyrpc_schedule import ServiceConstructor, WorkerConstructor

   class RpcFunction(ServiceConstructor):
       """
       Class Name Not modifiable, Define RPC functions
       """
       service_name = 'test_server_1'

       def get_service_name(self, version):
           self.logger.info(f'version == {version}')
           return {"service_name": self.service_name, "version": version}

       """
       You can add other code for this service here
       """
       def test_function(self, x: int, y: int):
           return x + y

   class WorkerFunction(WorkerConstructor):
       """
       Class Name Not modifiable, Worker Code
       """
       worker_name = 'test_server_1'

       def run(self, data):
           self.logger.info(data)
           """
           Implement business-related logic
           """

2.4 pyrpc_schedule_test Python File Content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import os
   import time
   import logging
   import argparse
   from pymongo.cursor import Cursor

2.5 Initiate Testing Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Start Service
   python pyrpc_schedule_test.py

   # Test RPC Service
   python pyrpc_schedule_test.py --test True

   # After startup, a logs folder will be created in the current directory, classified by service type.


Thank you for choosing to use PyrpcSchedule. 
If you encounter any problems or have any good ideas during use, please contact me.