# Analisis Dampak Perubahan Cuaca terhadap Produksi Pertanian Global

## Latar Belakang
Perubahan iklim berdampak besar pada sektor pertanian global. Kenaikan emisi CO2 dan cuaca ekstrem menurunkan hasil panen dan meningkatkan kerentanan wilayah serta komoditas pertanian.

Proyek ini bertujuan untuk memahami seberapa besar pengaruh faktor-faktor tersebut terhadap sektor pertanian, serta memberikan gambaran prediktif yang dapat digunakan dalam pengambilan keputusan berbasis data.

## Problem Statement
Perubahan iklim memengaruhi produktivitas pertanian global melalui peningkatan suhu, perubahan pola curah hujan, dan peningkatan kejadian cuaca ekstrem. Dampak ini tidak hanya menurunkan hasil panen (yield loss) tetapi juga menimbulkan kerugian ekonomi signifikan bagi petani, wilayah, dan negara.

Berdasarkan kondisi tersebut, penelitian ini berupaya menjawab pertanyaan berikut:
1. Faktor yang paling berpengaruh terhadap hasil panen
2. Analisis Dampak Ekonomi
3. Efektivitas Strategi Adaptasi
4. Optimisasi Input Pertanian
5. Kerentanan Spesifik Wilayah dan Tanaman
6. Korelasi antara emisi CO₂ dengan hasil panen dan kesehatan tanah
7. Tren produktivitas pertanian tiap benua dari 1990–2024 & proyeksinya hingga 2030

## Dataset
Sumber : https://www.kaggle.com/datasets/talhachoudary/global-agriculture-climate-impact-dataset.

Fitur utama dalam dataset:
- Region: Wilayah produksi pertanian.
- Crop_Type: Jenis komoditas pertanian.
- Average_Temperature: Suhu rata-rata tahunan (°C).
- Total_Precipitation: Curah hujan tahunan (mm).
- CO₂_Emissions: Emisi karbon tahunan (ton).
- Yield_Loss: Persentase penurunan hasil panen.
- Extreme_Weather: Indeks kejadian cuaca ekstrem.
- Economic_Impact_Million_USD: Estimasi kerugian ekonomi dalam juta USD.

## Data Pipeline
Membentuk data modeling dari dataset dengan menentukan dim dan fact table, kemudian  melakukakan extract dari sumber dataset, data cleaning dan transform, melakukan validasi dan melakukan load ke database NeonDB PostgreSQL. Proses ETL akan diautomasi menggunakan Airflow. Selanjutnya membuat datamart untuk kebutuhan analisa.

## Tools
* NeonDB PostgreSQL
* Airflow
* Docker
* Python
* Tableau

## Teams
* Farah Arafah
* Firaldi Chandra
* Gilang Aryadipha Lananggalih
* Reza Ainul Muttaqien
* Rifky Iqbal Algifari
* Yustika Dwiani
