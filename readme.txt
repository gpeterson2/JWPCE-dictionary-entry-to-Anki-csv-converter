Converts files of JWPCE dictionary entries to an Anki importable CSV.

Basically I've entered Japanese words into JWPCE in order to look up the
translations, saved those to files and now want to put them into the Anki
flashcard program.

There are two types of defenitions:
1. kanji [kana] translations
2. kana translations

This program will output:
For 1: kanji, "kana (html) newline translations"
For 2: kana, "translations"

At some point it would be nice to start with a list of pure Japanese words
have the program search for defenitions and then write that out to a csv,
completely bypassing JWPCE. But that will be a job for the future.

*Note* The JWPCE files must be in utf-8 format, not the default it uses.
That's another job for the future.

Usage:
    Python main.py infile.txt outfile.csv

TODO:
* Update the main to use argparse.
* Add some tests for the conversion as well as reading/writing.
* Convert the input/output to use file like objects to make testing easier.
* Review the current splitting logic, the kanji and kana versions could
    possibly be combined in some way.

