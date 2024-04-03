import pandas as pd
from lxml import etree

""" Download data """
# File path (.xls)
excel_file_path = "Table de correspondances NAF rev.2 - NAF 2025.xls"

# Import as dataframe
correspondance_NAF = pd.read_excel(excel_file_path, sheet_name='0) (a compléter)')
print(correspondance_NAF.columns.values)
# Select columns
correspondance_NAF = correspondance_NAF[['NAFold-code\n(a compléter)',
                                        'NAFold-intitulé\n(a compléter)',
                                        'NAFnew-code\n(a compléter)', 
                                        'NAFnew-intitulé\n(a compléter)',
                                        'ligne à supprimer (a compléter)']]

# Drop the first row (index 0)
correspondance_NAF = correspondance_NAF.drop(0)

# Rename the column
correspondance_NAF.rename(columns={'NAFold-code\n(a compléter)': 'NAF2008', 
                                   'NAFold-intitulé\n(a compléter)': 'NAF2008_intitule', 
                                   'NAFnew-code\n(a compléter)': 'NAF2025', 
                                   'NAFnew-intitulé\n(a compléter)' : 'NAF2025_intitule',
                                   'ligne à supprimer (a compléter)' : 'filtre_a_supp'}, inplace=True)

# Filter
correspondance_NAF = correspondance_NAF[correspondance_NAF['filtre_a_supp'] != 1]
print(correspondance_NAF)
# Delete .
correspondance_NAF['NAF2008'] = correspondance_NAF['NAF2008'].str.replace(".", "")
correspondance_NAF['NAF2025'] = correspondance_NAF['NAF2025'].str.replace(".", "")

# Group by NAF2008 to get list of one-to-many NAF2008-NAF2025

# Group by 'task_id', aggregate with custom functions
NAF_mapping = correspondance_NAF.groupby('NAF2008').agg({'NAF2025': (lambda x: list(x)), 'NAF2025_intitule': (lambda x: list(x))}).reset_index()  # Include 'other_column' with 'first'
NAF_mapping = NAF_mapping[['NAF2008', 'NAF2025', 'NAF2025_intitule']]
NAF_mapping_one_to_many = NAF_mapping[NAF_mapping['NAF2025'].apply(len) > 1]
NAF_mapping_one_to_one = NAF_mapping[NAF_mapping['NAF2025'].apply(len) == 1]

print(NAF_mapping_one_to_many.columns)
print(NAF_mapping_one_to_many)

correspondance_NAF.to_parquet('NAF_correspondance_table.parquet', compression=None)
NAF_mapping_one_to_one.to_parquet('NAF_mapping_one_to_one.parquet', compression=None)
NAF_mapping_one_to_many.to_parquet('NAF_mapping_one_to_many.parquet', compression=None)