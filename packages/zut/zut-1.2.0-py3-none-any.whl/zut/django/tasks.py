from time import sleep
from celery import Task, shared_task
from zut.logging import get_logger

_logger = get_logger(__name__)

def demo(fail_at=None):    
    for i in range(10):
        if fail_at == i:
            raise ValueError(f"Failure at {i}")
        print(f"DEMO {i}")
        _logger.info(f"From logger: {i}")
        sleep(1)

demo: Task = shared_task(demo)
