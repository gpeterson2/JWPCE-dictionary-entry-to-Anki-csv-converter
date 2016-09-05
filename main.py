#! /usr/bin/env python

''' Converts a file of JWPCE dictionary defenitions to an Anki CSV.

    Console version.

    *Note* The file must start in utf-8 format, not the default JWPCE format.
    At some point this may change, but for the moment I don't want to deal
    with the various file encodings.
'''

# TODO - merge the console and gui version?
# If paramaters are used then run this, otherwise the gui?

import argparse

from jwpce_convert import read_file, write_file
from jwpce_convert.validate import (
    OutputExistsError,
    ValidateError,
    generate_output_file,
    validate,
)


def main():
    description = '''
        Converts a file of JWPCE dictionary definitions to an Anki CSV.

        If output is not provided it will be genrated from the input file name.
    '''

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('input', help='Text input')
    parser.add_argument('--output', '-o', help='CSV output')
    parser.add_argument('--force', '-f', action='store_true',
                        help='Overwrites output if it already exists')

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    force = args.force

    if not output_path:
        output_path = generate_output_file(input_path)

    try:
        input_path, output_path = validate(input_path, output_path)
    except OutputExistsError as e:
        if not force:
            print('Error: ' + str(e))
            return 1
    except ValidateError as e:
        print('Error: ' + str(e))
        return 1

    contents = read_file(input_path)
    write_file(output_path, contents)


if __name__ == '__main__':
    main()
