import pandas as pd
from dagster import execute_pipeline, execute_solid, pipeline, solid

# My first solid
# A solid is a unit of computation in a data pipeline.
@solid
def hello_cereal(context):
    # Assuming the dataset is in the same directory as this file
    dataset_path = "https://raw.githubusercontent.com/dagster-io/dagster/master/examples/dagster_examples/intro_tutorial/cereal.csv"
    df = pd.read_csv(dataset_path)
    cereals = len(df.index)

    context.log.info(
        'Found {} cereals'.format(cereals)
    )

    return df

# A pipeline is a set of solids arranged into a DAG (or directed acyclic graph) of computation
@pipeline
def hello_cereal_pipeline():
    hello_cereal()

# Command line: 
# dagster pipeline execute -f hello_cereal.py -n hello_cereal_pipeline

# Dagit:
# dagit -f hello_cereal.py -n hello_cereal_pipeline

# To run using Python API: 
# python hello_cereal.py
if __name__ == '__main__':
    result = execute_pipeline(hello_cereal_pipeline)
    assert result.success

# Tests for solid and pipeline:
# pytest hello_cereal.py
def test_hello_cereal_solid():
    res = execute_solid(hello_cereal)
    assert res.success
    assert len(res.output_value()) == 77


def test_hello_cereal_pipeline():
    res = execute_pipeline(hello_cereal_pipeline)
    assert res.success
    assert len(res.result_for_solid('hello_cereal').output_value()) == 77