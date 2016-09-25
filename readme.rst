====================
Convert JWPCE to CSV
====================

Converts files of JWPCE dictionary entries to an Anki importable CSV.

**Note** this has most recently specifically been tested on python 3.4.3. Using
python 2.7 may not be supported.

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
japanese is the "back".

**Note** The JWPCE files must be in utf-8 format, not the default it uses.
That's another job for the future.

------------
Installation
------------

**NOTE** This has most recently been tested using 3.4.3. Running this on 2.7
or below may not be supported.

Run::

    pip install -r requirements.txt

-----
Usage
-----

    Python main.py infile.txt outfile.csv

-------
Testing
-------

While conventional python unit testing uses "self.assert" I find this to be
verbose for simple cases, so instead use assert unless there is a reason not
to like with "assertRaises".

This uses py.test as the test runner. Nose should still work, but will require
extra effort to get things like coverage in place.

To install py.test run::

    pip install -r requirements-dev.txt

After running the following command in the main directory will run the test::

    py.test

This will run the tests, run coverage, and run flake8 as a linter. The
settings for this can be found in the "setup.cfg" file.

----
TODO
----

* Update to work with the default JWPCE encoding.
* Update the tests to use the standard python unittest framwork.
* Update coverage, although the gui code might be problematic.
