import datetime

import numpy as np
import pandas as pd
from feature_engine.imputation import ArbitraryNumberImputer
from sklearn.base import BaseEstimator, TransformerMixin


class TemporalVariableTransformerDays(BaseEstimator, TransformerMixin):
    """
    Transforms temporal variables into the number of days elapsed from a reference date.
    """

    def __init__(self, variables, reference_variable, variables_first=False):
        """
        Initialize TemporalVariableTransformerDays.

        Args:
        variables (list): List of temporal variable names.
        reference_variable (str or datetime): Reference variable name or a specific
            reference datetime. If 'today' is provided, uses the current UTC date and
            time.
        variables_first (bool): Flag indicating whether the temporal variable comes
            first in subtraction. default=False

        Raises:
        ValueError: If variables is not a list.
        """
        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables
        self.variables_first = variables_first

        self.new_col_list = [f"{s}_days" for s in variables]

        if reference_variable == "today":
            self.reference_variable = datetime.datetime.now(datetime.timezone.utc)
            self.is_today = True
        else:
            self.is_today = False
            self.reference_variable = reference_variable

    def fit(self, X: pd.DataFrame, y=None):  # pylint: disable=unused-argument
        """
        Fit method for sklearn pipeline compatibility.

        Args:
        X (pd.DataFrame): Feature DataFrame.

        Returns:
        self (object): Returns self.
        """
        return self

    def transform(self, X: pd.DataFrame):
        """
        Transform method for converting temporal variables into elapsed days.

        Args:
        X (pd.DataFrame): Feature DataFrame.

        Returns:
        X (pd.DataFrame): Transformed feature DataFrame.
        """
        # so that we do not over-write the original dataframe
        X = X.copy()

        for i in self.variables:
            X[i] = X[i].dt.date

        X[self.reference_variable] = X[self.reference_variable].dt.date

        for feature, new_col in zip(self.variables, self.new_col_list):
            if self.is_today:
                if self.variables_first:
                    X[new_col] = (X[feature] - self.reference_variable).dt.days
                else:
                    X[new_col] = (self.reference_variable - X[feature]).dt.days
            else:
                if self.variables_first:
                    X[new_col] = (X[feature] - X[self.reference_variable]).dt.days
                else:
                    X[new_col] = (X[self.reference_variable] - X[feature]).dt.days

        return X


class BooleanToBinary(BaseEstimator, TransformerMixin):
    """Convert boolean variables to binary."""

    def __init__(self, variables: list):
        """
        Initialize BooleanToBinary.

        Args:
        variables (list): List of boolean variable names.

        Raises:
        ValueError: If variables is not a list.
        """
        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables

    def fit(self, X: pd.DataFrame, y=None):  # pylint: disable=unused-argument
        """
        Fit method for sklearn pipeline compatibility.

        Args:
        X (pd.DataFrame): Feature DataFrame.

        Returns:
        self (object): Returns self.
        """
        return self

    def transform(self, X: pd.DataFrame):
        """
        Transform method for converting boolean variables to binary.

        Args:
        X (pd.DataFrame): Feature DataFrame.

        Returns:
        X (pd.DataFrame): Transformed feature DataFrame.
        """
        # so that we do not over-write the original dataframe
        X = X.copy()

        for feature in self.variables:
            if X[feature].dtype == "bool":
                X[feature] = np.where(X[feature] is True, 1, 0)
            else:
                X[feature] = np.where(X[feature].astype(str).str.lower == "true", 1, 0)

        return X


class ReplaceNegativeWithZeroTransformer(BaseEstimator, TransformerMixin):
    """Replace negative values in specified variables with zero."""

    def __init__(self, variables: list):
        """
        Initialize ReplaceNegativeWithZeroTransformer.

        Args:
        variables (list): List of variable names to replace negative values with zero.

        Raises:
        ValueError: If variables is not a list.
        """
        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables

    def fit(self, X: pd.DataFrame, y=None):  # pylint: disable=unused-argument
        """
        Fit method for sklearn pipeline compatibility.

        Args:
        X (pd.DataFrame): Feature DataFrame.

        Returns:
        self (object): Returns self.
        """
        return self

    def transform(self, X: pd.DataFrame):
        """
        Transform method for replacing negative values with zero.

        Parameters:
        X (pd.DataFrame)): Feature DataFrame.

        Returns:
        X (pd.DataFrame)): Transformed feature DataFrame.
        """
        # so that we do not over-write the original dataframe
        X = X.copy()

        for feature in self.variables:
            X[feature] = np.where(X[feature] < 0, 0, X[feature])

        return X


class MaxValueImputer(ArbitraryNumberImputer):
    """Impute missing values with the maximum value from specified columns."""

    def __init__(self, variables=None):
        """
        Initialize MaxValueImputer.

        Args:
        variables (list or None): List of variable names to impute with their maximum
            values. If None, imputes all numeric variables. default=None

        Raises:
        ValueError
            If variables is not a list.
        """
        super().__init__(variables=variables)
        self.max_value = None  # Initialize max_value attribute

    def fit(self, X: pd.DataFrame, y=None):
        """
        Fit method for computing the maximum value for imputation.

        Args:
        X (pd.DataFrame): Feature DataFrame.

        Returns:
        self (object): Returns self.
        """
        # Compute the max value for each specified column
        if self.variables:
            self.max_value = X[self.variables].max().to_dict()
        else:
            self.max_value = X.max().to_dict()

        # Call the fit method of the super class
        return super().fit(X, y)

    def transform(self, X: pd.DataFrame):
        """
        Transform method for imputing missing values with maximum values.

        Args:
        X (pd.DataFrame): Feature DataFrame.

        Returns:
        X (pd.DataFrame): Transformed feature DataFrame.
        """
        # Replace missing values with the max value
        if self.variables:
            for var in self.variables:
                X[var].fillna(self.max_value[var], inplace=True)
        else:
            for var in X.columns:
                X[var].fillna(self.max_value[var], inplace=True)

        return X
