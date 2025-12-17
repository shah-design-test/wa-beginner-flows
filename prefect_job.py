from prefect import flow, task
from prefect.logging import get_run_logger
import time

@task
def step_one():
    logger = get_run_logger()
    logger.info("Step 1: Job started")

@task(
    retries=1,              # 🔁 Retry count
    retry_delay_seconds=5   # ⏱ Retry delay
)
def step_two():
    logger = get_run_logger()

    logger.info("Step 2: Processing...")

    # ❌ Intentional failure
    raise Exception("Intentional failure to test retry")

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
