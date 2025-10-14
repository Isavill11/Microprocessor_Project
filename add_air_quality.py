import pandas as pd

# Load dataset
df = pd.read_csv('air_quality_dataset.csv')

# Convert pollutant columns to numeric (force errors to NaN)
pollutants = ['SO2', 'NO3', 'HNO3', 'SO4']
for col in pollutants:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Define classification function
def classify_pollution_index(value):
    if value <= 0.33:
        return 0  # Low
    elif value <= 0.66:
        return 1  # Moderate
    else:
        return 2  # High

# Compute normalized pollution index across pollutants
df['pollution_index'] = (
    df[pollutants]
    .apply(lambda x: (x - x.min()) / (x.max() - x.min()), axis=0)
    .mean(axis=1)
)

# Apply pollution level classification
df['pollution_level'] = df['pollution_index'].apply(classify_pollution_index)


df.to_csv('updated_air_quality_dataset.csv')