# import library
import pandas as pd

# load dataset
df = pd.read_csv('/opt/airflow/data/agriculture_climate.csv')

# rename kolom menjadi agar mudah dibaca
df.columns = df.columns.str.lower()
df.rename(columns={'average_temperature_c': 'average_temperature'}, inplace=True)
df.rename(columns={'total_precipitation_mm': 'total_precipitation'}, inplace=True)
df.rename(columns={'co2_emissions_mt': 'co2_emmissions'}, inplace=True)
df.rename(columns={'crop_yield_mt_per_ha': 'crop_yield'}, inplace=True)
df.rename(columns={'irrigation_access_%': 'irrigation_access'}, inplace=True)
df.rename(columns={'pesticide_use_kg_per_ha': 'pesticide'}, inplace=True)
df.rename(columns={'fertilizer_use_kg_per_ha': 'fertilizer'}, inplace=True)
df.rename(columns={'soil_health_index': 'soil_health_index'}, inplace=True)
df.rename(columns={'adaptation_strategies': 'adaptation_strategies'}, inplace=True)
df.rename(columns={'economic_impact_million_usd': 'economic_impact'}, inplace=True)


# ambil dim geography dari dataset
dim_geo = df[['country', 'region']].drop_duplicates().reset_index(drop=True)
dim_geo['geo_id'] = dim_geo.index + 1

# ambil dim crop_type dari dataset
dim_crop_type = df[['crop_type']].drop_duplicates(subset=['crop_type']).reset_index(drop=True)
dim_crop_type['crop_id'] = dim_crop_type.index + 1

# ambil dim adaptation_strategies dari dataset
dim_adaptation = df[['adaptation_strategies']].drop_duplicates(subset=['adaptation_strategies']).reset_index(drop=True)
dim_adaptation['adaptation_id'] = dim_adaptation.index + 1

df = df.merge(dim_geo, on=['country', 'region'], how='left')
df = df.merge(dim_crop_type, on=['crop_type'], how='left')
df = df.merge(dim_adaptation, on=['adaptation_strategies'], how='left')

# ambil fact_table dari dataset
fact_agriculture_climate = df[['year','geo_id','crop_id','average_temperature', 'total_precipitation','co2_emmissions',
                               'crop_yield', 'extreme_weather_events', 'irrigation_access','pesticide', 'fertilizer',
                               'soil_health_index', 'adaptation_id','economic_impact']]


dim_geo.to_csv('/opt/airflow/data/dim_geo.csv', index=False)
dim_crop_type.to_csv('/opt/airflow/data/dim_crop_type.csv', index=False)
dim_adaptation.to_csv('/opt/airflow/data/dim_adaptation.csv', index=False)
fact_agriculture_climate.to_csv('/opt/airflow/data/fact_agriculture_climate.csv', index=False)



