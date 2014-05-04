#! /usr/bin/env python

''' Converts a file of JWPCE dictionary defenitions to an Anki CSV.

    GUI version.
'''

import os
import sys

from PySide.QtCore import (Qt, SIGNAL)
from PySide.QtGui import (QApplication, QDialog, QGridLayout, QLabel,
        QPushButton, QLineEdit, QFileDialog, QMessageBox)

from jwpce_convert import read_file, write_file

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # TODO - set a min width
        self.setMinimumWidth(500)

        self.label = QLabel('Input file...')
        self.input_path = QLineEdit()
        self.output_path = QLineEdit()

        convert_button = QPushButton('Convert')
        input_dialog_button = QPushButton('Browse...')
        # TODO - provide a dialog for ouput
        # possibly just a folder picker then they have to provide the name?

        layout = QGridLayout()
        layout.addWidget(QLabel('Input Path:'), 0, 0)
        layout.addWidget(self.input_path, 0, 1)
        layout.addWidget(input_dialog_button, 0, 2)
        layout.addWidget(QLabel('Output Path:'), 1, 0)
        layout.addWidget(self.output_path, 1, 1)
        layout.addWidget(convert_button, 2, 0)
        self.setLayout(layout)

        convert_button.clicked.connect(self.convert)
        input_dialog_button.clicked.connect(self.open_input_file_dialog)

        self.setWindowTitle('JWPCE to CSV convert')

    def convert(self):
        ''' Converts the input file and writes to the output file. '''

        # TODO move the path validation to a separate class to share with the
        # console program?

        # Make sure that the input path exists.
        input_path = self.input_path.text()
        if not (os.path.exists(input_path) or os.path.isfile(input_path)):
            QMessageBox.warning(self,
                self.tr('JWPCE conversion'),
                self.tr('The input file does not exist or if not a file'),
                QMessageBox.Ok)
            return

        output_path = self.output_path.text()

        # If not provided create the output file path.
        if not output_path:
            # Get name without extension
            output_path = os.path.splitext(input_path)[0]

        # Make sure it ends with csv.
        if not output_path.endswith('.csv'):
            output_path = output_path + '.csv'

        # Check if the output file already exists.
        # If so prompt to overwrite.
        if os.path.exists(output_path):
            overwrite = QMessageBox.warning(self,
                self.tr('JWPCE conversion'),
                self.tr('The output file already exits. Overwrite it?'),
                QMessageBox.Yes | QMessageBox.No)

            if overwrite == QMessageBox.No:
                return

        # Shouldn't happen, but hey.
        if input_path == output_path:
            QMessageBox.warning(self,
                self.tr('JWPCE conversion'),
                self.tr('Input and output paths are the same.'),
                QMessageBox.Ok)
            return

        # TODO - add in some kind of progress indicator?
        contents = read_file(input_path)
        write_file(output_path, contents)

        QMessageBox.information(self,
            self.tr('JWPCE conversion'),
            self.tr('The conversion is complete.'),
            QMessageBox.Ok)

    def open_input_file_dialog(self):
        ''' Opens and input file dialog and sets the output based on that.

            The output file path will be the same as the input, but renamed
            .csv instead of .txt.
        '''

        dialog = QFileDialog(self)
        # While testing anyway
        dialog.setDirectory('.')
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter('Text files (*.txt)')

        if dialog.exec_():
            input_files = dialog.selectedFiles()
            input_file = input_files[0]
            self.input_path.setText(input_file)

            # automatically set the output based on the input.
            # here as a helper so users won't have to type it in themselves.
            path, in_file = os.path.split(input_file)
            out_file = in_file.replace('txt', 'csv')
            out_path = os.path.join(path, out_file)
            self.output_path.setText(out_path)

def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

