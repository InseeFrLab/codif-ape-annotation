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

""" Choice section to display pre-annotations or NACE taxonomy """
# Create the second View element
second_view = etree.SubElement(root, "View") #, style="box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;")

""" Choice subsection to display question """
# Create the first nested level 1 View of the second View element
second_first_view = etree.SubElement(second_view, "View", style="box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;")
# Create the Header element within the first nested level 1 View of the second View element
header_element = etree.SubElement(second_first_view, "Header", value="Code NAF 2025 dans la liste ci-dessous ?")
# Display text of list of suggestions
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="liste_multivoque",
    value="$NAF2025_1 - $NAF2025_intitule_1 || $NAF2025_2 - $NAF2025_intitule_2 || $NAF2025_3 - $NAF2025_intitule_3 ||",
    highlightColor="#ff0000"
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="liste_multivoque",
    value="$NAF2025_4 - $NAF2025_intitule_4 || $NAF2025_5 - $NAF2025_intitule_5 || $NAF2025_6 - $NAF2025_intitule_6 ||",
    highlightColor="#ff0000"
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="liste_multivoque",
    value="$NAF2025_7 - $NAF2025_intitule_7 || $NAF2025_8 - $NAF2025_intitule_8 || $NAF2025_9 - $NAF2025_intitule_9 ||",
    highlightColor="#ff0000"
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="liste_multivoque",
    value="$NAF2025_10 - $NAF2025_intitule_10 || $NAF2025_11 - $NAF2025_intitule_11 || $NAF2025_12 - $NAF2025_intitule_12 ||",
    highlightColor="#ff0000"
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="liste_multivoque",
    value="$NAF2025_13 - $NAF2025_intitule_13 || $NAF2025_14 - $NAF2025_intitule_14 || $NAF2025_15 - $NAF2025_intitule_15 ||",
    highlightColor="#ff0000"
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="liste_multivoque",
    value="$NAF2025_16 - $NAF2025_intitule_16 || $NAF2025_17 - $NAF2025_intitule_17 ||$NAF2025_18 - $NAF2025_intitule_18 ||",
    highlightColor="#ff0000"
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="liste_multivoque",
    value="$NAF2025_19 - $NAF2025_intitule_19 || $NAF2025_20 - $NAF2025_intitule_20 || $NAF2025_21 - $NAF2025_intitule_21 ||",
    highlightColor="#ff0000"
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="liste_multivoque",
    value="$NAF2025_22 - $NAF2025_intitule_22 || $NAF2025_23 - $NAF2025_intitule_23 || $NAF2025_24 - $NAF2025_intitule_24 ||",
    highlightColor="#ff0000"
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="liste_multivoque",
    value="$NAF2025_25 - $NAF2025_intitule_25 || $NAF2025_26 - $NAF2025_intitule_26 || $NAF2025_27 - $NAF2025_intitule_27",
    highlightColor="#ff0000"
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="liste_multivoque",
    value="$NAF2025_28 - $NAF2025_intitule_28 || $NAF2025_29 - $NAF2025_intitule_29 || $NAF2025_30 - $NAF2025_intitule_30 ||",
    highlightColor="#ff0000"
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="liste_multivoque",
    value="$NAF2025_31 - $NAF2025_intitule_31 || $NAF2025_32 - $NAF2025_intitule_32 || $NAF2025_33 - $NAF2025_intitule_33 ||",
    highlightColor="#ff0000"
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="liste_multivoque",
    value="$NAF2025_34 - $NAF2025_intitule_34 || $NAF2025_35 - $NAF2025_intitule_35 || $NAF2025_36 - $NAF2025_intitule_36 ||",
    highlightColor="#ff0000"
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="liste_multivoque",
    value="$NAF2025_37 - $NAF2025_intitule_37 || $NAF2025_38 - $NAF2025_intitule_38 || $NAF2025_39 - $NAF2025_intitule_39",
    highlightColor="#ff0000"
)


question_choices = etree.SubElement(second_view, "Choices", name="NAF2008_OK", toName="text", choice="single", showInLine="true")
question_choice_1 = etree.SubElement(question_choices, "Choice", value="Oui", selected="true")
question_choice_2 = etree.SubElement(question_choices, "Choice", value="Non")

