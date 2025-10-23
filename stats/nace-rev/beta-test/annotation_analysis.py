import os
import s3fs

import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq


fs = s3fs.S3FileSystem(
        client_kwargs={"endpoint_url": os.getenv("S3_ENDPOINT")},
        key=os.getenv("AWS_ACCESS_KEY_ID"),
        secret=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )

# Get files
data = pd.read_parquet('annotated_data_triple_annotation.parquet')

#data = data[data['annotator'] != 'chdelacou@gmail.com']

# Agrégation par 'id' et création de listes uniques pour 'col1'
aggregated_df = data.groupby('task_id').agg({'text_description': lambda x: x,
                                                'apet_manual': lambda x: list(x),
                                                     'rating' : list,
                                                     'annotator': list
}).reset_index()
print(len(aggregated_df))
aggregated_df['text_description'] = aggregated_df['text_description'].apply(lambda x: x[0])

# Ne filtrer que les cas concernés par la triple annotation
aggregated_df = aggregated_df[aggregated_df['annotator'].apply(lambda x: len(x) == 3)] # 'veronique.legal3@insee.fr'  'chdelacou@gmail.com' 'soso1999@mail.fr'
#aggregated_df = aggregated_df[['task_id','text_description', 'apet_manual','rating']]
#aggregated_df.to_csv('sans_A.csv')

print(aggregated_df)

aggregated_df['apet_manual'] = aggregated_df['apet_manual'].apply(
    lambda x: [max(set(x), key=x.count)] if list(x).count(max(set(x), key=x.count)) > len(x)/2 else list(x)
)
print(aggregated_df)
discordance_majorite_df = aggregated_df[aggregated_df['apet_manual'].apply(lambda x: len(x) == 3)]
discordance_majorite_df = discordance_majorite_df[['task_id','text_description', 'apet_manual','rating']]
discordance_majorite_df.to_csv('discordance_majorite.csv')

# pq.write_table(pa.Table.from_pandas(aggregated_df), f"label-studio/annotation-campaign-2024/rev-NAF2025/eval-annotation/triple-annotation/preprocessed/annotated_data_triple_annotation.parquet", filesystem=fs)

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
print(len(aggregated_df))