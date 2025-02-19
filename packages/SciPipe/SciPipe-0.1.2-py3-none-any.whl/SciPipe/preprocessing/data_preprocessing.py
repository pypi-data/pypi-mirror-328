import pandas as pd
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def _rmv_char(df, columns=True):
    """Remove disallowed characters from column names or values in a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame on which to perform character removal.
        columns (bool): Whether to remove characters from columns (True) or from values
            (False). Defaults to True.
    """
    if columns:
        df.columns = df.columns.str.replace(r"[/,;\] -]", "_", regex=True)

    else:
        for col in df.select_dtypes(include=["object"]):
            df[col] = df[col].str.replace(r"[/,;\] -]", "_", regex=True)


class DataPreprocessor:
    """
    A class used to perform preprocessing tasks on a dataset before feeding it into a
    machine learning pipeline.

    This class provides methods for setting up, configuring, and applying a flexible
    preprocessing pipeline using `columns_dict` to define column attributes and
    `pipeline_steps_config` to define transformation steps.

    Attributes:
        columns_dict (dict): A dictionary defining the attributes for each column in
            the dataset.
        remove_chars (bool): A flag to specify whether to remove disallowed characters
            in column names and values.
        pipeline_steps_config (list): A list of dictionaries, each defining a pipeline
            step (name, action).
        pipeline (Pipeline): The constructed sklearn Pipeline based on the user-defined
            steps.
    """

    def __init__(
        self, columns_dict: dict, remove_chars=True, pipeline_steps_config=None
    ):
        """
        Initializes the DataPreprocessor with configuration settings and optional
        preprocessing steps.

        Args:
            columns_dict (dict): A dictionary containing processing information for
                each column.
            remove_chars (bool): If True, disallowed characters in column names and
                values will be removed.
            pipeline_steps_config (list of dict): Optional. Configuration for pipeline
                steps, each step should contain `name` and `action`.
        """
        self.columns_dict = columns_dict
        self.remove_chars = remove_chars
        self.pipeline_steps_config = pipeline_steps_config or []
        self.pipeline = None

    def fit(self, X_train_raw: pd.DataFrame):
        """
        Prepares the data, creates the pipeline, and fits it to the training data.

        Args:
            X_train_raw (pd.DataFrame): Raw training dataset to fit the pipeline on.

        Returns:
            Pipeline: The fitted sklearn pipeline, allowing the user to save it if
            needed.
        """
        # Prepare the data (set data types, handle missing values)
        X_train_raw = self._prepare_data(X_train_raw)

        # Optionally remove disallowed characters from column names
        if self.remove_chars:
            _rmv_char(X_train_raw)

        # Create and fit the pipeline
        self._create_pipeline()
        self.pipeline.fit(X_train_raw.sort_index(axis=1))

        return self.pipeline

    def transform(self, df_dict: dict):
        """
        Applies the trained pipeline transformations to each dataset in the provided
        dictionary.

        Args:
            df_dict (dict): A dictionary of DataFrames where each key is a dataset name
                (e.g., "X_train") and each value is a DataFrame to transform.

        Returns:
            dict: A dictionary of transformed DataFrames with the same keys as the
                input.
        """
        datasets = {}
        for name, df in df_dict.items():
            transformed_df = self.pipeline.transform(df)
            if self.remove_chars:
                _rmv_char(transformed_df)
            datasets[name] = transformed_df

        return datasets

    def save_pipeline(self, filepath, compress=3):
        """
        Saves the pipeline to a specified filepath as a .joblib file.

        Args:
            filepath (str): The file path where the pipeline should be saved.
            compress (int or bool): Compression level for the saved file. Default is 3.

        Raises:
            ValueError: If the pipeline is not initialized before saving.
        """
        if self.pipeline is None:
            raise ValueError("Pipeline is not initialized. Fit the data before saving.")

        dump(self.pipeline, filepath, compress=compress)
        print(f"Pipeline saved to {filepath}")

    def _prepare_data(self, df: pd.DataFrame):
        """
        Prepares the DataFrame by setting data types and performing basic preprocessing
        operations like converting data types and dropping duplicates.

        Args:
            df (pd.DataFrame): The DataFrame to prepare.

        Returns:
            pd.DataFrame: The prepared DataFrame.
        """
        # Convert boolean columns to boolean type
        boolean_cols = self._get_columns_by_criteria("class", "boolean")
        if boolean_cols:
            df[boolean_cols] = df[boolean_cols].astype("boolean")

        # Convert categorical columns to category type
        categorical_cols = self._get_columns_by_criteria("class", "categorical")
        if categorical_cols:
            df[categorical_cols] = df[categorical_cols].astype("category")

        # Convert numeric columns to float type
        categorical_cols = self._get_columns_by_criteria("class", "numeric")
        if categorical_cols:
            df[categorical_cols] = df[categorical_cols].astype("float")

        # Convert date columns to datetime type
        date_cols = self._get_columns_by_criteria("class", "date")
        if date_cols:
            df[date_cols] = df[date_cols].apply(pd.to_datetime, errors="coerce")

        # Convert ID columns to string type
        id_cols = self._get_columns_by_criteria("class", "id")
        if id_cols:
            df[id_cols] = df[id_cols].astype("str")

        # Drop duplicates if necessary
        df.drop_duplicates(inplace=True)

        return df

    def _create_pipeline(self):
        """
        Constructs and configures a sklearn Pipeline based on `pipeline_steps_config`
        and uses `columns_dict` to automatically determine columns for imputers and
        encoders.

        Each step in `pipeline_steps_config` is applied to the columns specified by
        `imputer` or `encoder` in `columns_dict`, making the configuration flexible and
        dynamic.
        """
        pipeline_steps = []

        # Identify columns for each type of transformation based on `columns_dict`
        imputer_columns = self._get_columns_by_criteria("imputer", return_dict=True)
        encoder_columns = self._get_columns_by_criteria("encoder", return_dict=True)

        # Iterate through pipeline_steps_config to create pipeline steps
        for step_config in self.pipeline_steps_config:
            step_name = step_config["name"]
            step_action = step_config["action"]
            step_params = step_config.get("params", {}).copy()  # Copy to modify safely

            # Check if the step is an imputer and apply only if columns exist
            if step_name in imputer_columns:
                step_params["variables"] = imputer_columns[step_name]
                if step_params["variables"]:  # Only add step if there are columns
                    pipeline_steps.append((step_name, step_action(**step_params)))

            # Check if the step is an encoder and apply only if columns exist
            elif step_name in encoder_columns:
                step_params["variables"] = encoder_columns[step_name]
                if step_params["variables"]:  # Only add step if there are columns
                    pipeline_steps.append((step_name, step_action(**step_params)))

        # Create the sklearn pipeline with the configured steps
        self.pipeline = Pipeline(pipeline_steps)

    def _get_columns_by_criteria(self, key, value=None, return_dict=False):
        """
        Retrieves columns based on the specified key and value within `columns_dict`.

        Args:
            key (str): The key to look up in `columns_dict`
                (e.g., 'class', 'imputer', 'encoder').
            value (str, optional): Specific value to filter by
                (e.g., 'boolean' for class).
                If None, retrieves all values for the key.
            return_dict (bool): If True, returns a dictionary where each key is a
                unique attribute (e.g., each type of imputer) and each value is a list
                of columns. If False, returns a list of columns matching the `value`.

        Returns:
            dict or list: A dictionary of lists (if `return_dict=True`),
            or a list of columns.
        """
        if return_dict:
            result = {}
            for col, props in self.columns_dict.items():
                action_type = props.get(key)
                if action_type:
                    if action_type not in result:
                        result[action_type] = []
                    result[action_type].append(col)
            return result
        else:
            return [
                col
                for col, props in self.columns_dict.items()
                if props.get(key) == value
            ]