""" Choice subsubsection to display pre-annotations help if the answer is "Yes" (default choice) """
# Create the second first level 2 View of the second View element
second_first_first_view = etree.SubElement(second_first_view, "View", visibleWhen="choice-selected", whenTagName="NAF2008_OK")
# Create the Header element within the first nested level 1 View of the second View element
header_element = etree.SubElement(second_view, "Header", value="Choix du bon code NAF 2025")
choices = etree.SubElement(
    second_view,
    "Choices",
    name="Choisissez dans la liste",
    toName="text",
    choice="single",
    showInLine="true",
    visibleWhen="choice-selected",
    whenTagName="NAF2008_OK",
    whenChoiceValue="Oui"
)
question_choice_1 = etree.SubElement(choices, "Choice", value="$NAF2025_1")
question_choice_2 = etree.SubElement(choices, "Choice", value="$NAF2025_2")
question_choice_3 = etree.SubElement(choices, "Choice", value="$NAF2025_3")
question_choice_4 = etree.SubElement(choices, "Choice", value="$NAF2025_4")
question_choice_5 = etree.SubElement(choices, "Choice", value="$NAF2025_5")
question_choice_6 = etree.SubElement(choices, "Choice", value="$NAF2025_6")
question_choice_7 = etree.SubElement(choices, "Choice", value="$NAF2025_7")
question_choice_8 = etree.SubElement(choices, "Choice", value="$NAF2025_8")
question_choice_9 = etree.SubElement(choices, "Choice", value="$NAF2025_9")
question_choice_10 = etree.SubElement(choices, "Choice", value="$NAF2025_10")
question_choice_11 = etree.SubElement(choices, "Choice", value="$NAF2025_11")
question_choice_12 = etree.SubElement(choices, "Choice", value="$NAF2025_12")
question_choice_13 = etree.SubElement(choices, "Choice", value="$NAF2025_13")
question_choice_14 = etree.SubElement(choices, "Choice", value="$NAF2025_14")
question_choice_15 = etree.SubElement(choices, "Choice", value="$NAF2025_15")
question_choice_16 = etree.SubElement(choices, "Choice", value="$NAF2025_16")
question_choice_17 = etree.SubElement(choices, "Choice", value="$NAF2025_17")
question_choice_18 = etree.SubElement(choices, "Choice", value="$NAF2025_18")
question_choice_19 = etree.SubElement(choices, "Choice", value="$NAF2025_19")
question_choice_20 = etree.SubElement(choices, "Choice", value="$NAF2025_20")
question_choice_21 = etree.SubElement(choices, "Choice", value="$NAF2025_21")
question_choice_22 = etree.SubElement(choices, "Choice", value="$NAF2025_22")
question_choice_23 = etree.SubElement(choices, "Choice", value="$NAF2025_23")
question_choice_24 = etree.SubElement(choices, "Choice", value="$NAF2025_24")
question_choice_25 = etree.SubElement(choices, "Choice", value="$NAF2025_25")
question_choice_26 = etree.SubElement(choices, "Choice", value="$NAF2025_26")
question_choice_27 = etree.SubElement(choices, "Choice", value="$NAF2025_27")
question_choice_28 = etree.SubElement(choices, "Choice", value="$NAF2025_28")
question_choice_29 = etree.SubElement(choices, "Choice", value="$NAF2025_29")
question_choice_30 = etree.SubElement(choices, "Choice", value="$NAF2025_30")
question_choice_31 = etree.SubElement(choices, "Choice", value="$NAF2025_31")
question_choice_32 = etree.SubElement(choices, "Choice", value="$NAF2025_32")
question_choice_33 = etree.SubElement(choices, "Choice", value="$NAF2025_33")
question_choice_34 = etree.SubElement(choices, "Choice", value="$NAF2025_34")
question_choice_35 = etree.SubElement(choices, "Choice", value="$NAF2025_35")
question_choice_36 = etree.SubElement(choices, "Choice", value="$NAF2025_36")
question_choice_37 = etree.SubElement(choices, "Choice", value="$NAF2025_37")
question_choice_38 = etree.SubElement(choices, "Choice", value="$NAF2025_38")
question_choice_39 = etree.SubElement(choices, "Choice", value="$NAF2025_39")

# Create the third View element
third_view = etree.SubElement(root, "View", visibleWhen="choice-selected", whenTagName="NAF2008_OK", whenChoiceValue="Non")
# Create the Header element within the second View
taxonomy_element = etree.SubElement(
    third_view,
    "Taxonomy",
    name="taxonomy",
    toName="text",
    minWidth="1200px",
    placeholder="Cliquez et tapez le code APE retenu",
    leafsOnly="true",
    maxUsages="1"
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
tree.write("taxonomy_NAF2025.xml", pretty_print=True)
