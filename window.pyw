#! /usr/bin/env python

''' Converts a file of JWPCE dictionary defenitions to an Anki CSV.

    GUI version.
'''

# TODO - merge the console and gui version?
# If no parameters are passed in then run this?

import sys

from PySide.QtGui import QApplication

from jwpce_convert.gui import MainForm

def main():
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

