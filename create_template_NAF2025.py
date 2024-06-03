import pandas as pd
from lxml import etree

""" Import data to get NACE rev.2.1 taxonomy """
excel_file_path = "data_naf.xlsx"

data_naf = pd.read_excel(excel_file_path, sheet_name="data_naf")

""" Format data """

# Forward fill NaN values in the 'Section' and 'Libellé des sections' columns
data_naf["Division"] = data_naf["Division"].astype(str).str.zfill(2)

""" Configure XML label studio template """

# Create XML structure
root = etree.Element("View")

""" Header section to display information for annotation """
# Create the first View element
first_view = etree.SubElement(
    root,
    "View",
    style="box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;",
)

# Create the Header element within the first View
header_element = etree.SubElement(first_view, "Header", value="Déclaration")
# Choose auxiliary variables to display for annotation
text_element = etree.SubElement(
    first_view,
    "Text",
    name="text",
    value="Libellé de l'activité la plus importante --> $libelle",
    highlightColor="#ff0000",
)
text_element = etree.SubElement(
    first_view,
    "Text",
    name="c05",
    value="Pseudo type de liasse CERFA --> $liasse_type",
    highlightColor="#ff9900",
)
text_element = etree.SubElement(
    first_view,
    "Text",
    name="emetteur",
    value="Emetteur --> $emetteur",
    highlightColor="#ff9900",
)
text_element = etree.SubElement(
    first_view,
    "Text",
    name="evt",
    value="Type d'évènement --> $evenement_type",
    highlightColor="#00ff00",
)
text_element = etree.SubElement(
    first_view,
    "Text",
    name="nat",
    value="Nature d'activité --> $activ_nat_et_intitule",
    highlightColor="#0000ff",
)
text_element = etree.SubElement(
    first_view,
    "Text",
    name="nat_autre",
    value="Autre nature d'activité --> $activ_nat_lib_et",
    highlightColor="#0000ff",
)
text_element = etree.SubElement(
    first_view,
    "Text",
    name="surf",
    value="Surface --> $activ_surf_et",
    highlightColor="#ffcc00",
)
text_element = etree.SubElement(
    first_view,
    "Text",
    name="cj",
    value="Catégorie juridique --> $cj_intitule",
    highlightColor="#00ff00",
)
text_element = etree.SubElement(
    first_view,
    "Text",
    name="nom_comm_et",
    value="Nom commercial de l'établissement --> $nom_comm_et",
    highlightColor="#00ff00",
)
text_element = etree.SubElement(
    first_view,
    "Text",
    name="enseigne_et1",
    value="Enseigne n°1 de l'établissement --> $enseigne_et1",
    highlightColor="#00ff00",
)
text_element = etree.SubElement(
    first_view,
    "Text",
    name="saisonnalite",
    value="Caractère permanent(P)/saisonnier(S) de l'activité générale --> $activ_perm_et",
    highlightColor="#00ff00",
)

""" Choice section to display labeling suggestions or NACE taxonomy """
# Create the second View element
second_view = etree.SubElement(
    root, "View"
)  # , style="box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;")

# Create the Header element within the first nested level 1 View of the second View element
NAF2008_header = etree.SubElement(
    second_view, "Header", value="Code NAF 2008"
)
NAF2008_view = etree.SubElement(second_view, "View", style="color:blue")
NAF2008_element = etree.SubElement(
    NAF2008_view,
    "Text",
    name="NAF2008",
    value="$NAF2008_code_intitule",
)

""" Choice subsection to display question """
# Collapse as an accordion
collapse = etree.SubElement(second_view, "Collapse", accordion="false", bordered="true")
panel = etree.SubElement(collapse, "Panel", value="Voir sous-classes NAF 2025 proposés et common content de la classe associée")
# Create the first nested level 1 View of the second View element
second_first_view = etree.SubElement(
    panel, "View", style="box-shadow: 2px 2px 2px #777;"
)
# Create the Header element within the first nested level 1 View of the second View element
# header_element = etree.SubElement(second_first_view, "Header", value="Code NAF 2025 dans la liste ci-dessous ?")
# Display text of list of suggestions
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_1",
    value="1) $NAF2025_code_intitule_1",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_1",
    value="$common_content_fr_1",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_2",
    value="2) $NAF2025_code_intitule_2",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_2",
    value="$common_content_fr_2",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_3",
    value="3) $NAF2025_code_intitule_3",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_3",
    value="$common_content_fr_3",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_4",
    value="4) $NAF2025_code_intitule_4",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_4",
    value="$common_content_fr_4",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_5",
    value="5) $NAF2025_code_intitule_5",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_5",
    value="$common_content_fr_5",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_6",
    value="6) $NAF2025_code_intitule_6",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_6",
    value="$common_content_fr_6",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_7",
    value="7) $NAF2025_code_intitule_7",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_7",
    value="$common_content_fr_7",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_8",
    value="8) $NAF2025_code_intitule_8",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_8",
    value="$common_content_fr_8",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_9",
    value="9) $NAF2025_code_intitule_9",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_9",
    value="$common_content_fr_9",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_10",
    value="10) $NAF2025_code_intitule_10",
)

