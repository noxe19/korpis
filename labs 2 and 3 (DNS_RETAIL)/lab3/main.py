from etl.extract import extract
from etl.transform import transform
from etl.load import load
from visualize import visualize
import pandas as pd

INPUT_FILE = "data/input/products_import.csv"

df = extract(INPUT_FILE)
valid_data, errors = transform(df)

load(valid_data)

pd.DataFrame(valid_data).to_csv("data/output/loaded_data.csv", index=False)
pd.DataFrame(errors).to_csv("data/output/errors.csv", index=False)

visualize(len(valid_data), len(errors))
