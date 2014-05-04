#! /usr/bin/env python

''' Converts a file of JWPCE dictionary defenitions to an Anki CSV.

    *Note* The file must start in utf-8 format, not the default JWPCE format.
    At some point this may change, but for the moment I don't want to deal
    with the various file encodings.
'''

import os
import sys

from jwpce_convert import read_file, write_file

def main():
    args = sys.argv

    # TODO - use argparse module
    if len(args) != 3:
        print('Usage main.py input output')
        sys.exit(1)

    # TODO - move path validation to a separate location to share with the
    # gui program?
    input_path = args[1]
    if not (os.path.exists(input_path) or os.path.isfile(input_path)):
        print('Input file does not exist or is not a file.')

    # TODO - if not provided, then base the outpufile file name on the input?
    output_path = args[2]
    # TODO if output exists, print message
    # prompt the user, and/or add an option to force overwrite it.

    # Shouldn't happen, but hey.
    if (input_path == output_path):
        print('Failure: Input and output are the same.')

    contents = read_file(input_path)
    write_file(output_path, contents)

if __name__ == '__main__':
    main()

