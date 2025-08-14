# import libraries
import kagglehub
import pandas as pd
import os

DATASET_ROOT_DIR = "/opt/airflow/data"
# Download latest version
path = kagglehub.dataset_download("talhachoudary/global-agriculture-climate-impact-dataset")

file_path = os.path.join(path, "climate_change_impact_on_agriculture_2024.csv")

# Baca file dengan pandas
df = pd.read_csv(file_path)

df.to_csv('/opt/airflow/data/agriculture_climate.csv', index=False)
