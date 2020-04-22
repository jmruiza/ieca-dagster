import pandas as pd

dataset = "https://raw.githubusercontent.com/dagster-io/dagster/master/examples/dagster_examples/intro_tutorial/cereal.csv"
df = pd.read_csv(dataset)

print(df.head())