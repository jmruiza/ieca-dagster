# Run from command line:
#   dagit -f hello_dagster.py -n hello_pipeline

# Run from the Dagit GUI:  http://localhost:3000
#   dagit -f hello_dagster.py -n hello_pipeline

from dagster import execute_pipeline, pipeline, solid

@solid
def get_name(_):
    return 'dagster'

@solid
def hello(context, name: str):
    context.log.info('Hello, {name}!'.format(name=name))

@pipeline
def hello_pipeline():
    hello(get_name())
