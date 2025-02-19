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


class MockPandas:
    """A mock pandas class for environments where pandas is not installed."""

    class DataFrame:
        """Mock DataFrame that safely handles calls but performs no actual operations."""
        def __init__(self, *args, **kwargs):
            self.data = kwargs.get("data", {})
            self.columns = list(self.data.keys()) if isinstance(self.data, dict) else []

        def applymap(self, func):
            """Mock applymap function to safely handle DataFrame element-wise operations."""
            return self  # No-op for applymap

        def itertuples(self, index: bool = True, name: str = "Row"):
            """Mock itertuples function to iterate over rows as named tuples."""
            for row in zip(*self.data.values()):
                yield tuple(row)

    class Series:
        """Mock Series that safely handles calls but performs no actual operations."""
        def __init__(self, data=None, *args, **kwargs):
            self.data = data

        def apply(self, func):
            """Mock apply function to safely handle Series element-wise operations."""
            return self  # No-op for apply

    class api:
        """Mock pandas.api for checking data types."""
        class types:
            @staticmethod
            def is_object_dtype(column):
                """Check if a column is an object type (always returns False)."""
                return False  # Simplified mock behavior

            @staticmethod
            def is_datetime64_any_dtype(column):
                """Check if a column is a datetime type (always returns False)."""
                return False  # Simplified mock behavior

            @staticmethod
            def is_timedelta64_dtype(column):
                """Check if a column is a timedelta type (always returns False)."""
                return False  # Simplified mock behavior

    @staticmethod
    def isna(value):
        """Mock pandas.isna function to check for None or NaN."""
        return value is None or (isinstance(value, float) and value != value)  # Handles NaN

    @staticmethod
    def notnull(value):
        """Mock pandas.notnull function to check for not-None and not-NaN values."""
        return not MockPandas.isna(value)

    def __init__(self):
        """Mock pandas.options."""
        self.options = {}

