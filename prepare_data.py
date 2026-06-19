# Script to process the list of German words

## Load required class
from PyPDF2 import PdfReader
import re
import json


## Define constants
PDF_FILE = "LernWB_A4_4Spalten_2021.pdf"
PAGE_NUMBERS = range(4, 90)
EXTRACT_AGAIN = False

OUTPUT_FILE = "wordlist.json"


## Function to extract words from PDF
def extract_page_content(pdf_file, page_numbers, output_file=None):
    
    # creating a pdf reader object
    try: 
        reader = PdfReader(pdf_file) 
    except:
        print("PDF file not found. Please make sure the PDF file is located in your current directory and check the README to get the PDF.")
        print("PDF file name:", pdf_file)
        break

    if output_file is None:
        file_name = re.sub(".pdf", ".txt", pdf_file)
    elif re.search(".txt", output_file):
        "Warning: Inserted file name is not .txt"
        file_name = str(output_file + ".txt")
    else :
        file_name = output_file

    # printing number of pages in pdf file
    print("# Extracting text from PDF to", file_name)
    print("Total number of pages:", len(reader.pages))
    print("Extracting pages", page_numbers, "...")

    with open(file_name, "w", encoding="utf-8") as f:
        for i in page_numbers:
            page = reader.pages[i]
            
            t = page.extract_text()
            if t:
                f.write(t + '\n')
    
    print("All pages extracted and saved to", file_name)


# Run extract function if not already done
if EXTRACT_AGAIN :
        extract_page_content(PDF_FILE, PAGE_NUMBERS)


## Function to get words from text
def get_words(output_file=None):
    if output_file is None:
        output_file = re.sub(".pdf", ".txt", PDF_FILE)

    print("# Extracting words from file", output_file, "...")
    word_list = []

    with open(output_file, "r", encoding="utf-8") as f:
        for line in f:
            if re.search(r"^[A-ZÄÖÜ]{2,}", line):
                word = re.findall(r"^[A-ZÄÖÜ]{2,}", line)[0]
                word_list.append(word)
            elif re.search(r"^=[A-ZÄÖÜ]{2,}", line):
                word = re.findall(r"^=([A-ZÄÖÜ]{2,})", line)[0]
                word_list.append(word)
            elif re.search(r"^\[[A-ZÄÖÜ]{2,}", line):
                word = re.findall(r"^\[([A-ZÄÖÜ]{2,})", line)[0]
                word_list.append(word)
        
    print("Extraction completed. Number of extracted words:", len(word_list))

    return word_list

WORD_LIST = get_words()


## Function to overwrite file (or save to different one)
def save_words(word_list, output_file):
    
    print("# Saving word list as JSON...")

    # The following code was based on:
    # Source - https://stackoverflow.com/a/59586116
    # Posted by Jay Mody, modified by community. See post 'Timeline' for change history
    # Retrieved 2026-06-19, License - CC BY-SA 4.0

    with open(output_file, 'w') as f:
        json.dump(word_list, f, indent=2)
        # indent=2 is not needed but makes the file human-readable 
        # if the data is nested

    print("Word list was saved to", output_file)

save_words(WORD_LIST, OUTPUT_FILE)