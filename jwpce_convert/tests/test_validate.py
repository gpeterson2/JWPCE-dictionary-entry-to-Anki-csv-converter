import unittest

from jwpce_convert.validate import (
    ValidateError,
    generate_output_file,
    validate,
)


class TestValidate(unittest.TestCase):

    def test_generate_output_file_non_csv(self):

        input_path = 'test.txt'
        expected = 'test.csv'

        result = generate_output_file(input_path)

        assert result == expected

    def test_generate_output_file_csv(self):

        input_path = 'test.csv'
        expected = 'test.csv'

        result = generate_output_file(input_path)

        assert result == expected

    def test_generate_output_file_no_extension(self):

        input_path = 'test'
        expected = 'test.csv'

        result = generate_output_file(input_path)

        assert result == expected

    def test_validate_no_input(self):

        input_path = ''
        output_path = 'test.csv'

        expected_msg = 'Input file not specified.'
        with self.assertRaises(ValidateError, msg=expected_msg):
            validate(input_path, output_path)

    def test_validate_no_output(self):

        input_path = 'test.txt'
        output_path = ''

        expected_msg = 'Output file not specified.'
        with self.assertRaises(ValidateError, msg=expected_msg):
            validate(input_path, output_path)
