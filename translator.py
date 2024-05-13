from transformers import pipeline


def translate(sentence):
    translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
    # Manage output format
    # Split the input sentence into lines
    lines = sentence.split('\n')
    print(lines)
    while '' in lines: lines.remove('')
    if len(lines) == 0:
        return ""
    if lines[0] == "the content of the NACE Rev 2 class is fully covered in the corresponding NACE Rev 2.1 class":
        return "même classe et scission claire au niveau des sous-classes dans la nouvelle NAF."
    # Translate each line individually and join them back
    translated_lines = []
    for line in lines:
        translated_line = translator(line)[0]['translation_text']
        translated_lines.append(translated_line)
    # Join the translated lines with newline characters
    translated_sentence = '\n'.join(translated_lines)
    print(translated_sentence)
    return translated_sentence
