import os
import importlib
import torch

from utils import process_metadata
from RVC.rvc_utils import get_vc, vc_single

inference_utils = importlib.import_module("ai-voice-cloning.tortoise_utils")
tts = inference_utils.tts


BOOK_TITLE = "Example"
AUTHOR = "Example"
PATH_TO_TXT_FILES = os.path.join(os.getcwd(), "books", BOOK_TITLE, "book_txt")


def main():
    chapter_num = 1
    files = os.listdir(PATH_TO_TXT_FILES)
    files.sort(
        key=lambda file_name: os.path.getmtime(
            os.path.join(PATH_TO_TXT_FILES, file_name)
        )
    )

    for file in files:
        full_path = os.path.join(PATH_TO_TXT_FILES, file)

        # read chapter
        tts(full_path, BOOK_TITLE)

        # refine voice
        
        # vc_single(

        # process metadata
        process_metadata(full_path, BOOK_TITLE, chapter_num, AUTHOR)
        chapter_num += 1


if __name__ == "__main__":     
    model_path = ""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    is_half = True   
    get_vc(model_path=model_path, device=device, is_half=is_half)

    main()
