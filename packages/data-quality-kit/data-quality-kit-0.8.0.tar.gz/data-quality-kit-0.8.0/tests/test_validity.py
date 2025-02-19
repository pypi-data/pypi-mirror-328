from assertpy import assert_that

from tests.global_test_data import df_global

from data_quality_kit.validity import assert_that_there_are_not_nulls,assert_regex_format


def test_assert_that_there_are_not_nulls_over_nulls_present():
    assert_that(assert_that_there_are_not_nulls(df_global, 'column2')).is_true()


def test_assert_that_there_are_not_nulls_over_no_nulls():
    assert_that(assert_that_there_are_not_nulls(df_global, 'column1')).is_false()
    assert_that(assert_that_there_are_not_nulls(df_global, 'column3')).is_false()


def test_assert_that_there_are_not_nulls_over_invalid_column_type():
    error_msg = 'Error: Field name must be a string.'
    assert_that(assert_that_there_are_not_nulls).raises(TypeError).when_called_with(
        df_global, 123
    ).is_equal_to(error_msg)


def test_assert_that_there_are_not_nulls_over_invalid_column_name():
    error_msg = 'Error: Field "nonexistent" not in DataFrame.'
    assert_that(assert_that_there_are_not_nulls).raises(ValueError).when_called_with(
        df_global, "nonexistent"
    ).is_equal_to(error_msg)

def test_assert_regex_format_with_all_values_matching_pattern():
    regex = r"ES[0-9]{4}"  
    result = assert_regex_format(df_global, 'valid_column', regex)
    assert_that(result).is_equal_to(True)

def test_assert_regex_format_with_some_values_not_matching_pattern():
    regex = r"ES[0-9]{4}"  
    result = assert_regex_format(df_global, 'invalid_column', regex)
    assert_that(result).is_equal_to(False)

def test_assert_regex_format_with_nonexistent_column():
    regex = r"ES[0-9]{4}"  
    assert_that(assert_regex_format).raises(ValueError).when_called_with(
        df_global, 'nonexistent_column', regex
    ).is_equal_to("The column 'nonexistent_column' does not exist in the DataFrame.")

def test_assert_regex_format_with_invalid_regex():
    invalid_regex = r"[\K]"
    assert_that(assert_regex_format).raises(ValueError).when_called_with(
        df_global, 'valid_column', invalid_regex
    ).is_equal_to("Invalid regular expression: bad escape \\K at position 1")