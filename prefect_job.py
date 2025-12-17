from prefect import flow, task
from prefect.logging import get_run_logger
import time

@task
def step_one():
    logger = get_run_logger()
    logger.info("Step 1: Job started")

@task
def step_two():
    logger = get_run_logger()
    logger.info("Step 2: Processing...")
    time.sleep(3)

@task
def step_three():
    logger = get_run_logger()
    logger.info("Step 3: Job completed")

@flow(name="sample-prefect-job")
def my_job():
    step_one()
    step_two()
    step_three()
my_job()
