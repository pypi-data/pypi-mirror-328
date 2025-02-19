import joblib
import xgboost as xgb


class XGBoostClassificationCustom:
    """
    A custom class for training XGBoost classification models, supporting basic
    training and model saving.

    Attributes:
        model_params (dict): Dictionary of model parameters for the XGBoost classifier.
        X_train (pd.DataFrame): Training feature dataset.
        y_train (pd.Series): Training target dataset.
        X_valid (pd.DataFrame): Validation feature dataset.
        y_valid (pd.Series): Validation target dataset.
        eval_set_list (list): List containing tuples of (features, target) for training
            and validation evaluation.
    """

    def __init__(self, model_params, X_train, y_train, X_valid=None, y_valid=None):
        """
        Initializes the XGBoostClassificationCustom class with specified training
        and validation data.

        Args:
            model_params (dict): Dictionary with model configurations for XGBoost.
            X_train (pd.DataFrame): Training data features.
            y_train (pd.Series): Training data target values.
            X_valid (pd.DataFrame, optional): Validation data features.
            y_valid (pd.Series, optional): Validation data target values.
        """
        self.model_params = model_params
        self.X_train = X_train
        self.y_train = y_train
        self.X_valid = X_valid
        self.y_valid = y_valid
        self.eval_set_list = [(self.X_train, self.y_train)]
        if self.X_valid is not None and self.y_valid is not None:
            self.eval_set_list.append((self.X_valid, self.y_valid))

    def train_model(self):
        """
        Trains an XGBoost classifier using the provided model parameters and evaluation
        set.

        Returns:
            xgb.XGBClassifier: The trained XGBoost model.
        """
        # Initialize and fit the XGB classifier
        model = xgb.XGBClassifier(**self.model_params)
        model.fit(self.X_train, self.y_train, eval_set=self.eval_set_list, verbose=True)
        return model

    def save_model(self, model, filepath):
        """
        Saves the trained model to the specified filepath in a .joblib format.

        Args:
            model (xgb.XGBClassifier): The trained XGBoost model to save.
            filepath (str): The file path where the model will be saved.
        """
        joblib.dump(model, filepath)
        print(f"Model saved to {filepath}")
