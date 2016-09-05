''' Gui version of the program using PySide. '''

from PySide.QtGui import (
    QDialog,
    QFileDialog,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
)

from jwpce_convert import read_file, write_file
from jwpce_convert.validate import (
    OutputExistsError,
    ValidateError,
    generate_output_file,
    validate,
)


class MainForm(QDialog):
    ''' The main (and so far only) form. '''

    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

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

        input_path = self.input_path.text()
        # Should be set below when opening input the file.
        output_path = self.output_path.text()

        try:
            input_path, output_path = validate(input_path, output_path)
        except OutputExistsError as e:
            overwrite = QMessageBox.warning(self,
                self.tr('JWPCE conversion'),
                self.tr('The output file already exits. Overwrite it?'),
                QMessageBox.Yes | QMessageBox.No)

            if overwrite == QMessageBox.No:
                return

        except ValidateError as e:
            QMessageBox.warning(self,
                                self.tr('JWPCE conversion'),
                                self.tr(str(e)),
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
        # TODO - While testing anyway
        dialog.setDirectory('.')
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter('Text files (*.txt)')

        if dialog.exec_():
            input_files = dialog.selectedFiles()
            input_file = input_files[0]
            self.input_path.setText(input_file)

            out_path = generate_output_file(input_file)

            self.output_path.setText(out_path)
