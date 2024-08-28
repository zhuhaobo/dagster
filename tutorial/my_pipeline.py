from dagster import job, op

@op
def hello_world_op():
    return "Hello, Dagster!"

@job
def hello_world_job():
    hello_world_op()