class PipelineLoader:
    """
    A class responsible for loading and applying a pre-trained pipeline to new data.
    """

    # pylint: disable=too-few-public-methods
    def __init__(self, pipeline_filepath):
        """
        Initializes the PipelineLoader and loads the pipeline.

        Args:
            pipeline_filepath (str): Path to the saved pipeline file.
        """
        self.pipeline = load(pipeline_filepath)

    def transform(self, data):
        """
        Applies the loaded pipeline to new data.

        Args:
            data (pd.DataFrame): Real-time or new data to preprocess.

        Returns:
            pd.DataFrame: The transformed data.
        """
        return self.pipeline.transform(data)


class DataSplitter:
    """
    Class to split a DataFrame into training, validation (optional), and test sets,
    with support for splitting based on an ID column, randomly, or by date.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        target_column: str,
        split_config: dict,
        random_state: int = 42,
    ) -> None:
        """
        Initialize the DataSplitter with the DataFrame, target column, and desired
        splitting proportions.

        Args:
            df (pd.DataFrame): The DataFrame to split.
            target_column (str): The name of the target column.
            split_config (dict): Configuration dictionary containing:
                - train_size (float): Proportion of the data to allocate to the
                    training set.
                - test_size (float): Proportion of the data to allocate to the test set.
                - valid_size (float or None): Proportion of the data to allocate to the
                  validation set. If None, no validation set is created.
            random_state (int): Random seed for reproducibility. Default is 42.

        Raises:
            ValueError: If the sum of train_size, valid_size, and test_size does not
                equal 1, or if the sum of train_size and test_size does not equal 1
                when no validation set is used.
        """
        self.df = df
        self.target_column = target_column
        self.train_size = split_config["train_size"]
        self.test_size = split_config["test_size"]
        self.valid_size = split_config.get("valid_size", None)
        self.random_state = random_state

        # Validate the split sizes
        if self.valid_size is not None:
            total = self.train_size + self.valid_size + self.test_size
            if not abs(total - 1.0) < 1e-6:
                raise ValueError(
                    "The sum of train_size, valid_size, and test_size must equal 1."
                )
        else:
            total = self.train_size + self.test_size
            if not abs(total - 1.0) < 1e-6:
                raise ValueError(
                    "The sum of train_size and test_size must equal 1 when no "
                    "validation set is used."
                )

    def split_on_id(self, id_column_name: str):
        """
        Split the DataFrame into training, validation (optional), and test sets
        based on an ID column.

        Args:
            id_column_name (str): The name of the column to use as the identifier
                for splitting.

        Returns:
            tuple: If `valid_size` is provided, returns six elements
                   (X_train, y_train, X_valid, y_valid, X_test, y_test).
                   Otherwise, returns four elements (X_train, y_train, X_test, y_test).
        """
        # Get the unique IDs from the ID column
        unique_ids = self.df[id_column_name].unique()

        # Split into train and temp (validation + test)
        non_train_size = 1 - self.train_size
        train_ids, temp_ids = train_test_split(
            arrays=unique_ids, test_size=non_train_size, random_state=self.random_state
        )

        if self.valid_size is not None:
            # Calculate the validation ratio as a proportion of temp (validation + test)
            valid_ratio = self.valid_size / (self.valid_size + self.test_size)

            # Split temp into validation and test sets
            valid_ids, test_ids = train_test_split(
                arrays=temp_ids,
                test_size=1 - valid_ratio,
                random_state=self.random_state,
            )

            # Split the DataFrame into training, validation, and test sets
            X_train = self.df[self.df[id_column_name].isin(train_ids)].drop(
                columns=[self.target_column]
            )
            y_train = self.df[self.df[id_column_name].isin(train_ids)][
                self.target_column
            ]
            X_valid = self.df[self.df[id_column_name].isin(valid_ids)].drop(
                columns=[self.target_column]
            )
            y_valid = self.df[self.df[id_column_name].isin(valid_ids)][
                self.target_column
            ]
            X_test = self.df[self.df[id_column_name].isin(test_ids)].drop(
                columns=[self.target_column]
            )
            y_test = self.df[self.df[id_column_name].isin(test_ids)][self.target_column]

            return X_train, y_train, X_valid, y_valid, X_test, y_test

        else:
            # Split the DataFrame into train and test sets (no validation set)
            X_train = self.df[self.df[id_column_name].isin(train_ids)].drop(
                columns=[self.target_column]
            )
            y_train = self.df[self.df[id_column_name].isin(train_ids)][
                self.target_column
            ]
            X_test = self.df[self.df[id_column_name].isin(temp_ids)].drop(
                columns=[self.target_column]
            )
            y_test = self.df[self.df[id_column_name].isin(temp_ids)][self.target_column]

            return X_train, y_train, X_test, y_test

    def random_split(self):
        """
        Split the DataFrame into training, validation (optional),
        and test sets randomly.

        Returns:
            tuple: If `valid_size` is provided, returns six elements
                   (X_train, y_train, X_valid, y_valid, X_test, y_test).
                   Otherwise, returns four elements (X_train, y_train, X_test, y_test).
        """
        # Extract feature columns and target column
        X = self.df.drop(columns=[self.target_column])
        y = self.df[self.target_column]

        # Split into train and temp (validation + test)
        non_train_size = 1 - self.train_size
        X_train, X_temp, y_train, y_temp = train_test_split(
            X, y, test_size=non_train_size, random_state=self.random_state
        )

        if self.valid_size is not None:
            # Calculate the validation ratio as a proportion of temp (validation + test)
            valid_ratio = self.valid_size / (self.valid_size + self.test_size)

            # Split temp into validation and test sets
            X_valid, X_test, y_valid, y_test = train_test_split(
                X_temp,
                y_temp,
                test_size=1 - valid_ratio,
                random_state=self.random_state,
            )

            return X_train, y_train, X_valid, y_valid, X_test, y_test

        else:
            # Split temp into train and test sets (no validation set)
            X_test = X_temp
            y_test = y_temp

            return X_train, y_train, X_test, y_test

    def split_by_date(self, date_column: str):
        """
        Split the DataFrame into training, validation (optional),
        and test sets based on a date column.

        Args:
            date_column (str): The name of the column to use as the date for splitting.
                Must be datetime type.

        Returns:
            tuple: If `valid_size` is provided, returns six elements
                   (X_train, y_train, X_valid, y_valid, X_test, y_test).
                   Otherwise, returns four elements (X_train, y_train, X_test, y_test).

        Raises:
            ValueError: If the date_column is not in datetime format.
        """
        # Ensure the date column is in datetime format
        if not pd.api.types.is_datetime64_any_dtype(self.df[date_column]):
            raise ValueError(f"The column '{date_column}' must be of datetime type.")

        # Sort the DataFrame by the date column
        df_sorted = self.df.sort_values(by=date_column)

        # Calculate the number of samples
        total_samples = len(df_sorted)
        train_end = int(self.train_size * total_samples)

        # Split when there's a validation set
        if self.valid_size is not None:
            valid_end = train_end + int(self.valid_size * total_samples)

            # Split into train, validation, and test sets
            X_train = df_sorted.iloc[:train_end].drop(
                columns=[self.target_column, date_column]
            )
            y_train = df_sorted.iloc[:train_end][self.target_column]

            X_valid = df_sorted.iloc[train_end:valid_end].drop(
                columns=[self.target_column, date_column]
            )
            y_valid = df_sorted.iloc[train_end:valid_end][self.target_column]

            X_test = df_sorted.iloc[valid_end:].drop(
                columns=[self.target_column, date_column]
            )
            y_test = df_sorted.iloc[valid_end:][self.target_column]

            return X_train, y_train, X_valid, y_valid, X_test, y_test

        # Split without validation set (just train and test)
        else:
            X_train = df_sorted.iloc[:train_end].drop(
                columns=[self.target_column, date_column]
            )
            y_train = df_sorted.iloc[:train_end][self.target_column]

            X_test = df_sorted.iloc[train_end:].drop(
                columns=[self.target_column, date_column]
            )
            y_test = df_sorted.iloc[train_end:][self.target_column]

            return X_train, y_train, X_test, y_test
