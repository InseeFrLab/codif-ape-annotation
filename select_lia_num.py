import pandas as pd

from lxml import etree

""" Import data to get NACE rev.2.1 taxonomy """
excel_file_path = "LIste liasses pour exercices Label Studio.xlsx"

data_lia_num = pd.read_excel(excel_file_path, sheet_name="Feuille1")
data = pd.read_parquet("data.parquet")

merged_data = data.merge(data_lia_num, left_on='liasse_numero', right_on='Liasse', how='inner')

merged_data_1 = merged_data[merged_data["Priorité (1 = à faire faire)"]==1]
merged_data_2 = merged_data[merged_data["Priorité (1 = à faire faire)"]!=1]

merged_data_1.to_parquet("formation_examples_prioritaires.parquet")
merged_data_2.to_parquet("formation_examples_moins_prioritaires.parquet")