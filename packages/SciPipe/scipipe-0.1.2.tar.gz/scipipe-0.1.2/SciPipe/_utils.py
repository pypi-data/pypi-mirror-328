import functools
import json
import os
import threading
import time
import tracemalloc
from datetime import datetime
from io import BytesIO
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_gbq
import psutil
import seaborn as sns
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer
from sklearn.model_selection import train_test_split


class ConfigLoader:
    """
    A class for loading and accessing configurations from a JSON file.

    This class encapsulates the functionality to load a configuration file once
    and provide an interface to access the configuration data throughout the
    application. It supports fetching values with defaults if the key is not found.

    Attributes:
        config_name (str): The path to the configuration file to be loaded.
        config (dict): The dictionary containing the loaded configuration.

    Methods:
        load_config: Loads the configuration file into a dictionary.
        get: Retrieves a value from the configuration with an optional default.
    """

    def __init__(self, config_name: str):
        """
        Initializes the ConfigLoader with the specified configuration file.

        Parameters:
            config_name (str): The path to the configuration file to be loaded.

        Raises:
            FileNotFoundError: If the specified configuration file does not exist.
            json.JSONDecodeError: If the configuration file is not valid JSON.
        """
        self.config_name = config_name
        self.config = self._load_config()

    def _load_config(self):
        """
        Loads the JSON configuration file into a dictionary.

        This method opens the configuration file in read mode, parses the JSON,
        and stores it in a dictionary. This dictionary is then accessible to
        other methods of the class.

        Returns:
            dict: The dictionary containing the loaded configuration.

        Raises:
            FileNotFoundError: If the specified configuration file does not exist.
            json.JSONDecodeError: If the configuration file is not valid JSON.
        """
        with open(self.config_name, "r") as con:
            json_dict = json.load(con)
        return json_dict

    def get(self, key, default=None):
        """
        Retrieves a value from the configuration dictionary given a key.

        If the key does not exist in the configuration, this method returns
        the specified default value.

        Parameters:
            key (str): The key for the configuration value to retrieve.
            default (any, optional): The default value to return if
                the key is not found. Defaults to None.

        Returns:
            The value from the configuration if the key exists,
            otherwise the specified default value.
        """
        return self.config.get(key, default)


def update_wrapper(wrapper, wrapped):
    """Update a wrapper function to look more like the wrapped function.

    Args:
        wrapper: The function that is wrapping another function.
        wrapped: The function that is being wrapped.

    Returns:
        The wrapper function with updated attributes.
    """
    functools.update_wrapper(wrapper, wrapped)
    return wrapper


