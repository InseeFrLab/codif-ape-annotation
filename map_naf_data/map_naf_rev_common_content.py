import pandas as pd
from lxml import etree

from translator import translate

""" Download data """
# File path (.xls)
excel_file_path = "data/Table de correspondances NAF rev.2 - NAF 2025.xls"

# Import as dataframe
correspondance_NAF = pd.read_excel(excel_file_path, sheet_name='1) correspondance NAFNAF')
print(correspondance_NAF.columns.values)
# Select columns
correspondance_NAF = correspondance_NAF[['NAFold-code\n(code niveau sous-classe de la nomenclature actuelle)',
                                        'NAFold-intitulé\n(niveau sous-classe)',
                                        'NAFnew-code\n(code niveau sous-classe de la nomenclature 2025, correspondance logique avec les NAFold-codes)', 
                                        'NAFnew-intitulé\n(niveau sous-classe)',
                                        'Common content identified for the NACEold and the NACEnew\n(niveau classe)',
                                        'ligne à supprimer =1 pour correspondance de codes APE (travail JXXXXX)']]

# Drop the first row (index 0)
correspondance_NAF = correspondance_NAF.drop(0)

# Rename the column
correspondance_NAF.rename(columns={'NAFold-code\n(code niveau sous-classe de la nomenclature actuelle)': 'NAF2008',
                                   'NAFold-intitulé\n(niveau sous-classe)': 'NAF2008_intitule',
                                   'NAFnew-code\n(code niveau sous-classe de la nomenclature 2025, correspondance logique avec les NAFold-codes)': 'NAF2025',
                                   'NAFnew-intitulé\n(niveau sous-classe)' : 'NAF2025_intitule',
                                   'Common content identified for the NACEold and the NACEnew\n(niveau classe)': 'common_content',
                                   'ligne à supprimer =1 pour correspondance de codes APE (travail JXXXX)' : 'filtre_a_supp'}, inplace=True)
correspondance_NAF["common_content"] = correspondance_NAF["common_content"].astype(str)
correspondance_NAF["common_content_fr"] = correspondance_NAF["common_content"].apply(translate)
# print(correspondance_NAF["common_content"].iloc[348])
print(correspondance_NAF["common_content_fr"])
# Filter
correspondance_NAF = correspondance_NAF[correspondance_NAF['filtre_a_supp'] != 1]
print(correspondance_NAF)
# Delete .
correspondance_NAF['NAF2008'] = correspondance_NAF['NAF2008'].str.replace(".", "")
correspondance_NAF['NAF2025'] = correspondance_NAF['NAF2025'].str.replace(".", "")

# Group by NAF2008 to get list of one-to-many NAF2008-NAF2025

# Group by 'task_id', aggregate with custom functions
NAF_mapping = correspondance_NAF.groupby('NAF2008').agg({'NAF2008_intitule': (lambda x: list(x)), 'common_content_fr': (lambda x: list(x)),'NAF2025': (lambda x: list(x)),'NAF2025_intitule': (lambda x: list(x))}).reset_index()  # Include 'other_column' with 'first'
NAF_mapping = NAF_mapping[['NAF2008', 'NAF2008_intitule', 'common_content_fr', 'NAF2025', 'NAF2025_intitule']]
NAF_mapping_one_to_many = NAF_mapping[NAF_mapping['NAF2025'].apply(len) > 1]
NAF_mapping_one_to_one = NAF_mapping[NAF_mapping['NAF2025'].apply(len) == 1]

print(NAF_mapping_one_to_many.columns)
print(NAF_mapping_one_to_many)
print(NAF_mapping_one_to_many["common_content_fr"])

correspondance_NAF.to_parquet('NAF_correspondance_table.parquet', compression=None)
NAF_mapping_one_to_one.to_parquet('NAF_mapping_one_to_one.parquet', compression=None)
NAF_mapping_one_to_many.to_parquet('NAF_mapping_one_to_many.parquet', compression=None)