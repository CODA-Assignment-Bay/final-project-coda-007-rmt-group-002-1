from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# Koneksi ke database Neon
DB_CONFIG = {
    'host': 'ep-old-wave-a1jg0peq-pooler.ap-southeast-1.aws.neon.tech',
    'database': 'neondb',
    'user': 'neondb_owner',
    'password': 'npg_kpWKCcs9fiA0',
    'port': '5432'
}
engine = create_engine(f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}", connect_args={'sslmode': "require"})


# 1. Create table
create_table_query = """
CREATE TABLE IF NOT EXISTS dm_agriculture_climate (
    year INT,
    country TEXT,
    region TEXT,
    crop_type TEXT,
    average_temperature FLOAT,
    total_precipitation FLOAT,
    co2_emmissions FLOAT,
    crop_yield FLOAT,
    extreme_weather_events INT,
    irrigation_access FLOAT,
    pesticide FLOAT,
    fertilizer FLOAT,
    soil_health_index FLOAT,
    adaptation_strategies TEXT,
    economic_impact FLOAT
);
"""


# 2. Insert table
etl_query = """
INSERT INTO dm_agriculture_climate (
    year,
    country,
    region,
    crop_type,
    average_temperature,	
    total_precipitation,	
    co2_emmissions,	
    crop_yield,	
    extreme_weather_events,	
    irrigation_access,	
    pesticide,	
    fertilizer,	
    soil_health_index,	
    adaptation_strategies,
    economic_impact
)
SELECT
    f.year,
    t.country,
    t.region,
    c.crop_type,
    f.average_temperature,	
    f.total_precipitation,	
    f.co2_emmissions,	
    f.crop_yield,	
    f.extreme_weather_events,	
    f.irrigation_access,	
    f.pesticide,	
    f.fertilizer,	
    f.soil_health_index,	
    l.adaptation_strategies,
    f.economic_impact
FROM fact_agriculture_climate f
JOIN dim_geography t ON f.geo_id = t.geo_id
JOIN dim_adaptation l ON f.adaptation_id = l.adaptation_id
JOIN dim_crop_type c ON f.crop_id = c.crop_id;
"""

# 3️. Eksekusi query
with Session(engine) as session:
    session.execute(text(create_table_query))
    session.execute(text("TRUNCATE TABLE dm_agriculture_climate;"))
    session.execute(text(etl_query))
    session.commit()