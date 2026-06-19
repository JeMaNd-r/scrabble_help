# Scrabble help app

This application provides suggestions for most-scoring words based on a given set of letters.

## Getting Started

Download the repository and run the *app.py* file using a terminal in VS Code or a command line interpreter (e.g. CMD). You will be asked to provide the letters without deliminator. Afterwards, the top 5 words scoring most points will be shown with their score. The score is based on the Scrabble scoring system. 

### Prerequisites

- Python 3.14.5

Following Python libraries are used for data preparation:

- pypdf-6.13.3 (load and extract text from PDF)
- re (extract string pattern)
- json (save and read JSON to store word list)

### Installing

Install the required Python version. Then, install the required Python packages (e.g., using `py -m pip install [package]` in the command line).

When running `py app.py` in the project directory, the programm should run and wait for the user input (i.e., letters)

If you plan to also run the *prepare_data.py*, please make sure to download the/a PDF with words first (see [Acknowledgements](#acknowledgments)).


## Running the tests

You can test if you installed the correct Python version using `py --version`. You correct Python version might be also accessible using `python` or `python3` instead of `py`.


## Contributing

This is a personal learning project and is not open to contributions. Thank you for your understanding.


## Versioning

Potential updates:
- allow users to correct the scoring system
- allow users to insert which position(s) in the word can get doubled or tripled points, or make the whole word count doubled or tripled
- provide leftover letters if choosing one of the top 5 words


## Author

  - Romy Zeiss


## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details

## Acknowledgments

The list of German Scrabble words was extracted [here]("https://scrabble-info.de/wp-content/uploads/2021/03/LernWB_A4_4Spalten_2021.pdf") from the [scrabble-info.de]("https://scrabble-info.de/wortlisten/sonstige-listen/") website. It does not contain a complete list of Scrabble words, but it does serve the purpose of this simple app, as the app should support finding words.

The code to read and extract text from PDF was based on the tutorial from Geeks for Geeks [here](https://www.geeksforgeeks.org/python/working-with-pdf-files-in-python/) and [here](https://www.geeksforgeeks.org/python/convert-pdf-to-txt-file-using-python/).
