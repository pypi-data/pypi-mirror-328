#  Copyright (c) $YEAR$. Copyright (c) $YEAR$ Wrench.AI., Willem van der Schans, Jeong Kim
#
#  MIT License
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#  All works within the Software are owned by their respective creators and are distributed by Wrench.AI.
#
#  For inquiries, please contact Willem van der Schans through the official Wrench.AI channels or directly via GitHub at [Kydoimos97](https://github.com/Kydoimos97).
#

from typing import Any

from .._Internal._MockPandas import MockPandas

try:
    import pandas as pd
except ImportError:
    pd = MockPandas()


def standardize_none(data: Any, none_like_values: set = None, evaluate_as_string: bool = False) -> Any:
    """
    Recursively standardizes mistyped None values to proper None.
        --> ('', ' ', 'null', 'none', 'nan', 'n/a', 'na', 'undefined', 'missing', 'nil', 'void', 'blank')
    Handles pandas DataFrames and Series if pandas is available.

    :param data: The input data, which can be a single value, list, dict, pandas DataFrame, or Series.
    :param none_like_values: A set of custom placeholders that should be treated as None.
                             If not provided, defaults to common None-like placeholders.
    :param evaluate_as_string: Whether to attempt str() conversion on non-string values before checking.
    :return: The standardized data with all mistyped None values replaced with proper None.
    """
    # Default None-like values
    default_none_like_values = {
        '', ' ', 'null', 'none', 'nan', 'n/a', 'na', 'undefined', 'missing', 'nil', 'void', 'blank'
    }
    none_like_values = none_like_values or default_none_like_values

    if isinstance(data, pd.DataFrame):  # Handle DataFrame
        return data.applymap(lambda x: None if is_mistyped_none(x, none_like_values, evaluate_as_string) else standardize_none(x, none_like_values, evaluate_as_string))
    elif isinstance(data, pd.Series):  # Handle Series
        return data.apply(lambda x: None if is_mistyped_none(x, none_like_values, evaluate_as_string) else standardize_none(x, none_like_values, evaluate_as_string))
    elif isinstance(data, list):  # Handle List
        return [standardize_none(x, none_like_values, evaluate_as_string) for x in data]
    elif isinstance(data, dict):  # Handle Dict
        return {k: standardize_none(v, none_like_values, evaluate_as_string) for k, v in data.items()}
    else:  # Handle single values
        return None if is_mistyped_none(data, none_like_values, evaluate_as_string) else data


def is_mistyped_none(value: Any, none_like_values: set, evaluate_as_string: bool) -> bool:
    """
    Checks if a value is a mistyped None placeholder based on a custom set of None-like values.

    :param value: The value to check.
    :param none_like_values: A set of placeholders to treat as None.
    :param evaluate_as_string: Whether to attempt str() conversion on non-string values before checking.
    :return: True if the value is mistyped None, False otherwise.
    """
    # Check for None or NaN directly
    if pd.isna(value):  # Handles NaN and None
        return True

    # Check for None-like placeholders in strings
    if isinstance(value, str):
        if value.strip().lower() in none_like_values:
            return True

    # Evaluate non-string values as strings if enabled
    if evaluate_as_string:
        try:
            string_value = str(value).strip().lower()
            return string_value in none_like_values
        except Exception:
            pass  # Safely ignore conversion errors

    # Fallback for other types
    if isinstance(value, (list, dict, set)) and not value:  # Empty containers
        return True

    return False
