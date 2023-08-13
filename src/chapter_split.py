import ebooklib

from ebooklib import epub

def extract_chapters(path):
    book = epub.read_epub(path)
    
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            print('NAME: ', item.get_name())
            print(item.get_body_content())

    return [item for item in book.get_items() if item.get_type() == ebooklib.ITEM_DOCUMENT]

extract_chapters("src/test.epub")