question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_10",
    value="$common_content_fr_10",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_11",
    value="11) $NAF2025_code_intitule_11",
)

question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_11",
    value="$common_content_fr_11",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_12",
    value="12) $NAF2025_code_intitule_12",
)

question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_12",
    value="$common_content_fr_12",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_13",
    value="13) $NAF2025_code_intitule_13",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_13",
    value="$common_content_fr_13",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_14",
    value="14) $NAF2025_code_intitule_14",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_14",
    value="$common_content_fr_14",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_15",
    value="15) $NAF2025_code_intitule_15",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_15",
    value="$common_content_fr_15",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_16",
    value="16) $NAF2025_code_intitule_16",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_16",
    value="$common_content_fr_16",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_17",
    value="17) $NAF2025_code_intitule_17",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_17",
    value="$common_content_fr_17",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_18",
    value="18) $NAF2025_code_intitule_18",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_18",
    value="$common_content_fr_18",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_19",
    value="19) $NAF2025_code_intitule_19",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_19",
    value="$common_content_fr_19",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_20",
    value="20) $NAF2025_code_intitule_20",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_20",
    value="$common_content_fr_20",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_21",
    value="21) $NAF2025_code_intitule_21",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_21",
    value="$common_content_fr_21",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_22",
    value="22) $NAF2025_code_intitule_22",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_22",
    value="$common_content_fr_22",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_23",
    value="23) $NAF2025_code_intitule_23",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_23",
    value="$common_content_fr_23",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_24",
    value="24) $NAF2025_code_intitule_24",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_24",
    value="$common_content_fr_24",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_25",
    value="25) $NAF2025_code_intitule_25",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_25",
    value="$common_content_fr_25",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_26",
    value="26) $NAF2025_code_intitule_26",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_26",
    value="$common_content_fr_26",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_27",
    value="27) $NAF2025_code_intitule_27",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_27",
    value="$common_content_fr_27",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_28",
    value="28) $NAF2025_code_intitule_28",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_28",
    value="$common_content_fr_28",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_29",
    value="29) $NAF2025_code_intitule_29",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_29",
    value="$common_content_fr_29",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_30",
    value="30) $NAF2025_code_intitule_30",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_30",
    value="$common_content_fr_30",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_31",
    value="31) $NAF2025_code_intitule_31",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_31",
    value="$common_content_fr_31",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_32",
    value="32) $NAF2025_code_intitule_32",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_32",
    value="$common_content_fr_32",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_33",
    value="33) $NAF2025_code_intitule_33",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_33",
    value="$common_content_fr_33",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_34",
    value="34) $NAF2025_code_intitule_34",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_34",
    value="$common_content_fr_34",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_35",
    value="35) $NAF2025_code_intitule_35",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_35",
    value="$common_content_fr_35",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_36",
    value="36) $NAF2025_code_intitule_36",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_36",
    value="$common_content_fr_36",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_37",
    value="37) $NAF2025_code_intitule_37",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_37",
    value="$common_content_fr_37",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_38",
    value="38) $NAF2025_code_intitule_38",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_38",
    value="$common_content_fr_38",
    granularity="paragraph",
)
NAF2025_view = etree.SubElement(second_first_view, "View", style="color:green")
question_element = etree.SubElement(
    NAF2025_view,
    "Text",
    name="liste_multivoque_39",
    value="39) $NAF2025_code_intitule_39",
)
question_element = etree.SubElement(
    second_first_view,
    "Text",
    name="common_content_fr_39",
    value="$common_content_fr_39",
    granularity="paragraph",
)

