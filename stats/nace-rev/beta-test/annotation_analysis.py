import os
import s3fs

import pandas as pd
import numpy as np


fs = s3fs.S3FileSystem(
        client_kwargs={"endpoint_url": os.getenv("S3_ENDPOINT")},
        key=os.getenv("AWS_ACCESS_KEY_ID"),
        secret=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )

# Get files
data = pd.read_parquet('annotated_data_CG_NAF2025.parquet')

# Agrégation par 'id' et création de listes uniques pour 'col1'
aggregated_df = data.groupby('liasse_numero').agg({'apet_manual': lambda x: list(x.unique()),
                                                     'rating' : list
}).reset_index()
print(len(aggregated_df))

# Calcul du nombre de lignes où la liste ne contient qu'un seul élément
single_element_count = aggregated_df['apet_manual'].apply(lambda x: len(x) == 1).sum()
mean_rating = aggregated_df['rating'].apply(lambda x: np.mean(x)).mean()

# Calcul du pourcentage de ces lignes par rapport au total
percentage_single_element = (single_element_count / len(aggregated_df)) * 100

print(data['apet_manual'])
print("Agrégation du DataFrame:")
print(aggregated_df)
print(f"\nPourcentage de lignes avec une seule valeur unique dans 'apet_manual': {percentage_single_element:.2f}%")
print(f"\nDifficulté moyenne': {int(mean_rating)}")