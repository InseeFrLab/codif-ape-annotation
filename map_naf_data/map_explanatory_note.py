import os
import s3fs

import pandas as pd

from lxml import etree

fs = s3fs.S3FileSystem(
        client_kwargs={"endpoint_url": os.getenv("S3_ENDPOINT")},
        key=os.getenv("AWS_ACCESS_KEY_ID"),
        secret=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )

# Get files
#NAF_mapping_one_to_many_old = pd.read_parquet('s3://projet-ape/NAF-revision/NAF_mapping_one_to_many_translation.parquet', filesystem=fs)

""" Gestion table de correspondance """

# File path (.xls)
excel_file_path = "Table de correspondances NAF rev.2 - NAF 2025.xls"

# Import as dataframe
correspondance_NAF = pd.read_excel(excel_file_path, sheet_name='1) correspondance NAFNAF')
#print(correspondance_NAF.columns.values)
# Select columns
correspondance_NAF = correspondance_NAF[['NAFold-code\n(code niveau sous-classe de la nomenclature actuelle)',
                                        'NAFold-intitulé\n(niveau sous-classe)',
                                        'NAFnew-code\n(code niveau sous-classe de la nomenclature 2025, correspondance logique avec les NAFold-codes)', 
                                        'NAFnew-intitulé\n(niveau sous-classe)',
                                        'Common content identified for the NACEold and the NACEnew\n(niveau classe)',
                                        'évaluation profil pratique NAFold pour JXXXX',
                                        'ligne à supprimer =1 pour correspondance de codes APE (travail JXXX)']]

# Drop the first row (index 0)
correspondance_NAF = correspondance_NAF.drop(0)

# Rename the column
correspondance_NAF.rename(columns={'NAFold-code\n(code niveau sous-classe de la nomenclature actuelle)': 'NAF2008',
                                   'NAFold-intitulé\n(niveau sous-classe)': 'NAF2008_intitule',
                                   'NAFnew-code\n(code niveau sous-classe de la nomenclature 2025, correspondance logique avec les NAFold-codes)': 'NAF2025',
                                   'NAFnew-intitulé\n(niveau sous-classe)' : 'NAF2025_intitule',
                                   'Common content identified for the NACEold and the NACEnew\n(niveau classe)': 'common_content',
                                   'évaluation profil pratique NAFold pour JXXXX': 'is_multivoque',
                                   'ligne à supprimer =1 pour correspondance de codes APE (travail JXXXX)' : 'filtre_a_supp'}, inplace=True)

# Filter
correspondance_NAF = correspondance_NAF[correspondance_NAF['is_multivoque'] == 'C']
correspondance_NAF = correspondance_NAF[correspondance_NAF['filtre_a_supp'] != 1]
#print(correspondance_NAF)
# Delete .
correspondance_NAF['NAF2008'] = correspondance_NAF['NAF2008'].str.replace(".", "")
correspondance_NAF['NAF2025'] = correspondance_NAF['NAF2025'].str.replace(".", "")


""" Gestion sous-classes notes explicatives """

# File path (.xls)
excel_file_path = "Traduction DNE toutes sections NACE et NAF_enrichi.xlsx"

# Import as dataframe
data_explanatory_notes = pd.read_excel(excel_file_path, sheet_name='Notes NACE Rev21 et NAF2025')

# Select columns
data_explanatory_notes = data_explanatory_notes[["Code.NACE.Rev.2.1", "Comprend", "Comprend.aussi", "Ne.comprend.pas",'indic.NACE', 'indic.NAF']]

# Delete .
data_explanatory_notes['Code.NACE.Rev.2.1'] = data_explanatory_notes['Code.NACE.Rev.2.1'].str.replace(".", "")

# Filter to get subclasses and classes notes
explanatory_notes_subclasses = data_explanatory_notes[(data_explanatory_notes['Code.NACE.Rev.2.1'].str.len() == 5) | ((data_explanatory_notes['Code.NACE.Rev.2.1'].str.len() == 4) & (data_explanatory_notes['indic.NACE']== 1) & (data_explanatory_notes['indic.NAF']== 1))]
common_content = data_explanatory_notes[data_explanatory_notes['Code.NACE.Rev.2.1'].str.len() == 4]

