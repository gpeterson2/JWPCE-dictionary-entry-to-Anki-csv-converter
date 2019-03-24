''' Gui version of the program using PySide. '''

from PySide2 import QtWidgets

import jwpce_convert.jwpce_convert.convert as convert
import jwpce_convert.jwpce_convert.validate as validate


class MainForm(QtWidgets.QDialog):
    ''' The main (and so far only) form. '''

    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        self.setMinimumWidth(500)

        self.label = QtWidgets.QLabel('Input file...')
        self.input_path = QtWidgets.QLineEdit()
        self.output_path = QtWidgets.QLineEdit()

        convert_button = QtWidgets.QPushButton('Convert')
        input_dialog_button = QtWidgets.QPushButton('Browse...')

        layout = QtWidgets.QGridLayout()
        layout.addWidget(QtWidgets.QLabel('Input Path:'), 0, 0)
        layout.addWidget(QtWidgets.QLabel('Output Path:'), 1, 0)
        layout.addWidget(self.output_path, 1, 1)
        layout.addWidget(convert_button, 2, 0)
        self.setLayout(layout)

        convert_button.clicked.connect(self.convert)
        input_dialog_button.clicked.connect(self.open_input_file_dialog)

        self.setWindowTitle('JWPCE to CSV convert')

    def convert(self):
        ''' Converts the input file and writes to the output file. '''

        input_path = self.input_path.text()
        # Should be set below when opening input the file.
        output_path = self.output_path.text()

        try:
            input_path, output_path = validate.validate(input_path, output_path)
        except validate.OutputExistsError as e:
            # E128 Technically this should be indented more, but I feel that
            # hurts readability in this case.
            overwrite = QtWidgets.QMessageBox.warning(self,
                self.tr('JWPCE conversion'),
                self.tr('The output file already exits. Overwrite it?'),
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)  # noqa: E128

            if overwrite == QtWidgets.QMessageBox.No:
                return

        except validate.ValidateError as e:
            error_message = '{0}'.format(e)
            QtWidgets.QMessageBox.warning(self,
                                          self.tr('JWPCE conversion'),
                                          self.tr(error_message),
                                          QtWidgets.QMessageBox.Ok)
            return

        # TODO - add in some kind of progress indicator?
        contents = convert.read_file(input_path)
        convert.write_file(output_path, contents)

        QtWidgets.QMessageBox.information(self,
                                          self.tr('JWPCE conversion'),
                                          self.tr('The conversion is complete.'),
                                          QtWidgets.QMessageBox.Ok)

    def open_input_file_dialog(self):
        ''' Opens and input file dialog and sets the output based on that.

            The output file path will be the same as the input, but renamed
            .csv instead of .txt.
        '''

        dialog = QtWidgets.QFileDialog(self)
        # TODO - While testing anyway
        dialog.setDirectory('.')
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        dialog.setNameFilter('Text files (*.txt)')

        if dialog.exec_():
            input_files = dialog.selectedFiles()
            input_file = input_files[0]
            self.input_path.setText(input_file)

            out_path = validate.generate_output_file(input_file)

            self.output_path.setText(out_path)
