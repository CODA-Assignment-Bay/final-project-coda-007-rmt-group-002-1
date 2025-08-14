#import libraries
import pandas as pd
import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine

# buat variable untuk koneksi ke NeonDB
DB_CONFIG = {
    'host': 'ep-old-wave-a1jg0peq-pooler.ap-southeast-1.aws.neon.tech',
    'database': 'neondb',
    'user': 'neondb_owner',
    'password': 'npg_kpWKCcs9fiA0',
    'port': '5432'
}
engine = create_engine(f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}", connect_args={'sslmode': "require"})

# read dataset
data_geo = pd.read_csv('/opt/airflow/data/dim_geo.csv')
data_crop_type = pd.read_csv('/opt/airflow/data/dim_crop_type.csv')
data_adaptation = pd.read_csv('/opt/airflow/data/dim_adaptation.csv')
data_fact = pd.read_csv ('/opt/airflow/data/fact_agriculture_climate.csv')

# load ke database sesuai nama tablenya
data_geo.to_sql(name='dim_geography', con=engine, if_exists='replace', index=False)
data_crop_type.to_sql(name='dim_crop_type', con=engine, if_exists='replace', index=False)
data_adaptation.to_sql(name='dim_adaptation', con=engine, if_exists='replace', index=False)
data_fact.to_sql(name='fact_agriculture_climate', con=engine, if_exists='replace', index=False)