class MemoryUsageDecorator:
    """A decorator class for measuring and recording the memory usage of a function."""

    memory_data = []
    execution_order = 0

    def __init__(self, func):
        """Initialize the decorator with the function to wrap.

        Args:
            func: The function to be decorated.
        """
        update_wrapper(self, func)
        self.func = func

    def __get__(self, instance, owner):
        """Support instance methods by returning a functools.partial object.

        Args:
            instance: The instance the method is accessed through.
            owner: The class that the method belongs to.

        Returns:
            A functools.partial object that behaves like the method.
        """
        return functools.partial(self.__call__, instance)

    def __call__(self, *args, **kwargs):
        """
        Execute the decorated function, measure its maximum memory usage and
        execution time, and record the data.

        This method wraps the original function call with a mechanism to monitor
        and record the maximum memory usage during its execution.
        It starts a background thread dedicated to periodically checking the
        process's memory usage, allowing for the capture of the peak memory usage
        relative to the starting memory footprint.
        Additionally, it measures the total execution time of the function.

        The monitoring thread is initiated before the function call and is stopped
        immediately after the function has completed execution.
        This method ensures that the memory usage is checked throughout
        the execution period, capturing the maximum memory used.

        The memory usage and execution time data are appended to a class-level list,
        intended for later analysis or reporting.

        Args:
            *args: Variable length argument list passed to the decorated function.
            **kwargs: Arbitrary keyword arguments passed to the decorated function.

        Returns:
            The result of the decorated function call.

        Side Effects:
            - Starts a background thread to monitor memory usage during the function's
            execution.
            - Stops the monitoring thread after the function's execution completes.
            - Appends a record to `memory_data`, capturing the function name,
            maximum memory usage during execution (in MB),
            and the execution time (in seconds).
            - Prints the execution time of the function to the console.

        Note:
            The memory usage is measured in megabytes (MB),
            and the execution time is reported in seconds,
            with high precision (up to six decimal places).
        """
        # Start tracking memory allocation
        tracemalloc.start()

        process = psutil.Process()
        mem_start = process.memory_info().rss / (1024 * 1024)
        self.max_mem_usage = mem_start  # Initialize with starting memory
        self.monitoring = True

        # Start a background thread to monitor memory usage
        # The comma "," in "args=(process,)" is to make sure it's a tuple
        monitor_thread = threading.Thread(target=self.monitor_memory, args=(process,))
        monitor_thread.start()

        start_time = time.time()

        # This is where we actually run the function
        result = self.func(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time

        # Determine if the function is a method of a class
        # and fetch class name if available
        qual_name_parts = self.func.__qualname__.split(".")
        if (len(qual_name_parts) > 1) & ("<locals>" not in qual_name_parts):
            class_name = qual_name_parts[-2]
            exec_name = f"{class_name}.{self.func.__name__}"
        else:
            exec_name = f"{self.func.__name__}"

        print(f"Execution time - {exec_name} : {execution_time:.6f} seconds")

        # Stop the monitoring thread
        self.monitoring = False
        monitor_thread.join()

        MemoryUsageDecorator.execution_order += 1

        # Display memory usage information
        current, peak = tracemalloc.get_traced_memory()

        MemoryUsageDecorator.memory_data.append(
            {
                "function": exec_name,
                "peak_memory_usage_mb_rss": self.max_mem_usage,
                "incremental_memory_usage_mb_rss": self.max_mem_usage - mem_start,
                "peak_memory_usage_mb_python": peak,
                "current_memory_usage_mb_python": current,
                "execution_time_seconds": execution_time,
                "order": MemoryUsageDecorator.execution_order,
            }
        )

        print(f"Total peak memory usage observed (RSS): {self.max_mem_usage:.2f} MB")
        print(
            f"Peak memory usage increment due to function execution (RSS): "
            f"{self.max_mem_usage - mem_start:.2f} MB"
        )
        print(
            f"Current memory usage (tracemalloc): {current / 10**6:.2f} MB; Peak "
            f"(tracemalloc): {peak / 10**6:.2f} MB\n"
        )
        tracemalloc.stop()

        return result

    def monitor_memory(self, process):
        """Monitor memory usage of the process in a separate thread."""
        while self.monitoring:
            current_mem = process.memory_info().rss / (1024 * 1024)
            if current_mem > self.max_mem_usage:
                self.max_mem_usage = current_mem
            time.sleep(0.1)  # Sleep for a short period to prevent excessive CPU usage

    @classmethod
    def process_data(cls):
        """Process the recorded memory data into a pandas DataFrame.

        Returns:
            A pandas DataFrame summarizing the memory usage by function.
        """
        df = pd.DataFrame(cls.memory_data)
        grouped_df = (
            df.groupby("function")
            .agg(
                {
                    "peak_memory_usage_mb_rss": "sum",
                    "execution_time_seconds": "sum",
                    "incremental_memory_usage_mb_rss": "sum",
                    "peak_memory_usage_mb_python": "sum",
                    "execution_time_seconds": "sum",
                    "order": "first",
                }
            )
            .reset_index()
        )
        grouped_df = grouped_df.sort_values(by="order")
        return grouped_df.drop(columns=["order"])

    @classmethod
    def generate_report(cls, filename="memory_and_time_report.png", path="."):
        """
        Generate a dual plot report of:
        The memory usage data - Bar plot
        The execution time data - Line plot


        Args:
            filename: The name of the file to save the plot to.
            path: The directory path to save the file in.
        """
        print("Starting MemoryUsageDecorator report")
        df = cls.process_data()

        fig, ax1 = plt.subplots()

        # Plotting the memory usage
        color = "tab:red"
        ax1.set_xlabel("Function")
        ax1.set_ylabel("Max Memory Usage (MB)", color=color)
        ax1.bar(df["function"], df["peak_memory_usage_mb_python"], color=color)
        ax1.tick_params(axis="y", labelcolor=color)

        # Adjust x-axis labels for better readability
        ax1.set_xticklabels(df["function"], rotation=45, ha="right", fontsize=8)

        # Enable grid for primary axis only
        ax1.grid(True)
        # Customize the grid appearance
        ax1.grid(which="major", linestyle="-", linewidth="0.5", color="grey")
        ax1.grid(which="minor", linestyle=":", linewidth="0.5", color="black")

        # Creating a second y-axis for execution time
        ax2 = ax1.twinx()
        color = "tab:blue"
        ax2.set_ylabel("Execution Time (Seconds)", color=color)
        ax2.plot(
            df["function"],
            df["execution_time_seconds"],
            color=color,
            marker="o",
            linestyle="--",
        )
        ax2.tick_params(axis="y", labelcolor=color)

        # Disable grid for the secondary axis to avoid overlapping grids
        ax2.grid(False)

        # Final touches
        plt.tight_layout(pad=3.0)
        plt.title("Memory Usage and Execution Time by Function")

        os.makedirs(path, exist_ok=True)
        full_path = os.path.join(path, filename)
        plt.savefig(full_path)
        print(f"Report saved to {full_path}")


class UnivariateAnalysisReport:
    """
    This class provides a univariate analysis report.
    The report contains:
    - Variable (column) name
    - The number of missing/non-missing values
    - Variable stats (count, unique, mean, std, min, max, 25%, 50%, 75%, freq)
    - Variable distribution plot
    - Correlations plot
    """

    def __init__(self, df: pd.DataFrame, config_model) -> None:
        self._convert_int64(df)  # Convert all int columns to 'int64'
        self._convert_boolean(df)  # Convert boolean columns to 1/0
        self.df = df
        self.config_model = config_model
        self.version = config_model["model_version"]
        self.elements = []  # List of Flowable elements to add to the report
        self.styleSheet = getSampleStyleSheet()
        # Change document template to landscape orientation for correlation chart
        self.doc = SimpleDocTemplate(
            f"outputs/reports/univariate_analysis_report_{self.version}.pdf",
            pagesize=landscape(letter),  # landscape orientation
            leftMargin=50,
            rightMargin=50,
            topMargin=50,
            bottomMargin=50,
        )

    def _convert_int64(self, df: pd.DataFrame):
        """
        This method converts all integer dtypes to int64

        Args:
            df (pd.DataFrame): The main dataframe
        """
        for col in df.columns:
            if pd.api.types.is_integer_dtype(df[col]):
                df[col] = df[col].fillna(0)
                df[col] = df[col].astype("int64", errors="ignore")

    def _convert_boolean(self, df: pd.DataFrame):
        """
        Convert boolean columns to 1/0

        Args:
            df (pd.DataFrame): The main dataframe
        """
        for col in df.columns:
            if pd.api.types.is_bool_dtype(df[col]):
                df[col] = df[col].fillna(False).astype(int)

    def _save_plot_as_image(self, plt, img_height: int, img_width: int):
        """
        Saves the current plot to a BytesIO object and returns an Image object

        Args:
            plt: Matplotlib plot object
            img_height (int): The image height
            img_width (int): The image width

        Returns:
            An Image object ready to be added to elements
        """
        # Save the image to a BytesIO object
        img_buffer = BytesIO()
        # Save the plot to the buffer in PNG format
        plt.savefig(img_buffer, format="PNG")
        # Move to the beginning of the buffer
        img_buffer.seek(0)
        # Create an Image flowable with this buffer
        img = Image(img_buffer)
        # Adjust the image size if necessary
        img.drawHeight = img_height
        img.drawWidth = img_width

        return img

    def _dist_plot(self, column: str):
        """
        This method generates a distribution plot for a given column of the dataframe
        and adds it to the elements list

        Args:
            column (str): The column name
        """
        col_dtype = self.df[column].dtype
        if pd.api.types.is_object_dtype(col_dtype):
            plt.figure(figsize=(30, 25))

        # Determine the plot type based on data type
        if pd.api.types.is_object_dtype(col_dtype):
            self.df[column].value_counts().plot(kind="bar")
            plt.xticks(rotation=45)
        elif pd.api.types.is_bool_dtype(col_dtype):
            self.df[column].value_counts().plot(kind="bar")
        elif pd.api.types.is_numeric_dtype(col_dtype):
            self.df[column].hist()
        elif pd.api.types.is_datetime64_any_dtype(col_dtype):
            # Remove timezone information by converting to naive datetime
            tz_naive_series = self.df[column].dt.tz_localize(None)
            tz_naive_series.groupby(tz_naive_series.dt.to_period("M")).count().plot(
                kind="line"
            )
            plt.xticks(rotation=45)
        else:
            print(f"Unsupported column type: {col_dtype}")
            return

        # Design the plot
        if pd.api.types.is_object_dtype(col_dtype):
            plt.xticks(rotation=45, ha="right", fontsize=30)
            plt.yticks(fontsize=30)
            plt.title(f"Distribution of {column}", fontsize=80)
            plt.tight_layout(pad=2, h_pad=None, w_pad=None)

        else:
            plt.title(f"Distribution of {column}")
            plt.tight_layout()

        # Save the image to a BytesIO object
        img = self._save_plot_as_image(plt=plt, img_height=250, img_width=400)

        # Add this image to the elements
        self.elements.append(img)

        plt.close()

    def _calculate_missing_values(self, column: str):
        """
        This method calculates the number of missing and non missing values
        of the column and adds it to the elements list

        Args:
            column (str): The column name
        """
        # Calculate and add missing and non-missing values
        missing = self.df[column].isna().sum()
        non_missing = self.df[column].notna().sum()
        self.elements.append(
            Paragraph(
                f"Missing values: {int(float(missing)):,}",
                self.styleSheet["Normal"],
            )
        )
        self.elements.append(
            Paragraph(
                f"Non-missing values: {int(float(non_missing)):,}",
                self.styleSheet["Normal"],
            )
        )

    def _calculate_stats(self, column: str):
        """
        This method calculates all the stats (.describe()) of a specific column
        and adds it to the elements list

        Args:
            column (str): The column name
        """
        # Determine if the column is datetime
        is_datetime = pd.api.types.is_datetime64_any_dtype(self.df[column].dtype)

        # Describe the data, using datetime_is_numeric for datetime columns
        stats = self.df[column].describe().to_string()
        for line in stats.split("\n"):
            parts = line.split()  # Splitting each line into parts (name and value)
            if len(parts) > 1:  # Making sure it's not an empty line
                stat_name, stat_value = parts[0], parts[1]

                # Format numeric values as float
                if not is_datetime and stat_name.lower() in [
                    "count",
                    "unique",
                    "mean",
                    "std",
                    "min",
                    "max",
                    "25%",
                    "50%",
                    "75%",
                    "freq",
                ]:
                    stat_value = f"{float(stat_value):,}"  # Convert to float

                formatted_line = f"{stat_name}: {stat_value}"
            else:
                formatted_line = (
                    line  # In case it's an empty line or doesn't fit expected structure
                )

            self.elements.append(Paragraph(formatted_line, self.styleSheet["Normal"]))

    def _calculate_correlations_with_target_variable(
        self, column: str, target_column: str
    ):
        """
        This method calculates correlation of a column with the specified target column
        and adds it to the elements list

        Args:
            column (str): The column name
            target_column (str): The target variable name
        """
        col_dtype = self.df[column].dtype

        # Get the correlations
        # Default to Pearson correlation
        if pd.api.types.is_numeric_dtype(col_dtype):
            corr_value = self.df[column].corr(self.df[target_column], method="pearson")

            self.elements.append(
                Paragraph(
                    f"The correlation between {column} and {target_column}: "
                    f"{corr_value}",
                    self.styleSheet["Normal"],
                )
            )

    def _create_correlation_plot(self):
        """
        This method creates a correlation plot between all the numeric columns
        and adds it to the elements list
        """
        # Calculate the correlation matrix
        corr = self.df.corr(numeric_only=True)

        # Create a heatmap from the correlation matrix
        plt.figure(figsize=(30, 25))
        sns.heatmap(
            corr, annot=True, fmt=".1f", cmap="coolwarm", annot_kws={"size": 10}
        )
        # Design the plot
        plt.xticks(rotation=45, ha="right", fontsize=10)
        plt.yticks(fontsize=10)
        # plt.yticks(rotation=45, ha="right", va="top")
        plt.title("Variable Correlations", fontsize=22)
        plt.tight_layout()

        # Save the plot to a BytesIO object
        img = self._save_plot_as_image(plt=plt, img_height=500, img_width=790)

        # Set image to be centered
        # For some reason, LEFT sets it in the centre
        img.hAlign = "LEFT"

        self.elements.append(img)
        self.elements.append(PageBreak())

        plt.close()  # Close the plt object to free memory

    def create_report(self, drop_col_list: list, date_col_list: list):
        """
        This method generates the final report as a PDF

        Args:
            drop_col_list (list): List of columns to exclude from the analysis
                                  (mostly ID columns)
        """
        self.elements.append(
            Paragraph("Univariate Analysis Report", self.styleSheet["Title"])
        )
        self.elements.append(Spacer(1, 12))

        # Make sure date column have the correct dtype
        for i in date_col_list:
            self.df[i] = pd.to_datetime(self.df[i])

        for column in self.df.drop(columns=drop_col_list).columns:
            # Add section title for each feature
            self.elements.append(
                Paragraph(f"Feature: {column}", self.styleSheet["Heading2"])
            )

            # Calculate and add missing and non-missing values
            self._calculate_missing_values(column)
            # Add stats text
            self._calculate_stats(column)
            # Add the correlation with the target variable
            self._calculate_correlations_with_target_variable(
                column, self.config_model["target_col"]
            )
            # Add a space line
            self.elements.append(Spacer(1, 12))
            # Add the distribution plot image
            self._dist_plot(column)
            # Add a page break after each section
            self.elements.append(PageBreak())

        # Generate and add the correlation plot as the last page
        self._create_correlation_plot()

        # Build the PDF
        self.doc.build(self.elements)


class SplitOnId:
    """
    Class to split a DataFrame into training, validation, and test sets based on
    an ID column, using specified proportions.
    """

    def __init__(self, config_model: dict) -> None:
        """
        Initialize the SplitOnId object with a model configuration dictionary.

        Args:
            config_model (dict): Model configuration containing split proportions and
                                 target column information.
        """
        self.config_model = config_model

    def split_the_data(
        self, df: pd.DataFrame, id_column_name: str, is_save_split_dataset: bool = False
    ):
        """
        Split the DataFrame into training, validation, and test sets.

        Args:
            df (pd.DataFrame): The DataFrame to split.
            id_column_name (str): The name of the column to use as the identifier for
                splitting.
            is_save_split_dataset (bool): Whether to save the datasets.
                Defaults to False.

        Returns:
            tuple: A tuple containing six elements (X_train, y_train, X_valid, y_valid,
                   X_test, y_test), where each 'X' is a DataFrame of the feature
                   columns and each 'y' is a Series of the target column.
        """
        groups = df.groupby(id_column_name).size()

        # Split IDs into train and temp sets first
        non_train_size = 1 - self.config_model["split_dict"]["train_size"]
        train_ids, temp_ids = train_test_split(
            groups.index, test_size=non_train_size, random_state=101
        )
        # Split the temp set into validation and test sets
        valid_ids, test_ids = train_test_split(
            temp_ids, test_size=0.5, random_state=101
        )
        # Feature columns (all columns except the target variable)
        feature_columns = df.columns.difference([self.config_model["target_col"]])
        # Reconstruct datasets based on IDs
        X_train = df[df[id_column_name].isin(train_ids)][feature_columns]
        y_train = df[df[id_column_name].isin(train_ids)][
            self.config_model["target_col"]
        ]
        X_valid = df[df[id_column_name].isin(valid_ids)][feature_columns]
        y_valid = df[df[id_column_name].isin(valid_ids)][
            self.config_model["target_col"]
        ]
        X_test = df[df[id_column_name].isin(test_ids)][feature_columns]
        y_test = df[df[id_column_name].isin(test_ids)][self.config_model["target_col"]]
        if is_save_split_dataset:  # TODO Refactor the path
            X_train.to_parquet("outputs/data/raw/X_train.parquet")
            pd.DataFrame(y_train).to_parquet("outputs/data/raw/y_train.parquet")
            X_valid.to_parquet("outputs/data/raw/X_valid.parquet")
            pd.DataFrame(y_valid).to_parquet("outputs/data/raw/y_valid.parquet")
            X_test.to_parquet("outputs/data/raw/X_test.parquet")
            pd.DataFrame(y_test).to_parquet("outputs/data/raw/y_test.parquet")
        return X_train, y_train, X_valid, y_valid, X_test, y_test


class DatasetInfo:
    """
    A class to manage and display information about datasets used in machine learning,
    including training, validation, and test datasets.

    Attributes:
        X_train (pd.DataFrame): Features for the training set.
        y_train (pd.DataFrame): Target variable for the training set.
        X_valid (pd.DataFrame): Features for the validation set.
        y_valid (pd.DataFrame): Target variable for the validation set.
        X_test (pd.DataFrame): Features for the test set.
        y_test (pd.DataFrame): Target variable for the test set.
    """

    def __init__(
        self,
        X_train: pd.DataFrame,
        y_train: pd.DataFrame,
        X_valid: pd.DataFrame,
        y_valid: pd.DataFrame,
        X_test: pd.DataFrame,
        y_test: pd.DataFrame,
    ):
        """
        Initializes the DatasetInfo class with training, validation, and test data.

        Args:
            X_train (pd.DataFrame): Training dataset features.
            y_train (pd.DataFrame): Training dataset target variable.
            X_valid (pd.DataFrame): Validation dataset features.
            y_valid (pd.DataFrame): Validation dataset target variable.
            X_test (pd.DataFrame): Test dataset features.
            y_test (pd.DataFrame): Test dataset target variable.
        """
        self.X_train = X_train
        self.y_train = y_train
        self.X_valid = X_valid
        self.y_valid = y_valid
        self.X_test = X_test
        self.y_test = y_test

    def _print_split_df_info(self):
        """
        Prints the shape and spending average info of the train, test,
        and validation sets.
        """
        print(f"The shape of X_train is: {self.X_train.shape}")
        print(f"The shape of X_test is: {self.X_test.shape}")
        print(f"The shape of X_valid is: {self.X_valid.shape}\n")
        print(f"The spending average of y_train is: {round(self.y_train.mean())}")
        print(f"The spending average of y_test is: {round(self.y_test.mean())}")
        print(f"The spending average of y_valid is: {round(self.y_valid.mean())}\n")

    def get_datasets_info(self, is_saving_info: bool = True):
        """
        Gathers and prints information about each dataset, then returns it in the form
        of a dictionary.

        Args:
            is_saving_info (bool): Whether to save the dataset info. Defaults to True

        Returns:
            dict: A dictionary containing information about each dataset including
                  the length, width, and spending average.
        """
        datasets_info_dict = {}
        for i, n, z in zip(
            [self.X_train, self.X_valid, self.X_test],
            [self.y_train, self.y_valid, self.y_test],
            ["X_train", "X_valid", "X_test"],
        ):
            length, width = i.shape
            case = {
                "length": length,
                "width": width,
                "Spending Average": f"{n.mean()}",
            }
            datasets_info_dict[z] = case

        # Save the metrics
        if is_saving_info:
            with open("outputs/artifacts/dataset_info.json", "w") as json_file:
                json.dump(datasets_info_dict, json_file, indent=4)

        self._print_split_df_info()


class GetModel:
    """
    A class to manage and retrieve machine learning models based on configuration
    settings.

    Attributes:
        model_config (dict): A dictionary containing model configuration details.
        conc (str): A concatenated string derived from model configuration details used
            for naming.
    """

    def __init__(self, model_config: dict):
        """
        Initializes the GetModel instance with the given configuration.

        Args:
            model_config (dict): A dictionary containing the following keys:
                - model_name: The name of the model.
                - model_type: The type of the model.
                - model_name_suffix: A suffix for the model name.
                - model_version: The version of the model.
                - preprocessing_dir: Directory where preprocessing files are stored.
                - model_dir: Directory where model files are stored.
        """
        self.model_config = model_config

        model_name = self.model_config["model_name"]
        model_type = self.model_config["model_type"]
        model_name_suffix = self.model_config["model_name_suffix"]
        model_version = self.model_config["model_version"]

        self.conc = f"{model_name}_{model_type}_{model_name_suffix}_{model_version}"

    def get_model(self, model_type: str):
        """
        Retrieves and loads the model based on the given model type.

        Args:
            model_type (str): The type of the model to retrieve. It can be either
                "preprocess" or "model".

        Returns:
            The loaded model object.

        Raises:
            FileNotFoundError: If the model file does not exist at the specified path.
            ValueError: If the provided model_type is neither "preprocess" nor "model".
        """
        if model_type == "preprocess":
            prefix = "prep_train_"
            directory = self.model_config["preprocessing_dir"]
        elif model_type == "model":
            prefix = "model_"
            directory = self.model_config["model_dir"]
        elif model_type == "raw_pipeline":
            prefix = "raw_pipeline_"
            directory = self.model_config["raw_pipeline_dir"]
        else:
            raise ValueError(
                "model_type must be either 'preprocess' or 'model' or 'raw_pipeline'"
            )

        pkl_file_name = f"{prefix}{self.conc}.pkl"
        model_path = Path().cwd() / directory / pkl_file_name
        model = joblib.load(model_path)

        return model


class MissingColumnsFix:
    """
    A class to ensure that the prediction DataFrame has all the required columns
    used during the model training. If columns are missing, they are added with
    NaN values.

    Attributes:
        model (object): A trained machine learning model (e.g., XGBoost).
        pred_df (pd.DataFrame): A DataFrame containing the data for which predictions
            are to be made.
    """

    def __init__(self, model, pred_df) -> None:
        """
        Initialize the MissingColumnsFix class with a model and a prediction
        DataFrame.

        Args:
            model (object): A trained machine learning model (e.g., XGBoost).
            pred_df (pd.DataFrame): A DataFrame containing the data for which
                predictions are to be made.
        """
        self.model = model
        self.pred_df = pred_df

    def fix(self):
        """
        Ensure that the prediction DataFrame contains all the columns that were
        present during the model training. Missing columns are added with NaN
        values.
        """
        # Get the feature names from the trained model
        feature_names = self.model.get_booster().feature_names

        # Calculate the missing columns by comparing with the prediction DataFrame
        missing_columns = list(set(feature_names) - set(self.pred_df.columns.tolist()))

        # Assign NaN to the missing columns in the prediction DataFrame
        self.pred_df[missing_columns] = np.nan

        # Ensure the prediction DataFrame columns match the training feature names
        self.pred_df = self.pred_df[feature_names]


class CreatePredictionsDF:
    """
    A class to create a DataFrame with predictions and additional metadata.

    Attributes:
        pre_processed_pred_df (pd.DataFrame): Pre-processed DataFrame with necessary
            columns.
        pred (np.array): Array of predictions.
        general_col_list (list): List of general column names to include in the final
            DataFrame.
        model_config (dict): Dictionary containing model configuration details.
    """

    def __init__(
        self,
        pre_processed_pred_df: pd.DataFrame,
        pred: np.array,
        general_col_list: list,
        model_config: dict,
    ):
        """
        Initializes CreatePredictionsDF with the given pre-processed DataFrame,
        predictions, general column list, and model configuration.

        Args:
            pre_processed_pred_df (pd.DataFrame): Pre-processed DataFrame.
            pred (np.array): Array of predictions.
            general_col_list (list): List of general column names.
            model_config (dict): Dictionary containing model configuration.
        """
        self.pre_processed_pred_df = pre_processed_pred_df
        self.pred_df = pd.DataFrame(pred, columns=["total_spend_projection_eur_31d"])
        self.general_col_list = general_col_list
        self.model_config = model_config

    def create_df(self) -> pd.DataFrame:
        """
        Creates a DataFrame that merges the pre-processed DataFrame with predictions
        and adds metadata such as prediction timestamp and model version.

        Returns:
            pd.DataFrame: DataFrame containing the merged data with additional metadata.
        """
        # Extract relevant columns from the pre-processed DataFrame
        general_df = self.pre_processed_pred_df[self.general_col_list]

        # Merge the predictions with the general DataFrame
        predictions_df = general_df.reset_index(drop=True).merge(
            self.pred_df.reset_index(drop=True), left_index=True, right_index=True
        )

        # Calculate non-eur prediction
        predictions_df["total_spend_projection_31d"] = (
            predictions_df["total_spend_projection_eur_31d"]
            * predictions_df["currency_convert_rate"]
        )
        # Fix missing values in case one balance is missing and the other one isn't
        predictions_df.loc[
            pd.isna(predictions_df["balance_external_available_eur"])
            & ~pd.isna(predictions_df["balance_external_available"]),
            "balance_external_available_eur",
        ] = (
            predictions_df["balance_external_available"]
            / predictions_df["currency_convert_rate"]
        )

        predictions_df.loc[
            ~pd.isna(predictions_df["balance_external_available_eur"])
            & pd.isna(predictions_df["balance_external_available"]),
            "balance_external_available",
        ] = (
            predictions_df["balance_external_available_eur"]
            * predictions_df["currency_convert_rate"]
        )

        # Calculate predicted balances
        predictions_df["predicted_balance_eur"] = (
            predictions_df["balance_external_available_eur"]
            - predictions_df["total_spend_projection_eur_31d"]
        )
        predictions_df["predicted_balance"] = (
            predictions_df["balance_external_available"]
            - predictions_df["total_spend_projection_31d"]
        )

        predictions_df = predictions_df.drop(columns=["currency_convert_rate"])

        # Add a column with the current timestamp
        predictions_df.loc[:, "predicted_at"] = datetime.now()
        # Add a column with the model version
        predictions_df.loc[:, "model_version"] = self.model_config["model_version"]

        return predictions_df


class UploadToBQ:
    """
    A class used to upload data to Google BigQuery with environment-specific table
    suffixes.

    Attributes:
        bq_project (str): The Google BigQuery project ID.
        table_suffix (str): The suffix added to the table name based on the environment
            parameter.
    """

    def __init__(self, bq_project: str, env_param: str):
        """
        Initializes the UploadToBQ class with the specified BigQuery project and
        environment parameter.

        Args:
            bq_project (str): The Google BigQuery project ID.
            env_param (str): The environment parameter which determines the table
                suffix. Accepted values are "shadow", "prod", and any other value
                defaults to "_debug".
        """
        self.bq_project = bq_project
        if env_param == "shadow":
            self.table_suffix = "_shadow"
        elif env_param == "prod":
            self.table_suffix = ""
        else:
            self.table_suffix = "_debug"

    def single_upload(
        self,
        dataset: str,
        df: pd.DataFrame,
        table_name: str,
        is_hist: bool,
    ):
        """
        Uploads a single DataFrame to a specified BigQuery table.

        Args:
            dataset (str): The BigQuery dataset name.
            df (pd.DataFrame): The DataFrame to be uploaded.
            table_name (str): The base name of the BigQuery table.
            is_hist (bool): Determines the upload mode: if True, data is appended;
            if False, data replaces existing table content.
        """
        if is_hist:
            how_to_add = "append"
        else:
            how_to_add = "replace"

        full_table_name = table_name + self.table_suffix

        pandas_gbq.to_gbq(
            df,
            f"{dataset}.{full_table_name}",
            f"{self.bq_project}",
            if_exists=how_to_add,
        )


import json

import GPyOpt
import joblib
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, mean_squared_error
from utils.utils import MemoryUsageDecorator


class XGBoostRegressionCustom:
    """
    Encapsulates a custom XGBoost regression model, offering functionalities for model
    training, evaluation, and hyperparameter tuning via Bayesian optimization with
    Gaussian Processes.

    Allows customization of XGBoost regressor parameters, supports validation set
    evaluation, and uses configurable scoring metrics (e.g., MAE or MAPE) for
    performance assessment.

    Attributes:
        model_dict (dict): Configuration parameters for the XGBoost regressor.
        X_train (np.ndarray): Training data features.
        y_train (np.ndarray): Training data target values.
        X_valid (np.ndarray): Validation data features.
        y_valid (np.ndarray): Validation data target values.
        eval_set_list (list): List containing tuples of (features, target) for
            evaluation.
    """

    def __init__(self, model_dict, X_train, y_train, X_valid, y_valid):
        """
        Initializes the XGBoost regression model with specified training and validation
        data.

        Args:
            model_dict (dict): Dictionary with model configurations.
            X_train (np.ndarray): Training data features.
            y_train (np.ndarray): Training data target variable.
            X_valid (np.ndarray): Validation data features.
            y_valid (np.ndarray): Validation data target variable.
        """
        self.model_dict = model_dict
        self.X_train = X_train
        self.y_train = y_train
        self.X_valid = X_valid
        self.y_valid = y_valid
        self.eval_set_list = [
            (self.X_train, self.y_train),
            (self.X_valid, self.y_valid),
        ]

    def _mae_scorer(self, y_true, y_pred):
        """
        Calculates the Mean Absolute Error (MAE) between true and predicted values.

        Args:
            y_true (np.ndarray): True target values.
            y_pred (np.ndarray): Predicted target values.

        Returns:
            float: The MAE.
        """
        return mean_absolute_error(y_true, y_pred)

    def _rmse_scorer(self, y_true, y_pred):
        """
        Calculates the Mean Squared Error (MSE) between true and predicted values.

        Args:
            y_true (np.ndarray): True target values.
            y_pred (np.ndarray): Predicted target values.

        Returns:
            float: The MSE.
        """
        mse = mean_squared_error(y_true, y_pred)
        rmse = np.sqrt(mse)
        return rmse

    def _mape_scorer(self, y_true, y_pred):
        """
        Calculates the Mean Absolute Percentage Error (MAPE) between true and predicted
        values.

        Args:
            y_true (np.ndarray): True target values.
            y_pred (np.ndarray): Predicted target values.

        Returns:
            float: The MAPE.
        """
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

    def _objective_function(self, params):
        """
        Objective function for Bayesian optimization, evaluating model performance.

        Args:
            params (np.ndarray): Array of hyperparameter values.

        Returns:
            float: Evaluated score based on the specified eval_metric.
        """
        param_values = params[0]
        param_dict = {
            bound["name"]: (int(value) if bound["type"] == "discrete" else value)
            for bound, value in zip(self.bounds, param_values)
        }
        updated_params = {**self.model_dict["constant_params_xgb"], **param_dict}
        model = xgb.XGBRegressor(**updated_params)
        model.fit(self.X_train, self.y_train, eval_set=self.eval_set_list, verbose=True)
        predictions = model.predict(self.X_valid)
        if self.model_dict["constant_params_xgb"]["eval_metric"] == "mape":
            return self._mape_scorer(self.y_valid, predictions)
        elif self.model_dict["constant_params_xgb"]["eval_metric"] == "mae":
            return self._mae_scorer(self.y_valid, predictions)
        elif self.model_dict["constant_params_xgb"]["eval_metric"] == "mse":
            return self._mse_scorer(self.y_valid, predictions)

    def _save_model(self, model, model_dict: dict):
        """
        Saves the trained XGBoost model to a file in the specified directory with a
        constructed filename that includes various details from the model configuration
        dictionary.

        Args:
            model (XGBRegressor): The trained XGBoost model to be saved.
            model_dict (dict): A dictionary containing configuration details for the
                model. It must include keys for 'model_name', 'model_type',
                'model_name_suffix', 'model_version', and 'model_dir' which
                are used to construct the filename and determine the save
                location.

        The function uses joblib to serialize the model object to disk.
        """
        model_name = (
            f"{model_dict['model_name']}_{model_dict['model_type']}_"
            f"{model_dict['model_name_suffix']}_{model_dict['model_version']}"
        )
        filename = f"model_{model_name}.pkl"
        model_path = f"{model_dict['model_dir']}/{filename}"
        joblib.dump(model, model_path)
        print(f"Model saved to {model_path}")

    def xgb_train(self, is_saving_params: bool = True):
        """
        Trains the XGBoost model using predefined parameters and specified evaluation
        sets.

        Args:
            is_saving_params (bool): Whether to save the model's parameters.
                Defaults to True

        Returns:
            tuple: The trained model and its constant parameters.
        """
        model = xgb.XGBRegressor(**self.model_dict["constant_params_xgb"])
        model.fit(self.X_train, self.y_train, eval_set=self.eval_set_list, verbose=True)
        self._save_model(model, self.model_dict)

        # Save the parameters
        if is_saving_params:
            with open("outputs/artifacts/model_params.json", "w") as json_file:
                json.dump(self.model_dict["constant_params_xgb"], json_file, indent=4)

        return model

    def xgb_train_hpt_bayes(self, is_saving_params: bool = True):
        """
        Conducts hyperparameter tuning using Bayesian Optimization and trains the model
        with optimal parameters.

        Args:
            is_saving_params (bool): Whether to save the model's parameters.
                Defaults to True

        Returns:
            tuple: The best model and its hyperparameters.

        Notes:
            Acquisition Type "EI": Helps in deciding the next point to evaluate by
                calculating the expected improvement, balancing exploration of new
                regions and exploitation of known good regions.
                "EI" stands for Expected Improvement, which is one of the most common
                acquisition functions used in Bayesian optimization.
            exact_feval True: Indicates that the objective function returns precise,
                noise-free evaluations, allowing the model to more confidently use
                observed data for predicting the objective function landscape.
            Parameter Passing: When GPyOpt runs the optimization, it automatically
                generates sets of parameters based on the specified domain (self.bounds)
                and the internal logic of the Bayesian optimization process.
                It then calls the objective function (self._objective_function) with
                these parameter sets one at a time.
        """
        self.bounds = [
            {"name": "learning_rate", "type": "continuous", "domain": (0.01, 1.0)},
            {"name": "max_depth", "type": "discrete", "domain": (1, 10)},
            {"name": "n_estimators", "type": "discrete", "domain": (50, 1000)},
            {"name": "gamma", "type": "continuous", "domain": (1e-9, 0.5)},
            {"name": "colsample_bytree", "type": "continuous", "domain": (0.5, 1.0)},
            {"name": "min_child_weight", "type": "discrete", "domain": (1, 20)},
            {"name": "subsample", "type": "continuous", "domain": (0.5, 1.0)},
        ]
        optimizer = GPyOpt.methods.BayesianOptimization(
            f=self._objective_function,
            domain=self.bounds,
            acquisition_type="EI",
            exact_feval=True,
        )
        optimizer.run_optimization(max_iter=50)
        best_params = {
            bound["name"]: value for bound, value in zip(self.bounds, optimizer.x_opt)
        }
        final_model_params = {**self.model_dict["constant_params_xgb"], **best_params}
        final_model = xgb.XGBRegressor(**final_model_params)
        final_model.fit(
            self.X_train, self.y_train, eval_set=self.eval_set_list, verbose=True
        )
        self._save_model(final_model, self.model_dict)

        # Save the parameters
        if is_saving_params:
            with open("outputs/artifacts/model_params.json", "w") as json_file:
                json.dump(best_params, json_file, indent=4)

        return final_model


class XGBoostClassificationCustom:
    """
    A custom class for training XGBoost classification models, supporting
    basic training, hyperparameter tuning with Bayesian optimization, and
    grid search. It integrates with MLflow for experiment tracking and allows
    the use of custom evaluation sets and weight adjustments for handling
    imbalanced datasets.

    Parameters:
    - model_dict (dict): A dictionary containing model configuration parameters.
    - X_train (pd.DataFrame): Training feature dataset.
    - y_train (pd.DataFrame): Training target dataset.
    - X_valid (pd.DataFrame): Validation feature dataset.
    - y_valid (pd.DataFrame): Validation target dataset.
    - run: An object or identifier for the current MLFlow experiment run.
    - weights (int, optional): Scale factor for positive class weights, defaults to 1.

    Attributes:
    - eval_set_list (list): A list of tuples containing (X, y) pairs for training
        and validation sets.
    """

    def __init__(
        self,
        model_dict: dict,
        X_train: pd.DataFrame,
        y_train: pd.DataFrame,
        X_valid: pd.DataFrame,
        y_valid: pd.DataFrame,
        run,
        # weights=1,
    ):
        self.model_dict = model_dict
        self.X_train = X_train
        self.y_train = y_train
        self.X_valid = X_valid
        self.y_valid = y_valid
        self.eval_set_list = [
            (self.X_train, self.y_train),
            (self.X_valid, self.y_valid),
        ]
        # self.weights = weights
        self.run = run

    def xgb_train(self):
        """
        Trains an XGBoost classifier with predefined parameters and logs the
        training process and results to MLflow. Utilizes custom decorators for
        memory usage tracking and MLflow run management.

        Returns:
        tuple: A tuple containing the trained model and its constant parameters.
        """
        # Instantiate the XGB model
        model = xgb.XGBClassifier(**self.model_dict["constant_params_xgb"])
        # Fit the model
        model.fit(
            self.X_train,
            self.y_train,
            eval_set=self.eval_set_list,
            **self.model_dict["fit_params"],
        )
        mlflow.log_param("constant_params_xgb", self.model_dict["constant_params_xgb"])
        mlflow.log_param("fit_params", self.model_dict["fit_params"])
        mlflow.xgboost.log_model(model, "model")
        save_model(model=model, model_dict=self.model_dict)
        return model, self.model_dict["constant_params_xgb"]

    def xgb_train_hpt_bayes(self):
        """
        Performs hyperparameter tuning using Bayesian optimization on an XGBoost
        classifier. Logs the tuning process and the best model parameters to MLflow,
        and uses custom decorators for memory usage tracking and MLflow run management.

        Returns:
        tuple: A tuple containing the best model and its parameters after tuning.
        """
        # Instantiate the XGB model
        base_model = xgb.XGBClassifier(
            # scale_pos_weight=self.weights,
            random_state=101,
            early_stopping_rounds=10,
        )

        # Define the search spaces
        search_spaces_dict = {
            "learning_rate": Real(0.01, 1.0, "log-uniform"),
            # Boosting learning rate (xgb’s “eta”)
            "max_depth": Integer(1, 10),
            # Maximum tree depth for base learners.
            "n_estimators": Integer(50, 1000),
            # Number of boosting rounds.
            "gamma": Real(1e-9, 0.5, "log-uniform"),
            # Minimum loss reduction required to make a further partition
            # on a leaf node of the tree
            "min_child_weight": Integer(1, 20),
            # Minimum sum of instance weight(hessian) needed in a child.
            "subsample": Real(0.5, 1.0),
            # Ensuring subsample is between 50% and 100%
            "colsample_bytree": Real(0.5, 1.0),
            # Ensuring colsample_bytree is between 50% and 100%
            "eval_metric": ["aucpr"],
        }

        # Define the parameters for the "fit" method
        eval_set_dict = {"eval_set": self.eval_set_list}
        fit_params = {**self.model_dict["fit_params"], **eval_set_dict}

        cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=101)

        # Instanciate the Bayes optimizer
        bayes_search = BayesSearchCV(
            estimator=base_model,
            search_spaces=search_spaces_dict,
            n_iter=50,
            scoring="average_precision",
            n_jobs=-1,  # when -1; number of jobs is set to the number of cores
            cv=cv,
            random_state=101,
            fit_params=fit_params,
            verbose=10,
        )

        # Fit the model
        bayes_search.fit(self.X_train, self.y_train, eval_set=self.eval_set_list)

        print(f"The best params: {pd.Series(bayes_search.best_params_)}")

        model = xgb.XGBClassifier(
            **bayes_search.best_params_,
            # scale_pos_weight=self.weights
        )

        model.fit(
            self.X_train,
            self.y_train,
            eval_set=self.eval_set_list,
            **self.model_dict["fit_params"],
        )

        mlflow.log_param("constant_params_xgb", {**bayes_search.best_params_})
        mlflow.log_param("fit_params", self.model_dict["fit_params"])
        mlflow.xgboost.log_model(model, "model")
        save_model(model=model, model_dict=self.model_dict)

        return model, {**bayes_search.best_params_}

    def xgb_train_hpt_grid(self):
        """
        Performs hyperparameter tuning using grid search on an XGBoost classifier.
        Logs the tuning process and the best model parameters to MLflow, and uses
        custom decorators for memory usage tracking and MLflow run management.

        Returns:
        tuple: A tuple containing the best model and its parameters after tuning.
        """
        # Instantiate the XGB model
        base_model = xgb.XGBClassifier(
            # scale_pos_weight=self.weights,
            random_state=101,
            early_stopping_rounds=10,
        )

        # Define the search spaces
        search_spaces_dict = {
            "learning_rate": [0.1, 0.3],
            # Boosting learning rate (xgb’s “eta”)
            "max_depth": [5, 7],
            # Maximum tree depth for base learners.
            "n_estimators": [1000],
            # Number of boosting rounds.
            "gamma": [0, 0.5, 1],
            # Minimum loss reduction required to make a further partition
            # on a leaf node of the tree
            "eval_metric": ["aucpr"],
            # Metric used for monitoring the training result and early stopping.
            "reg_alpha": [0, 0.5, 1],
            # L1 regularization term on weights (xgb’s alpha).
            "reg_lambda": [0.5, 1, 5],
            # L2 regularization term on weights (xgb’s lambda).
            "base_score": [0.2, 0.5, 1],
            # The initial prediction score of all instances, global bias.
            "min_child_weight": [0, 1, 2, 3, 4, 5],
            # Minimum sum of instance weight(hessian) needed in a child.
        }

        # Define the parameters for the "fit" method
        eval_set_dict = {"eval_set": self.eval_set_list}
        fit_params = {**self.model_dict["fit_params"], **eval_set_dict}
        # fit_params.pop("early_stopping_rounds", None)

        cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=101)

        # Instanciate the Bayes optimizer
        grid_search = GridSearchCV(
            estimator=base_model,
            param_grid=search_spaces_dict,
            scoring="average_precision",
            n_jobs=-1,  # when -1; number of jobs is set to the number of cores
            cv=cv,
            verbose=10,
        )

        # Fit the model
        grid_search.fit(self.X_train, self.y_train, **fit_params)

        print(f"The best params: {pd.Series(grid_search.best_params_)}")

        model = xgb.XGBClassifier(
            **grid_search.best_params_,
            # scale_pos_weight=self.weights
        )

        model.fit(
            self.X_train,
            self.y_train,
            eval_set=self.eval_set_list,
            **self.model_dict["fit_params"],
        )

        mlflow.log_param("constant_params_xgb", {**grid_search.best_params_})
        mlflow.log_param("fit_params", self.model_dict["fit_params"])
        mlflow.xgboost.log_model(model, "model")
        save_model(model=model, model_dict=self.model_dict)

        return model, {**grid_search.best_params_}
