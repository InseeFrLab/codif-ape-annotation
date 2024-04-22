import pandas as pd
from lxml import etree

""" Download data from website to get NACE rev.2 taxonomy """
excel_file_path = "custom-taxonomy-template/table_NAF2-NA.xls"

intitule_ape = pd.read_excel("https://www.insee.fr/fr/statistiques/fichier/2028155/table_NAF2-NA.xls", sheet_name='Version avec niveau A 21')
intitule_section_division = pd.read_excel("https://www.insee.fr/fr/statistiques/fichier/2028155/niv_agreg_naf_rev_2.xls ", sheet_name='A 88')

""" Format data """

# Select columns
intitule_ape = intitule_ape[['SOUS CLASSE', 'INTITULE DE LA NAF rév. 2', 'CLASSE', 'DIVISION','SECTION']]
# Drop the first row (index 0)
intitule_ape = intitule_ape.drop(0)
# Forward fill NaN values in the 'Section' and 'Libellé des sections' columns
intitule_section_division['Section '] = intitule_section_division['Section '].ffill()
intitule_section_division['Libellé des sections'] = intitule_section_division['Libellé des sections'].ffill()
intitule_section_division['Code\nDivision'] = intitule_section_division['Code\nDivision'].astype(str).str.zfill(2)
# Rename the column
intitule_section_division.rename(columns={'Code\nDivision': 'Division', 'Intitulé ': 'Intitulé des divisions'}, inplace=True)
intitule_ape.rename(columns={'SOUS CLASSE': 'Sous-classe', 'INTITULE DE LA NAF rév. 2': 'Intitulé de la sous-classe', 'CLASSE': 'Classe', 'DIVISION': 'Division', 'SECTION': 'Section', }, inplace=True)
# Left join on 'ID' column
data_naf = pd.merge(intitule_ape, intitule_section_division, on='Division', how='left')

""" Configure XML label studio template """

# Create XML structure
root = etree.Element("View")

""" Header section to display information for annotation """
# Create the first View element
first_view = etree.SubElement(root, "View", style="box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;")

# Create the Header element within the first View
header_element = etree.SubElement(first_view, "Header", value="Déclaration")
# Choose auxiliary variables to display for annotation
text_element = etree.SubElement(first_view, "Text", name="text", value="Libellé --> $text_description", highlightColor="#ff0000")
text_element = etree.SubElement(first_view, "Text", name="c05", value="Pseudo type de liasse CERFA --> $type_", highlightColor="#ff9900")
text_element = etree.SubElement(first_view, "Text", name="evt", value="Type d'évènement --> $event", highlightColor="#00ff00")
text_element = etree.SubElement(first_view, "Text", name="nat", value="Nature d'activité --> $nature", highlightColor="#0000ff")
text_element = etree.SubElement(first_view, "Text", name="surf", value="Surface --> $surface", highlightColor="#ffcc00")


""" Choice section to display NACE taxonomy """
# Create the second View element
second_view = etree.SubElement(root, "View") #, style="box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;")
# Create the Header element within the second View

""" Show the result given by annotation """
# Create the Header element within the first nested level 1 View of the second View element
NAF2008_header = etree.SubElement(
    second_view, "Header", value="Code NAF 2008 donné"
)
NAF2008_view = etree.SubElement(second_view, "View", style="color:blue")
NAF2008_element = etree.SubElement(
    NAF2008_view,
    "Text",
    name="NAF2008",
    value="$apet_manual",
)

""" Validation section is annotation good or not """

header_element = etree.SubElement(
    second_view, "Header", value="Est-ce que le code NAF 2008  donné est correct ?"
)
question_choices = etree.SubElement(
    second_view,
    "Choices",
    name="NAF2008_OK",
    toName="text",
    choice="single",
    showInLine="true",
)
question_choice_1 = etree.SubElement(
    question_choices, "Choice", value="Oui", selected="true"
)
question_choice_2 = etree.SubElement(question_choices, "Choice", value="Non")

""" Taxonomy section """ 

# Create the third View element
third_view = etree.SubElement(
    root,
    "View",
    visibleWhen="choice-selected",
    whenTagName="NAF2008_OK",
    whenChoiceValue="Non",
)
# Create the Header element within the second View
taxonomy_element = etree.SubElement(
    third_view,
    "Taxonomy",
    name="taxonomy",
    toName="text",
    minWidth="1200px",
    placeholder="Cliquez et tapez le code APE retenu",
    leafsOnly="true",
    maxUsages="1",
)

section_choice = etree.SubElement(taxonomy_element, "Choice", value="Inclassable", alias="XXXXX")
# Iterate over each branch and write to XML
for section, section_df in data_naf.groupby('Section'):
    section_label = section_df['Libellé des sections'].iloc[0]  # Assuming the label is the same for all rows in the section
    # Limit the string length to 70 characters and add "..." if it exceeds
    # section_label = (section_label[:47] + '...') if len(section_label) > 50 else section_label

    section_choice = etree.SubElement(taxonomy_element, "Choice", value=f"{section} - {section_label}", alias=section)
    # Add style to each View element within the taxonomy
    #section_choice.set("style", "box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;")

    for division, division_df in section_df.groupby('Division'):
        division_label = division_df['Intitulé des divisions'].iloc[0]  # Assuming the label is the same for all rows in the division
        # Limit the string length to 70 characters and add "..." if it exceeds
        # division_label = (division_label[:57] + '...') if len(division_label) > 60 else division_label
        division_choice = etree.SubElement(section_choice, "Choice", value=f"{division} - {division_label}", alias=division)
        # Add style to each View element within the taxonomy
        #division_choice.set("style", "box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;")
  
        for sous_classe, sous_classe_label in zip(division_df['Sous-classe'], division_df['Intitulé de la sous-classe']):
            # Limit the string length to 70 characters and add "..." if it exceeds
            # sous_classe_label = (sous_classe_label[:47] + '...') if len(sous_classe_label) > 50 else sous_classe_label
            code_ape = sous_classe.replace('.', '')
            sous_classe_choice = etree.SubElement(division_choice, "Choice", value=f"{sous_classe} // {code_ape} - {sous_classe_label}", alias=sous_classe)
            # Add style to each View element within the taxonomy
            #sous_classe_choice.set("style", "box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;")

""" Comment section (customized one as it's not available in Label Studio community) """
# Create the command View element
comment_view = etree.SubElement(root, "View")

# Create the Header element within the first View
header_element = etree.SubElement(comment_view, "Header", value="Commentaire")
text_element = etree.SubElement(comment_view, "TextArea", name="Remarques", toName="text", showSubmitButton="true", maxSubmissions="1", editable="true")

""" Create XML """
# Create ElementTree and write to file
tree = etree.ElementTree(root)
tree.write("taxonomy_NAF2008_validation.xml", pretty_print=True)
