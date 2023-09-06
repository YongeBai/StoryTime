import os

from utils import process_metadata, tts

BOOK_TITLE = "Example"
AUTHOR = "Example"
PATH_TO_TXT_FILES = os.path.join(os.getcwd(), "books", BOOK_TITLE, "book_txt")

CHAPTER_NUM = 1


def main():
    files = os.listdir(PATH_TO_TXT_FILES)
    files.sort(
        key=lambda file_name: os.path.getmtime(
            os.path.join(PATH_TO_TXT_FILES, file_name)
        )
    )

    for file in files:
        full_path = os.path.join(PATH_TO_TXT_FILES, file)
        tts(full_path, BOOK_TITLE)
        process_metadata(full_path, BOOK_TITLE, CHAPTER_NUM, AUTHOR)
        CHAPTER_NUM += 1


if __name__ == "__main__":
    main()
