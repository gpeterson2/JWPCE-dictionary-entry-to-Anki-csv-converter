from jwpce_convert.validate import (
    ValidateError,
    generate_output_file,
    validate,
)


class TestValidate:

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

    def test_validate_no_input(self):

        passed = False
        error_msg = ''

        input_path = ''
        output_path = 'test.csv'

        try:
            validate(input_path, output_path)
        except ValidateError as e:
            passed = True
            error_msg = e.message

        assert passed is True
        assert error_msg == 'Input file not specified.'

    def test_validate_no_output(self):

        passed = False
        error_msg = ''

        input_path = 'test.txt'
        output_path = ''

        try:
            validate(input_path, output_path)
        except ValidateError as e:
            passed = True
            error_msg = e.message

        assert passed is True
        assert error_msg == 'Output file not specified.'
