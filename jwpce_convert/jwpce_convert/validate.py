#! /usr/bin/env python

''' Validation and path utils. '''

import os

__all__ = [
    'OutputExistsError',
    'ValidateError',
    'generate_output_file',
    'validate'
]


class ValidateError(Exception):
    ''' General validation error. '''

    pass


class OutputExistsError(Exception):
    ''' Error when output exists to force or prompt to overwrite it. '''

    pass


def generate_output_file(input_path):
    ''' Generate an output path based on the input path.

        If the path already ends in ".csv" nothing is done. If the file
        extension is missing or not .csv it will be set to .csv

        :params input_path: Input file path.
        :return: A path ending in ".csv"
        :rtype: str
    '''

    output_path = os.path.splitext(input_path)[0]

    if not output_path.endswith('.csv'):
        output_path = output_path + '.csv'

    return output_path


# TODO:
# - Split these, can't easily test that the files actually exist.
# - Add an option to ignore the OutputExistsError in case you want to force
#   creation of the output file.
def validate(input_path, output_path):
    ''' Validates user input.

        A ValidateError will be raised in the following conditions:

        - The input_path is missing.
        - The output_path is missing.
        - The input_path does not exist or is not a file.
        - The input_path matches the output path.

        An OutputExistsError will be raised in the following conditions:o

        - The ouptut_path alread exists on the file system. If you want to
          force creation of the file this can be ignored.

        :param input_path: Input file path.
        :param output_path: Output file path.
    '''

    # Somehow passed in None or empty string
    if not input_path:
        raise ValidateError('Input file not specified.')

    if not output_path:
        raise ValidateError('Output file not specified.')

    # Kick it out if the input doesn't exist
    if not (os.path.exists(input_path) or os.path.isfile(input_path)):
        raise ValidateError('Input file does not exist or is not a file.')

    # Yes, this did happen, which is why I want an explicit check for it.
    if (input_path == output_path):
        raise ValidateError('Input and output are the same.')

    # Check if output already exists.
    # TODO - If force is specified allow it to overwrite.
    if os.path.exists(output_path):
        raise OutputExistsError('Output file already exists')

    return (input_path, output_path)
