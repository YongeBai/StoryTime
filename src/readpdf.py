from pdfminer.high_level import extract_text

with open('output.txt', 'a') as f:
    f.writelines(extract_text('Einstein_Walter_Isaacson_Z-Library.pdf'))