# SciPipe

SciPipe is a Python library designed to streamline data preprocessing, model training, evaluation, and general machine learning workflows. With modules for preprocessing, custom model training, and extensive model evaluation, it provides a robust framework for machine learning practitioners.

---

## Installation

Install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

## Modules

### 1. Data Splitting (`data_preprocessing.py`)

The `DataSplitter` class provides utilities for splitting data into training, validation, and test sets with options to split by ID, randomly, or by date.

#### Usage Example

```python
from preprocessing.data_preprocessing import DataSplitter

split_config = {
    "train_size": 0.8,
    "test_size": 0.1,
    "valid_size": 0.1
}
splitter = DataSplitter(df=data, target_column="target", split_config=split_config)
X_train, y_train, X_test, y_test = splitter.random_split()
```

### 2. Data Preprocessing (`data_preprocessing.py`)

The `DataPreprocessor` class provides flexible data preparation utilities including missing value imputation, encoding, and pipeline creation.

#### Usage Example

```python
from preprocessing.data_preprocessing import DataPreprocessor

# Define column configurations and pipeline steps
columns_dict = {
    "column1": {"class": "numeric", "imputer": "ArbitraryNumberImputer"},
    "column2": {"class": "categorical", "encoder": "OneHotEncoder"},
}
pipeline_steps_config = [
    {"name": "missing_imputation", "action": ArbitraryNumberImputer, "params": {"arbitrary_number": 0}},
    {"name": "one_hot_encoder", "action": OneHotEncoder}
]

# Initialize and fit the preprocessor
preprocessor = DataPreprocessor(columns_dict=columns_dict, pipeline_steps_config=pipeline_steps_config)
pipeline = preprocessor.fit(X_train)
datasets = data_preprocessor.transform({"X_train": X_train, "X_test": X_test, "X_valid": X_valid})
```

### 3. Model Training (`xgboost_classification.py`)

`XGBoostClassificationCustom` provides custom XGBoost classification model training. The class supports training, saving, and hyperparameter configuration.

#### Usage Example

```python
from models.xgboost_classification import XGBoostClassificationCustom

# Define model parameters
model_dict = {
    "constant_params_xgb": {"max_depth": 6, "learning_rate": 0.01, "n_estimators": 100},
}

# Initialize and train the model
xgb_classifier = XGBoostClassificationCustom(
    model_params=model_params,
    X_train=datasets["X_train"],
    y_train=y_train,
    X_valid=datasets["X_valid"],
    y_valid=y_valid
)
model = xgb_classifier.train_model()
```

### 4. Model Evaluation (`model_evaluator.py`)

`ClassificationEvaluator` provides a suite of evaluation metrics, visualizations, and tools to assess model performance, check for overfitting, and compare train/test metrics.

#### Key Functions:
- **Precision-Recall and ROC Curve**: Plots PR AUC and ROC curves.
- **Confusion Matrix and Classification Report**: Generates confusion matrix and detailed classification report.
- **SHAP Analysis**: Visualizes feature importance using SHAP values.
- **Overfitting Check**: Compares train and test metrics to identify potential overfitting.

#### Usage Example

```python
from evaluation.model_evaluator import ClassificationEvaluator

evaluator = ClassificationEvaluator(
    model=model,
    X_test=datasets["X_test"],
    y_test=y_test,
    X_train=datasets["X_train"],
    y_train=y_train,
    report_path="evaluation_report"
)
final_table_df = evaluator.evaluate(model_version="1.0", save_plots=True, show_plots=True)
```

#### Example Output:
This function generates plots for PR AUC, ROC Curve, and a confusion matrix, and saves a JSON report with evaluation metrics.

---

## Example Workflow

1. **Data Preprocessing**: Use `DataPreprocessor` to create and fit a preprocessing pipeline.
2. **Data Splitting**: Split data using `DataSplitter`.
3. **Model Training**: Train an XGBoost classifier with `XGBoostClassificationCustom`.
4. **Model Evaluation**: Evaluate the model’s performance with `ClassificationEvaluator`.

```python
# Split data
split_config = {
    "train_size": 0.8,
    "test_size": 0.1,
    "valid_size": 0.1
}
splitter = DataSplitter(df=data, target_column="target", split_config=split_config)
X_train, y_train, X_test, y_test = splitter.random_split()

# Define and preprocess
columns_dict = {...}  # Column configs
pipeline_steps_config = [...]
preprocessor = DataPreprocessor(columns_dict=columns_dict, pipeline_steps_config=pipeline_steps_config)
pipeline = preprocessor.fit(X_train)
datasets = data_preprocessor.transform({"X_train": X_train, "X_test": X_test, "X_valid": X_valid})

# Train model
model_params = {
    "objective": "binary:logistic",
    "eval_metric": "logloss",
    "use_label_encoder": False,
    "n_estimators": 100,
    "max_depth": 3,
    "learning_rate": 0.1,
    "scale_pos_weight": 1
}
xgb_classifier = XGBoostClassificationCustom(
    model_params=model_params,
    X_train=datasets["X_train"],
    y_train=y_train,
    X_valid=datasets["X_valid"],
    y_valid=y_valid
)
model = xgb_classifier.train_model()

# Evaluate model
evaluator = ClassificationEvaluator(
    model=model,
    X_test=datasets["X_test"],
    y_test=y_test,
    X_train=datasets["X_train"],
    y_train=y_train,
    report_path="evaluation_report"
)
final_table_df = evaluator.evaluate(model_version="1.0", save_plots=True, show_plots=True)
```

---

## License

This project is licensed under the MIT License.
