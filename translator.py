import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from send_payload import send_payload

def translate(text):
    translated_text = send_payload(f'Translate in chinese:"{text}"')
    # Use this code to verify that all the text you want to translate will be translated.
    # translated_text = 'ZH:' + text
    return translated_text

def translate_epub(input_path, output_path):
    # Load a epub file
    book = epub.read_epub(input_path)

    # Translate all html file in extracted epub file
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        # Get HTML ccontent and do preprocesses
        html_content = item.get_content().decode('utf-8')
        html_content = html_content.replace('\\n','\n')

        # Use BeautifulSoup to parse html content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Translate
        for tag in soup.find_all(string=True):
            if tag.parent.name not in ['p','div','strong','span','i','em']:
                origin_text = str(tag.string)
                tag.string.replace_with(origin_text)
            elif tag.string not in ['','\n']:
                translated_text = translate(tag.string)
                tag.string.replace_with(translated_text)

        translated_html = soup.prettify()

        item.set_content(translated_html)

    epub.write_epub(output_path, book)

output_file_path = 'output.epub'
translate_epub('Your book.epub', output_file_path)