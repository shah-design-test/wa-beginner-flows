from prefect import flow, task
import time

@task(retries=2, retry_delay_seconds=5)
def step_one():
    print("Step 1: Job started")

@task
def step_two():
    print("Step 2: Processing...")
    time.sleep(3)

@task
def step_three():
    print("Step 3: Job completed")

@flow(name="sample-prefect-job")
def my_job():
    step_one()
    step_two()
    step_three()

if __name__ == "__main__":
    my_job()
