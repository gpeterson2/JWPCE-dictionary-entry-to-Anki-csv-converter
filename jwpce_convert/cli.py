#! /usr/bin/env python

''' Converts a file of JWPCE dictionary definitions to an Anki CSV.

    Console version.

    *Note* The file must start in utf-8 format, not the default JWPCE format.
    At some point this may change, but for the moment I don't want to deal
    with the various file encodings.
'''

import argparse

import jwpce_convert.jwpce_convert.convert as convert
import jwpce_convert.jwpce_convert.validate as validate


def main():
    description = '''
        Converts a file of JWPCE dictionary definitions to an Anki CSV.

        If output is not provided it will be generated from the input file
        name.

        For example "test.txt" will become "test.csv". If the ouptut file
        already exists then it will not be overwritten unless "--force" is
        provided.
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
        output_path = validate.generate_output_file(input_path)

    try:
        input_path, output_path = validate.validate(input_path, output_path)
    except validate.OutputExistsError as e:
        if not force:
            print('Error: {0}'.format(e))
            return 1
    except validate.ValidateError as e:
        print('Error: {0}'.format(e))
        return 1

    contents = convert.read_file(input_path)
    convert.write_file(output_path, contents)


if __name__ == '__main__':
    main()
