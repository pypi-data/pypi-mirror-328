import asyncio
import logging
import os
import sys
from contextvars import ContextVar

task_name_getter = ContextVar("task_name_getter", default=lambda: "-")

import asyncio

async def ainput(*args):
    return await asyncio.to_thread(input, *args)

class TaskFieldFilter(logging.Filter):
    def filter(self, record):
        record.task = task_name_getter.get()()
        return True

logging.getLogger().addFilter(TaskFieldFilter())
quest_logger = logging.getLogger('quest')

for logger_name in logging.root.manager.loggerDict.keys():
    logger = logging.getLogger(logger_name)
    logger.addFilter(TaskFieldFilter())
