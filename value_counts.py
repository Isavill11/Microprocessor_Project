import pandas as pd



df = pd.read_csv('updated_air_quality_dataset.csv')



print(df['pollution_level'].value_counts())