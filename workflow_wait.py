from prefect import flow, task
import time

@task
def wait_task():
    time.sleep(10)

@flow
def wait_workflow():
    wait_task()
@flow
def my_flow():
    logger = get_run_logger()
    logger.info("Running Version 1")
    return "Version 1"
