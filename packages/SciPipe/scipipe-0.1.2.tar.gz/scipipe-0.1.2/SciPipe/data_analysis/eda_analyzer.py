import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class EDAAnalyzer:
    """
    A class used to perform exploratory data analysis (EDA) on a given DataFrame.

    Attributes:
    df (pd.DataFrame): The input DataFrame to analyze.
    target_column (str): The target variable column to focus on during analysis.
    unique_values (int): The number of unique values in the target variable.
    """

    def __init__(self, df, target_column):
        """
        Initializes the EDAAnalyzer with the DataFrame and target column.

        Parameters:
        df (pd.DataFrame): The input DataFrame.
        target_column (str): The target variable to analyze.
        """
        self.df = df
        self.target_column = target_column
        self.unique_values = df[target_column].nunique()

    def summary_statistics(self):
        """
        Generates summary statistics for numeric columns in the DataFrame.

        Returns:
        pd.DataFrame: Summary statistics for numeric columns.
        """
        return self.df.describe().T  # Transpose for better readability

    def missing_value_proportion(self):
        """
        Analyzes the proportion of missing values in each column of the DataFrame.

        Returns:
        pd.DataFrame: A DataFrame showing the proportion of missing values for
                      each column.
        """
        missing_values = self.df.isnull().sum() / len(self.df)
        missing_values_df = (
            pd.DataFrame(
                {
                    "column": missing_values.index,
                    "missing_proportion": missing_values.values,
                }
            )
            .sort_values(by="missing_proportion", ascending=False)
            .reset_index(drop=True)
        )
        return missing_values_df

    def plot_missing_data_heatmap(self):
        """
        Plots a heatmap showing missing data in the DataFrame.

        Returns:
        None: Displays a heatmap with missing data locations.
        """
        plt.figure(figsize=(12, 6))
        sns.heatmap(self.df.isnull(), cbar=False, cmap="viridis")
        plt.title("Missing Data Heatmap")
        plt.show()

    def plot_correlation_matrix(self, method="pearson"):
        """
        Plots a correlation matrix for numeric features in the DataFrame.

        Parameters:
        method (str): Method of correlation ('pearson', 'kendall', 'spearman').

        Returns:
        None: Displays a heatmap of the correlation matrix.
        """
        correlation = self.df.corr(numeric_only=True, method=method)
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
        plt.title("Correlation Matrix")
        plt.show()

    def detect_outliers(self, column):
        """
        Detects outliers in a specific numeric column using the IQR method.

        The IQR (Interquartile Range) method is a statistical technique used to detect
        outliers in a dataset. IQR=Q3-Q1
        Lower Bound: Any data point below this threshold is considered an outlier:
        Lower Bound=Q1-1.5xIQR
        Upper Bound: Any data point above this threshold is also considered an outlier:
        Upper Bound=Q3+1.5xIQR

        Parameters:
        column (str): The name of the column to analyze for outliers.

        Returns:
        pd.DataFrame: A DataFrame with rows that contain outliers.
        """
        quantile_1 = self.df[column].quantile(0.25)
        quantile_3 = self.df[column].quantile(0.75)
        iqr = quantile_3 - quantile_1

        outliers = self.df[
            (self.df[column] < (quantile_1 - 1.5 * iqr))
            | (self.df[column] > (quantile_3 + 1.5 * iqr))
        ]
        return outliers

    def plot_feature_distribution(self, column, bins=30):
        """
        Plots the distribution of a specific feature, with different methods for numeric
        and categorical columns.

        Parameters:
        column (str): The name of the column for which to plot the distribution.
        bins (int): Number of bins for the histogram (numeric features only).

        Returns:
        None: Displays a plot based on the feature type (numeric or categorical).
        """
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found in the DataFrame")

        # Determine if the column is numeric or categorical
        if pd.api.types.is_numeric_dtype(self.df[column]):
            self._plot_numeric_distribution(column, bins)
        else:
            self._plot_categorical_distribution(column)

    def _plot_numeric_distribution(self, column, bins):
        """Private method to plot the distribution of a numeric column."""
        plt.figure(figsize=(8, 6))
        sns.histplot(self.df[column], bins=bins, kde=False)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

    def _plot_categorical_distribution(self, column):
        """Private method to plot the distribution of a categorical column."""
        plt.figure(figsize=(8, 6))
        sns.countplot(x=self.df[column], order=self.df[column].value_counts().index)
        plt.title(f"Category Counts of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha="right")  # Rotate labels
        plt.show()

    def plot_boxplot(self, column, by=None):
        """
        Plots a boxplot of a numeric column,
        optionally grouped by a categorical feature.

        Parameters:
        column (str): Numeric column to plot.
        by (str or None): Categorical column to group by.
        If None, no grouping is applied.

        Returns:
        None: Displays a box plot.
        """
        plt.figure(figsize=(8, 6))

        if by:
            sns.boxplot(x=self.df[by], y=self.df[column])
            plt.title(f"Boxplot of {column} by {by}")
            plt.xlabel(by)
            plt.ylabel(column)
        else:
            sns.boxplot(x=self.df[column])
            plt.title(f"Boxplot of {column}")

        plt.show()

    def plot_pairplot(self, hue=None):
        """
        Plots a pair plot for numeric features in the DataFrame.

        Parameters:
        hue (str): Optional. Column to use for color encoding (typically a categorical
                   variable).

        Returns:
        None: Displays a pair plot.
        """
        sns.pairplot(self.df, hue=hue)
        plt.title("Pair Plot")
        plt.show()

    def plot_target_distribution(self, bins=30, kde=True):
        """
        Plots the distribution of the target variable, automatically determining whether
        it's numeric, binary, or categorical. Customization options are available for
        bins and KDE.

        Parameters:
        bins (int): Number of bins to use for the histogram (numeric targets only).
                    Default is 30.
        kde (bool): Whether to add KDE to the numeric target distribution plot.
                    Default is True.

        Returns:
        None: Displays a plot of the target distribution.
        """
        # Handle Binary Target (even if it's numeric)
        if self.unique_values == 2:
            print(f"Detected binary target: {self.target_column}")
            plt.figure(figsize=(8, 6))
            sns.countplot(
                x=self.df[self.target_column],
                order=self.df[self.target_column].value_counts().index,
            )

            # Add percentage annotations
            total = len(self.df[self.target_column])
            for p in plt.gca().patches:
                percentage = f"{100 * p.get_height() / total:.1f}%"
                plt.gca().annotate(
                    percentage,
                    (p.get_x() + p.get_width() / 2.0, p.get_height()),
                    ha="center",
                    va="baseline",
                )

            plt.title(f"Distribution of Binary Target: {self.target_column}")
            plt.xlabel(self.target_column)
            plt.ylabel("Count")
            plt.show()

        # Numeric Target
        elif (
            pd.api.types.is_numeric_dtype(self.df[self.target_column])
            and self.unique_values > 2
        ):
            print(f"Detected numeric target: {self.target_column}")
            plt.figure(figsize=(8, 6))
            sns.histplot(self.df[self.target_column], bins=bins, kde=kde)
            plt.title(f"Distribution of Numeric Target: {self.target_column}")
            plt.xlabel(self.target_column)
            plt.ylabel("Frequency")
            plt.show()

        # Categorical Target
        else:
            print(f"Detected categorical target: {self.target_column}")
            plt.figure(figsize=(8, 6))
            sns.countplot(
                x=self.df[self.target_column],
                order=self.df[self.target_column].value_counts().index,
            )

            # Add percentage annotations
            total = len(self.df[self.target_column])
            for p in plt.gca().patches:
                percentage = f"{100 * p.get_height() / total:.1f}%"
                plt.gca().annotate(
                    percentage,
                    (p.get_x() + p.get_width() / 2.0, p.get_height()),
                    ha="center",
                    va="baseline",
                )

            plt.title(f"Distribution of Categorical Target: {self.target_column}")
            plt.xlabel(self.target_column)
            plt.ylabel("Count")
            plt.xticks(rotation=45, ha="right")  # Rotate labels for readability
            plt.show()

    def value_counts(self, column, round_by=2):
        """
        Returns a DataFrame with the value counts and percentage distribution of a
        categorical column.

        Parameters:
        column (str): The name of the categorical column to analyze.
        round_by (int): Number of decimal places to round the percentage values.
                        Default is 2.

        Returns:
        pd.DataFrame: A DataFrame with two columns:
                      - column_name_num: Absolute count of each category.
                      - column_name_pct: Percentage distribution of each category,
                        rounded to the specified number of decimal places.
        """
        column_dist_num = pd.DataFrame(self.df[column].value_counts(normalize=False))
        column_dist_pct = pd.DataFrame(
            self.df[column].value_counts(normalize=True).round(round_by)
        )
        column_dist_df = column_dist_num.merge(
            column_dist_pct,
            left_index=True,
            right_index=True,
            suffixes=["_num", "_pct"],
        ).reset_index()
        return column_dist_df

    def calculate_duplicates(self, subset=None):
        """
        Calculates the number of duplicate rows in the DataFrame, optionally based on
        specific columns, and returns the result as a DataFrame.

        Parameters:
        subset (list or None): Columns to check for duplicates.
            If None, checks all columns. Default is None.

        Returns:
        pd.DataFrame: A DataFrame containing:
            - 'Metric': The metric names
                (Total Rows, Duplicate Rows, Duplicate Percentage).
            - 'Value': The calculated values for each metric.
        """
        # Identify duplicate rows
        duplicate_rows = self.df.duplicated(subset=subset).sum()
        total_rows = len(self.df)
        duplicate_percentage = (duplicate_rows / total_rows) * 100

        # Create a DataFrame with the results
        result_df = pd.DataFrame(
            {
                "Metric": ["Total Rows", "Duplicate Rows", "Duplicate Percentage"],
                "Value": [total_rows, duplicate_rows, round(duplicate_percentage, 2)],
            }
        )

        return result_df

    def feature_correlation_with_target(self, method="pearson"):
        """
        Calculates the correlation of each numeric feature with the target variable.

        Parameters:
        method (str): Method of correlation ('pearson', 'kendall', 'spearman').

        Returns:
        pd.DataFrame: A DataFrame with features and their correlation values with the
            target.
        """
        if pd.api.types.is_numeric_dtype(self.df[self.target_column]):
            correlations = self.df.corr(numeric_only=True, method=method)[
                self.target_column
            ].drop(self.target_column)
            result_df = pd.DataFrame(correlations).reset_index()
            result_df.columns = ["Feature", "Correlation"]
            result_df = result_df.sort_values(by="Correlation", ascending=False)
        else:
            print("The target column is not numeric. Correlation calculation skipped.")
            result_df = pd.DataFrame()

        return result_df

    def categorical_feature_summary(self):
        """
        Summarizes categorical features and suggests encoding if needed.

        Returns:
        pd.DataFrame: A DataFrame with categorical columns and their unique value
            counts.
        """
        categorical_columns = self.df.select_dtypes(
            include=["object", "category"]
        ).columns
        result = pd.DataFrame(
            {
                "Feature": categorical_columns,
                "Unique Values": [
                    self.df[col].nunique() for col in categorical_columns
                ],
                "Need Encoding": [
                    "Yes" if self.df[col].nunique() > 1 else "No"
                    for col in categorical_columns
                ],
            }
        )

        return result.sort_values(by="Need Encoding", ascending=False)

    def compare_missing_vs_non_missing_target(self, feature):
        """
        Compares the distribution or average of the target variable for rows with and
        without missing values in a specific feature.

        Parameters:
        feature (str): The feature column to analyze for missing values.

        Returns:
        pd.DataFrame: A DataFrame showing the mean of the target variable for rows with
                    and without missing values in the specified feature.
        """
        # Split data into rows with and without missing values in the specified feature
        missing_mask = self.df[feature].isnull()

        # Calculate the average or distribution of the target variable
        target_with_missing = self.df[missing_mask][self.target_column]
        target_without_missing = self.df[~missing_mask][self.target_column]

        # Create a DataFrame to compare mean values
        mean_comparison = pd.DataFrame(
            {
                "Category": ["With Missing", "Without Missing"],
                "Mean Target": [
                    target_with_missing.mean(),
                    target_without_missing.mean(),
                ],
                "Median Target": [
                    target_with_missing.median(),
                    target_without_missing.median(),
                ],
                "Count": [len(target_with_missing), len(target_without_missing)],
            }
        )

        return mean_comparison

    def analyze_all_features(self, columns_to_skip: list = None):
        """
        Automatically analyzes all features in the DataFrame by applying appropriate
        methods for numeric and categorical columns.

        Parameters:
        columns_to_skip (list, optional): List of columns to exclude from analysis.
            Defaults to None.

        Returns:
        None: Displays the analysis results for each feature.
        """
        if columns_to_skip is None:
            columns_to_skip = []

        if self.df.empty:
            print("The DataFrame is empty. No features to analyze.")
            return

        column_list = [col for col in self.df.columns if col not in columns_to_skip]

        for column in column_list:
            print("\n" + "=" * 80)
            print(f"Analyzing Feature: {column}")
            print("=" * 80)

            if pd.api.types.is_numeric_dtype(self.df[column]):
                print(f"Summary Statistics for Numeric Feature: {column}")
                print(self.df[column].describe())

                print(f"\nDetecting Outliers in {column}...")
                outliers = self.detect_outliers(column)
                print(f"Found {len(outliers)} outliers in {column}.")

            else:
                print(f"Value Counts for Categorical Feature: {column}")
                print(self.df[column].value_counts())

            if (self.df[column].isnull().sum() > 0) & (
                pd.api.types.is_numeric_dtype(self.df[self.target_column])
            ):
                print(f"\nMissing values effect on the target variable for {column}...")
                print(self.compare_missing_vs_non_missing_target(column))

            print(f"\nPlotting Distribution for {column}...")
            self.plot_feature_distribution(column)

        print("\nAnalysis completed for all features.")

    def run_global_eda(self):
        """
        Runs broader exploratory data analysis steps such as correlation matrix, missing
        data heatmap, pair plot, and target distribution analysis.

        Returns:
        None: Displays the results of the global EDA analysis.
        """
        print("\nAnalyzing Info...")
        print(self.df.info())

        print("\nAnalyzing Summary Statistics...")
        print(self.summary_statistics())

        print("\nAnalyzing Duplications...")
        print(self.calculate_duplicates())

        print("\nRunning Missing Data Proportion...")
        print(self.missing_value_proportion())

        print("\nRunning Missing Data Heatmap...")
        self.plot_missing_data_heatmap()

        print("\nAnalyzing Target Distribution...")
        self.plot_target_distribution()

        print("\nAnalyzing Correlation With The Target Variable...")
        print(self.feature_correlation_with_target())

        print("\nRunning Correlation Matrix Analysis...")
        self.plot_correlation_matrix()

        print("\nGenerating Pair Plot for Numeric Features...")
        if self.unique_values == 2:
            self.plot_pairplot(hue=self.target_column)

        # Numeric Target
        elif (
            pd.api.types.is_numeric_dtype(self.df[self.target_column])
            and self.unique_values > 2
        ):
            self.plot_pairplot()

        # Categorical Target
        else:
            self.plot_pairplot(hue=self.target_column)

        print("\nAnalyzing Categorical Features Summary...")
        print(self.categorical_feature_summary())
