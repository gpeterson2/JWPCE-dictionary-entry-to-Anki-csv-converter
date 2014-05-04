#! /usr/bin/env python

''' Converts a file of JWPCE dictionary defenitions to an Anki CSV.

    *Note* The file must start in utf-8 format, not the default JWPCE format.
    At some point this may change, but for the moment I don't want to deal
    with the various file encodings.
'''

import argparse
import os

from convert import read_file, write_file

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

    # TODO - move path validation to a separate location to share with the
    # gui program?

    # Kick it out if the input doesn't exist
    if not (os.path.exists(input_path) or os.path.isfile(input_path)):
        print('Input file does not exist or is not a file.')
        return 1

    # If not provided create the output file path.
    if not output_path:
        # Get name without extension
        output_path = os.path.splitext(input_path)[0]

    # Make sure it ends with csv.
    if not output_path.endswith('.csv'):
        output_path = output_path + '.csv'

    # Check if output already exists.
    # if force is specified allow it to overwrite.
    if os.path.exists(output_path) and not force:
        print('Output file already exists')
        return 1

    # Shouldn't happen, but hey.
    if (input_path == output_path):
        print('Failure: Input and output are the same.')
        return 1

    contents = read_file(input_path)
    write_file(output_path, contents)

if __name__ == '__main__':
    main()

