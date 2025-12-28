import pandas as pd
from utils.logger import logger

def extract(file_path: str) -> pd.DataFrame:
    logger.info(f"Extract: чтение файла {file_path}")
    df = pd.read_csv(file_path)
    return df
