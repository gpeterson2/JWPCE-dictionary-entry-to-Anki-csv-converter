====================
Convert JWPCE to CSV
====================

Converts files of JWPCE dictionary entries to an Anki importable CSV.

Where JWPCE_ is a Windows based Japanese text input and dictionary program
and Anki_ is a flash card program.

.. _JWPCE: http://www.physics.ucla.edu/~grosenth/jwpce.html
.. _Anki: http://ankisrs.net/

There are two types of definitions:

1. kanji [kana] translations
2. kana translations

This program will output:

1. kanji, "kana (html) newline translations"
2. kana, "translations"

As well as a translation, kana/kanji version as well.

At some point it would be nice to start with a list of pure Japanese words
have the program search for definitions and then write that out to a csv,
completely bypassing JWPCE. But that will be a job for the future.

*Note* The JWPCE files must be in utf-8 format, not the default it uses.
That's another job for the future.

-----
Usage
-----
    Python main.py infile.txt outfile.csv

------------
Requirements
------------

To use the GUI version you must have pyside installed.

----
TODO
----

* Add some tests for the conversion as well as reading/writing.
* Convert the input/output to use file like objects to make testing easier.
* Review the current splitting logic, the kanji and kana versions could
  possibly be combined in some way.
* Check/Convert the file's encoding

