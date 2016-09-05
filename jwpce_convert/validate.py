#! /usr/bin/env python

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
    ''' Error when output exists so you can prompt to overwrite it. '''
    pass


def generate_output_file(input_path):
    ''' Generate an ouptut path based on the input path.

        :params input_path: Input file path.
    '''

    output_path = os.path.splitext(input_path)[0]

    if not output_path.endswith('.csv'):
        output_path = output_path + '.csv'

    return output_path


def validate(input_path, output_path):
    ''' Validates user input.

        :param input_path: Input file path.
        :param output_path: Output file path. If not provided it will be
                            generated.
    '''

    # Somehow passed in None or empty string
    if not input_path:
        raise ValidateError('Input file not specified.')

    if not output_path:
        raise ValidateError('Output file not specified.')

    # Kick it out if the input doesn't exist
    if not (os.path.exists(input_path) or os.path.isfile(input_path)):
        raise ValidateError('Input file does not exist or is not a file.')

    # Shouldn't happen, but hey.
    if (input_path == output_path):
        raise ValidateError('Input and output are the same.')

    # Check if output already exists.
    # if force is specified allow it to overwrite.
    if os.path.exists(output_path):
        raise OutputExistsError('Output file already exists')

    return (input_path, output_path)
