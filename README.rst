====================
Convert JWPCE to CSV
====================

Converts files of JWPCE dictionary entries to an Anki importable CSV.

**Note** this has most recently specifically been tested on python 3.6.7. Using
python 2.7 is not supported.

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

As well as a reversed version where the translation is the "front" and the
Japanese is the "back".

**Note** The JWPCE files must be in utf-8 format, not the default it uses.
That's another job for the future.

-----------
Development
-----------

Install requirements::

    pip install -r requirements.txt
    pip install -r requirements-dev.txt

Install the package locally::

    pip install -e .

This will allow using the entry points from the setup.py file.

Running the command line version::

    jwpce_convert

Running the gui version::

    jwpce_convert_gui

------------------
Command Line Usage
------------------

    jwpce_convert [-h] [--output OUTPUT] [--force] input

-------
Testing
-------

This uses py.test as the test runner.  The requirements are included in
requirements-dev.txt.

After installing those in the main directory run::

    py.test tests

This will run the tests, run coverage, and run flake8 as a linter. The
settings for this can be found in the "setup.cfg" file.

----
TODO
----

* Update to work with the default JWPCE encoding.
* Update coverage, although the gui code might be problematic.
