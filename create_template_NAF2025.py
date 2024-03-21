import pandas as pd
from lxml import etree

""" Import data to get NACE rev.2.1 taxonomy """
excel_file_path = "data_naf.xlsx"

data_naf = pd.read_excel(excel_file_path, sheet_name='data_naf')

""" Format data """

# Forward fill NaN values in the 'Section' and 'Libellé des sections' columns
data_naf['Division'] = data_naf['Division'].astype(str).str.zfill(2)

""" Configure XML label studio template """

# Create XML structure
root = etree.Element("View")

""" Header section to display information for annotation """
# Create the first View element
first_view = etree.SubElement(root, "View", style="box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;")

# Create the Header element within the first View
header_element = etree.SubElement(first_view, "Header", value="Déclaration")
# Choose auxiliary variables to display for annotation
text_element = etree.SubElement(first_view, "Text", name="text", value="Activité la plus importante dans l'établissement --> $activ_pr_lib_et", highlightColor="#ff0000")
text_element = etree.SubElement(first_view, "Text", name="act_exec", value="Activité(s) exercée(s) dans l'établissement --> $activ_ex_lib_et", highlightColor="#ff0000")
text_element = etree.SubElement(first_view, "Text", name="act_ent", value="Activité(s) de l'entreprise --> $activ_pr_lib", highlightColor="#ff0000")
text_element = etree.SubElement(first_view, "Text", name="c05", value="Type de liasse --> $liasse_type", highlightColor="#ff9900")
text_element = etree.SubElement(first_view, "Text", name="evt", value="Type d'évènement --> $evenement_type", highlightColor="#00ff00")
text_element = etree.SubElement(first_view, "Text", name="nat", value="Nature d'activité --> $activ_nat_et_intitule", highlightColor="#0000ff")
text_element = etree.SubElement(first_view, "Text", name="nat_autre", value="Autre nature d'activité --> $activ_nat_lib_et", highlightColor="#0000ff")
text_element = etree.SubElement(first_view, "Text", name="surf", value="Surface --> $activ_surf_et", highlightColor="#ffcc00")
text_element = etree.SubElement(first_view, "Text", name="cj", value="Catégorie juridique --> $cj_intitule", highlightColor="#00ff00")
text_element = etree.SubElement(first_view, "Text", name="nom_comm_et", value="Nom commercial de l'établissement --> $nom_comm_et", highlightColor="#00ff00")
text_element = etree.SubElement(first_view, "Text", name="enseigne_et1", value="Enseigne n°1 de l'établissement --> $enseigne_et1", highlightColor="#00ff00")
text_element = etree.SubElement(first_view, "Text", name="saisonnalite", value="Caractère permanent(P)/saisonnier(S) de l'activité générale --> $activ_perm_et", highlightColor="#00ff00")

""" Choice section to display NACE taxonomy """
# Create the second View element
second_view = etree.SubElement(root, "View") #, style="box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;")
# Create the Header element within the second View
taxonomy_element = etree.SubElement(second_view, "Taxonomy", name="taxonomy", toName="text", minWidth="1200px", placeholder="Cliquez et tapez le code APE retenu", leafsOnly="true", maxUsages="1")

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
tree.write("taxonomy_NAF2025.xml", pretty_print=True)