# Rename columns
explanatory_notes_subclasses.rename(columns={'Code.NACE.Rev.2.1': 'NAF2025',
                                  'Comprend': 'comprend_niv5_belge',
                                  'Comprend.aussi': 'comprend_aussi_niv5_belge',
                                  'Ne.comprend.pas': 'ne_comprend_pas_niv5_belge'}, inplace=True)

common_content.rename(columns={'Code.NACE.Rev.2.1': 'normalized_key',
                               'Comprend': 'comprend_niv4_belge',
                               'Comprend.aussi': 'comprend_aussi_niv4_belge',
                               'Ne.comprend.pas': 'ne_comprend_pas_niv4_belge'}, inplace=True)

# Merge data
explanatory_notes_subclasses["normalized_key"] = explanatory_notes_subclasses["NAF2025"].str.slice(0,4)
explanatory_notes = pd.merge(explanatory_notes_subclasses, common_content, on='normalized_key', how='left')

print(explanatory_notes_subclasses.head(20))
print(explanatory_notes.head(20))

# Add Y in the end of class without division
explanatory_notes["NAF2025"]= explanatory_notes["NAF2025"].str.replace(r'^\d{4}$',lambda m: m.group(0)+'Y', regex=True)

print(explanatory_notes.head(20))

""" Combine all """

correspondance_NAF = pd.merge(correspondance_NAF, explanatory_notes, on='NAF2025', how='left')
#print(print(correspondance_NAF[correspondance_NAF.duplicated(subset=['NAF2025'], keep=False)]))

# Group by 'task_id', aggregate with custom functions
NAF_mapping = correspondance_NAF.groupby('NAF2008').agg({'NAF2008_intitule': (lambda x: list(x.fillna('Indisponible pour le moment'))),
                                                    'NAF2025': (lambda x: list(x.fillna('Indisponible pour le moment'))),
                                                    'NAF2025_intitule': (lambda x: list(x.fillna('Indisponible pour le moment'))),
                                                    'comprend_niv5_belge': lambda x: list(x.fillna('Indisponible pour le moment')),
                                                    'comprend_aussi_niv5_belge': lambda x: list(x.fillna('Indisponible pour le moment')),
                                                    'ne_comprend_pas_niv5_belge': lambda x: list(x.fillna('Indisponible pour le moment')),
                                                    'comprend_niv4_belge': lambda x: list(x.fillna('Indisponible pour le moment')),
                                                    'comprend_aussi_niv4_belge': lambda x: list(x.fillna('Indisponible pour le moment')),
                                                    'ne_comprend_pas_niv4_belge': lambda x: list(x.fillna('Indisponible pour le moment'))}).reset_index()
NAF_mapping = NAF_mapping[['NAF2008', 'NAF2008_intitule', 'NAF2025', 'NAF2025_intitule','comprend_niv5_belge','comprend_aussi_niv5_belge','ne_comprend_pas_niv5_belge','comprend_niv4_belge','comprend_aussi_niv4_belge','ne_comprend_pas_niv4_belge']]
NAF_mapping_one_to_many = NAF_mapping[NAF_mapping['NAF2025'].apply(len) > 1]
NAF_mapping_one_to_one = NAF_mapping[NAF_mapping['NAF2025'].apply(len) == 1]


print(NAF_mapping_one_to_many.head)


#NAF_mapping = pd.merge(NAF_mapping_one_to_many, NAF_mapping_one_to_many_old, on='NAF2008', how='left')
#print(NAF_mapping_one_to_many_old)
#print(NAF_mapping_one_to_many)
#print(len(NAF_mapping_one_to_many))

# NAF_mapping_one_to_one.to_parquet('s3://projet-ape/NAF-revision/NAF_mapping_one_to_one_provisoire_belge.parquet', compression=None, filesystem=fs)
NAF_mapping_one_to_many.to_parquet('NAF_mapping_one_to_many_provisoire_belge.parquet', compression=None)

#print(NAF_mapping_one_to_many)
#print(pd.read_parquet("NAF_mapping_one_to_many_provisoire_belge.parquet"))
