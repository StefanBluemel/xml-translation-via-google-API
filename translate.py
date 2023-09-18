import xml.etree.ElementTree as ET
import sys
import time
from googletrans import Translator

def translate_text(text, counter, fails):
    try:
        translator = Translator()
        translation = translator.translate(text, src='en', dest='de')

        if translation and translation.text:
            counter += 1
            print(f'API-Aufruf {counter}: Übersetzung von "{text}" zu "{translation.text}" abgeschlossen.')
            return translation.text, fails, counter
        else:
            fails += 1
            print(f'------------------- Übersetzung FEHLGESCHLAGEN --------------------')
            return '', fails, counter
    except Exception as e:
        fails += 1
        print(f'------------------- Übersetzung FEHLGESCHLAGEN (Fehler: {str(e)}) --------------------')
        return '', fails, counter

def remove_ns0_prefix(xml_file):
    with open(xml_file, 'r', encoding='utf-8') as file:
        xml_content = file.read()
        xml_content = xml_content.replace('ns0:', '')

    with open(xml_file, 'w', encoding='utf-8') as file:
        file.write(xml_content)

def main():
    if len(sys.argv) < 3:
        print("Verwendung: translate_and_process_xml.py <input_xml_file> <output_xml_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    translation_count = 0
    translation_fails = 0

    tree = ET.parse(input_file)
    root = tree.getroot()

    ns = {'ns0': 'urn:oasis:names:tc:xliff:document:1.2'}

    for element in root.iterfind('.//ns0:trans-unit', namespaces=ns):
        source_element = element.find('ns0:source', namespaces=ns)
        target_element = element.find('ns0:target', namespaces=ns)

        if source_element is not None and target_element is not None and target_element.text is not None:
            source_content = source_element.text.strip()
            if target_element.text.strip() == '[NAB: NOT TRANSLATED]':
                time.sleep(0.26)
                if source_content is not None:
                    translated_content, translation_fails, translation_count = translate_text(source_content, translation_count, translation_fails)
                    if translated_content is not None:
                        target_element.text = translated_content

    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    remove_ns0_prefix(output_file)

    print(f'Insgesamt übersetzte Zeilen: {translation_count}')
    print(f'fehlgeschlagene Übersetzungen: {translation_fails}')

if __name__ == "__main__":
    main()