# Create the Header element within the first nested level 1 View of the second View element
header_element = etree.SubElement(
    second_view, "Header", value="Code NAF 2025 dans la liste ci-dessus ?"
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

""" Choice subsubsection to display pre-annotations help if the answer is "Yes" (default choice) """
# Create the second first level 2 View of the second View element
second_first_first_view = etree.SubElement(
    second_first_view, "View", visibleWhen="choice-selected", whenTagName="NAF2008_OK"
)
# Create the Header element within the first nested level 1 View of the second View element
header_element = etree.SubElement(
    second_view, "Header", value="Choix du bon code NAF 2025"
)
choices = etree.SubElement(
    second_view,
    "Choices",
    name="Choisissez dans la liste",
    toName="text",
    choice="single",
    showInLine="true",
    visibleWhen="choice-selected",
    whenTagName="NAF2008_OK",
    whenChoiceValue="Oui",
)
question_choice_1 = etree.SubElement(choices, "Choice", value="$NAF2025_1", hint="voir 1er code proposé dans la liste")
question_choice_2 = etree.SubElement(choices, "Choice", value="$NAF2025_2", hint="voir 2eme code proposé dans la liste")
question_choice_3 = etree.SubElement(choices, "Choice", value="$NAF2025_3", hint="voir 3eme code proposé dans la liste")
question_choice_4 = etree.SubElement(choices, "Choice", value="$NAF2025_4", hint="voir 4eme code proposé dans la liste")
question_choice_5 = etree.SubElement(choices, "Choice", value="$NAF2025_5", hint="voir 5eme code proposé dans la liste")
question_choice_6 = etree.SubElement(choices, "Choice", value="$NAF2025_6", hint="voir 6eme code proposé dans la liste")
question_choice_7 = etree.SubElement(choices, "Choice", value="$NAF2025_7", hint="voir 7eme code proposé dans la liste")
question_choice_8 = etree.SubElement(choices, "Choice", value="$NAF2025_8", hint="voir 8eme code proposé dans la liste")
question_choice_9 = etree.SubElement(choices, "Choice", value="$NAF2025_9", hint="voir 9eme code proposé dans la liste")
question_choice_10 = etree.SubElement(choices, "Choice", value="$NAF2025_10", hint="voir 10eme code proposé dans la liste")
question_choice_11 = etree.SubElement(choices, "Choice", value="$NAF2025_11", hint="voir 11eme code proposé dans la liste")
question_choice_12 = etree.SubElement(choices, "Choice", value="$NAF2025_12", hint="voir 12eme code proposé dans la liste")
question_choice_13 = etree.SubElement(choices, "Choice", value="$NAF2025_13", hint="voir 13eme code proposé dans la liste")
question_choice_14 = etree.SubElement(choices, "Choice", value="$NAF2025_14", hint="voir 14eme code proposé dans la liste")
question_choice_15 = etree.SubElement(choices, "Choice", value="$NAF2025_15", hint="voir 15eme code proposé dans la liste")
question_choice_16 = etree.SubElement(choices, "Choice", value="$NAF2025_16", hint="voir 16eme code proposé dans la liste")
question_choice_17 = etree.SubElement(choices, "Choice", value="$NAF2025_17", hint="voir 17eme code proposé dans la liste")
question_choice_18 = etree.SubElement(choices, "Choice", value="$NAF2025_18", hint="voir 18eme code proposé dans la liste")
question_choice_19 = etree.SubElement(choices, "Choice", value="$NAF2025_19", hint="voir 19eme code proposé dans la liste")
question_choice_20 = etree.SubElement(choices, "Choice", value="$NAF2025_20", hint="voir 20eme code proposé dans la liste")
question_choice_21 = etree.SubElement(choices, "Choice", value="$NAF2025_21", hint="voir 21eme code proposé dans la liste")
question_choice_22 = etree.SubElement(choices, "Choice", value="$NAF2025_22", hint="voir 22eme code proposé dans la liste")
question_choice_23 = etree.SubElement(choices, "Choice", value="$NAF2025_23", hint="voir 23eme code proposé dans la liste")
question_choice_24 = etree.SubElement(choices, "Choice", value="$NAF2025_24", hint="voir 24eme code proposé dans la liste")
question_choice_25 = etree.SubElement(choices, "Choice", value="$NAF2025_25", hint="voir 25eme code proposé dans la liste")
question_choice_26 = etree.SubElement(choices, "Choice", value="$NAF2025_26", hint="voir 26eme code proposé dans la liste")
question_choice_27 = etree.SubElement(choices, "Choice", value="$NAF2025_27", hint="voir 27eme code proposé dans la liste")
question_choice_28 = etree.SubElement(choices, "Choice", value="$NAF2025_28", hint="voir 28eme code proposé dans la liste")
question_choice_29 = etree.SubElement(choices, "Choice", value="$NAF2025_29", hint="voir 29eme code proposé dans la liste")
question_choice_30 = etree.SubElement(choices, "Choice", value="$NAF2025_30", hint="voir 30eme code proposé dans la liste")
question_choice_31 = etree.SubElement(choices, "Choice", value="$NAF2025_31", hint="voir 31eme code proposé dans la liste")
question_choice_32 = etree.SubElement(choices, "Choice", value="$NAF2025_32", hint="voir 32eme code proposé dans la liste")
question_choice_33 = etree.SubElement(choices, "Choice", value="$NAF2025_33", hint="voir 33eme code proposé dans la liste")
question_choice_34 = etree.SubElement(choices, "Choice", value="$NAF2025_34", hint="voir 34eme code proposé dans la liste")
question_choice_35 = etree.SubElement(choices, "Choice", value="$NAF2025_35", hint="voir 35eme code proposé dans la liste")
question_choice_36 = etree.SubElement(choices, "Choice", value="$NAF2025_36", hint="voir 36eme code proposé dans la liste")
question_choice_37 = etree.SubElement(choices, "Choice", value="$NAF2025_37", hint="voir 37eme code proposé dans la liste")
question_choice_38 = etree.SubElement(choices, "Choice", value="$NAF2025_38", hint="voir 38eme code proposé dans la liste")
question_choice_39 = etree.SubElement(choices, "Choice", value="$NAF2025_39", hint="voir 39eme code proposé dans la liste")

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

section_choice = etree.SubElement(
    taxonomy_element, "Choice", value="Inclassable", alias="XXXXX"
)
# Iterate over each branch and write to XML
for section, section_df in data_naf.groupby("Section"):
    section_label = section_df["Libellé des sections"].iloc[
        0
    ]  # Assuming the label is the same for all rows in the section
    # Limit the string length to 70 characters and add "..." if it exceeds
    # section_label = (section_label[:47] + '...') if len(section_label) > 50 else section_label

    section_choice = etree.SubElement(
        taxonomy_element, "Choice", value=f"{section} - {section_label}", alias=section
    )
    # Add style to each View element within the taxonomy
    # section_choice.set("style", "box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;")

    for division, division_df in section_df.groupby("Division"):
        division_label = division_df["Intitulé des divisions"].iloc[
            0
        ]  # Assuming the label is the same for all rows in the division
        # Limit the string length to 70 characters and add "..." if it exceeds
        # division_label = (division_label[:57] + '...') if len(division_label) > 60 else division_label
        division_choice = etree.SubElement(
            section_choice,
            "Choice",
            value=f"{division} - {division_label}",
            alias=division,
        )
        # Add style to each View element within the taxonomy
        # division_choice.set("style", "box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;")

        for sous_classe, sous_classe_label in zip(
            division_df["Sous-classe"], division_df["Intitulé de la sous-classe"]
        ):
            # Limit the string length to 70 characters and add "..." if it exceeds
            # sous_classe_label = (sous_classe_label[:47] + '...') if len(sous_classe_label) > 50 else sous_classe_label
            code_ape = sous_classe.replace(".", "")
            sous_classe_choice = etree.SubElement(
                division_choice,
                "Choice",
                value=f"{sous_classe} // {code_ape} - {sous_classe_label}",
                alias=sous_classe,
            )
            # Add style to each View element within the taxonomy
            # sous_classe_choice.set("style", "box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;")

""" Comment section (customized one as it's not available in Label Studio community) """
# Create the command View element
comment_view = etree.SubElement(root, "View")

# Create the Header element within the first View
header_element = etree.SubElement(comment_view, "Header", value="Commentaire")
text_element = etree.SubElement(
    comment_view,
    "TextArea",
    name="Remarques",
    toName="text",
    showSubmitButton="true",
    maxSubmissions="1",
    editable="true",
)

""" Difficulty rating section  """
# Create the command View element
rating_view = etree.SubElement(root, "View")

# Create the Header element within the first View
header_element = etree.SubElement(comment_view, "Header", value="Difficulté ressentie")
text_element = etree.SubElement(
    rating_view,
    "Text",
    name="diff",
    value="Notez votre ressenti sur une échelle de 1 à 5",
    highlightColor="#ff0000",
)
rating_element = etree.SubElement(
    rating_view,
    "Rating",
    name="rating",
    toName="diff",
    defaultValue="5",
    maxRating="5",
    icon="heart",
    size="large" 
)


""" Create XML """
# Create ElementTree and write to file
tree = etree.ElementTree(root)
tree.write("taxonomy_NAF2025.xml", pretty_print=True)
