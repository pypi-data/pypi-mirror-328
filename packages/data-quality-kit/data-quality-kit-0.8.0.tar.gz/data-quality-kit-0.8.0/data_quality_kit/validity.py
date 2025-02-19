from pandas import DataFrame
import pandas as pd
import re

def assert_that_there_are_not_nulls(df: DataFrame, field_name: str) -> bool:
    """
    Checks for null values in a specified column of a DataFrame.

    Parameters:
    df : The DataFrame to check.
    field_name : The name of the column to check for null values.

    Returns:
    bool: True if there are null values in the column, False if there are no null values.

    Raises:
    TypeError: If the field_name is not a string.
    ValueError: If the field_name is not a column in the DataFrame.
    """
    if not isinstance(field_name, str):
        raise TypeError('Error: Field name must be a string.')

    if field_name not in df.columns:
        raise ValueError(f'Error: Field "{field_name}" not in DataFrame.')

    return df[field_name].isnull().any()

def assert_regex_format(df: pd.DataFrame, column_name: str, regex: str) -> bool:
    """
    Validates whether all values in the specified column of a DataFrame match the format
    defined by the provided regular expression, including null and empty values.

    Parameters:
    ----------
    df : The DataFrame containing the column to validate.
    column_name : The name of the column to validate.
    regex : The regular expression used to validate each value in the column.

    Returns:
    -------
    bool
        Returns `True` if all values in the column match the regular expression.
        Returns `False` if any value does not match.

    Exceptions:
    -----------
    ValueError:
        Raised if the DataFrame is empty, the column does not exist, or the regex is invalid.
    """
    
    if column_name not in df.columns:
        raise ValueError(f"The column '{column_name}' does not exist in the DataFrame.")
    
    try:
        pattern = re.compile(regex)
    except re.error as e:
        raise ValueError(f"Invalid regular expression: {e}")

    for value in df[column_name]:
        if pd.isnull(value) or value == '' or not pattern.fullmatch(value):
            return False
    return True