import json
import os
from typing import List, Optional

import dataframe_image as dfi
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import shap
from IPython.display import display
from sklearn.calibration import calibration_curve
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    PrecisionRecallDisplay,
    auc,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_recall_curve,
    roc_curve,
)


class ClassificationEvaluator:
    """
    Evaluates classification model performance, visualizes metrics, and detects
    overfitting by comparing train and test metrics.
    """

    def __init__(
        self,
        model,
        X_test: pd.DataFrame,
        y_test: pd.Series,
        X_train: Optional[pd.DataFrame] = None,
        y_train: Optional[pd.Series] = None,
        report_path: str = "evaluation_report",
    ):
        """
        Initializes the evaluator with model, test, and optional train data.

        Args:
            model: Trained model for evaluation.
            X_test (pd.DataFrame): Test features.
            y_test (pd.Series): Test target values.
            X_train (pd.DataFrame, optional): Train features. Default is None.
            y_train (pd.Series, optional): Train target values. Default is None.
            report_path (str): Path to save the evaluation report. Default is
                "evaluation_report".
        """
        self.model = model
        self.X_test = X_test
        self.y_test = y_test
        self.X_train = X_train
        self.y_train = y_train
        self.report_path = report_path
        self.probs_test = self.model.predict_proba(X_test)[:, 1]
        self.probs_train = (
            self.model.predict_proba(X_train)[:, 1] if X_train is not None else None
        )
        os.makedirs(report_path, exist_ok=True)

    def calculate_metrics(self, y, probs) -> dict:
        """
        Calculates precision-recall AUC, ROC AUC, and Gini coefficient.

        Returns:
            dict: A dictionary with calculated metrics.
        """
        precision, recall, thresholds_pr = precision_recall_curve(y, probs)
        fpr, tpr, thresholds_roc = roc_curve(y, probs)
        aucpr = auc(recall, precision)
        roc_auc = auc(fpr, tpr)
        gini = 2 * roc_auc - 1

        return {
            "precision": precision,
            "recall": recall,
            "thresholds_pr": thresholds_pr,
            "fpr": fpr,
            "tpr": tpr,
            "thresholds_roc": thresholds_roc,
            "aucpr": aucpr,
            "roc_auc": roc_auc,
            "gini": gini,
        }

    def plot_pr_auc_curve(
        self, metrics: dict, save: bool = False, show: bool = False
    ) -> None:
        """
        Plots the Precision-Recall (PR) AUC curve with a no-skill baseline.

        Args:
            metrics (dict): Dictionary containing calculated precision, recall, and
                PR AUC.
            save (bool): If True, saves the plot to the report path. Default is False.
            show (bool): If True, displays the plot. Default is False.
        """
        precision = metrics["precision"]
        recall = metrics["recall"]
        pr_auc_score = metrics["aucpr"]

        # Plot PR AUC curve
        _, ax = plt.subplots(figsize=(8, 6))
        pr_display = PrecisionRecallDisplay(precision=precision, recall=recall)
        pr_display.plot(ax=ax, name=f"PR AUC = {pr_auc_score:.2f}")

        # Calculate and plot the no-skill line
        no_skill = len(self.y_test[self.y_test == 1]) / len(self.y_test)
        ax.plot(
            [0, 1],
            [no_skill, no_skill],
            linestyle="--",
            label=f"No Skill = {no_skill:.2f}",
        )

        # Display the no-skill line value above the line
        plt.text(
            0.5,
            no_skill + 0.02,
            f"No Skill = {no_skill:.2f}",
            ha="center",
            color="gray",
        )

        # General plot settings
        plt.title("Precision-Recall Curve")
        plt.legend()
        ax.set_aspect(0.75)

        if save:
            plt.savefig(f"{self.report_path}/pr_auc_curve.png")
        if show:
            plt.show()
        plt.close()

    def plot_roc_curve(
        self, metrics: dict, save: bool = False, show: bool = False
    ) -> None:
        """
        Plots the ROC curve.

        Args:
            metrics (dict): Dictionary containing calculated metrics.
            save (bool): If True, saves the plot to the report path. Default is False.
            show (bool): If True, displays the plot. Default is False.
        """
        fpr, tpr, roc_auc = metrics["fpr"], metrics["tpr"], metrics["roc_auc"]
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, label=f"ROC AUC = {roc_auc:.2f}")
        plt.plot([0, 1], [0, 1], linestyle="--", label="No Skill = 0.5")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("ROC Curve")
        plt.legend(loc="lower right")
        if save:
            plt.savefig(os.path.join(self.report_path, "roc_curve.png"))
        if show:
            plt.show()
        plt.close()

    def get_best_f1_threshold(self) -> float:
        """
        Calculates the F1 score for various thresholds and returns the threshold
        with the highest F1 score.

        Returns:
            float: The threshold that gives the best F1 score.
        """
        thresholds = np.linspace(0, 1, 100)  # 100 thresholds between 0 and 1
        best_threshold = 0.0
        best_f1 = 0.0

        for threshold in thresholds:
            # Convert probabilities to binary predictions at the current threshold
            preds = (self.probs_test >= threshold).astype(int)

            # Calculate F1 score
            score = f1_score(self.y_test, preds)

            # Update the best threshold if the current F1 score is higher
            if score > best_f1:
                best_f1 = score
                best_threshold = threshold

        return best_threshold

    def plot_confusion_matrix(self, save: bool = False, show: bool = False) -> None:
        """
        Plots the confusion matrix using the optimal threshold for the best F1 score.

        This method calculates predictions based on the threshold that maximizes
        the F1 score and generates a confusion matrix plot. The plot title
        includes the best F1 threshold used for classification.

        Args:
            save (bool): If True, saves the plot to the report path. Default is False.
            show (bool): If True, displays the plot. Default is False.
        """
        best_f1 = self.get_best_f1_threshold()
        preds = (self.probs_test >= best_f1).astype(int)
        cm = confusion_matrix(self.y_test, preds)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot(cmap="Blues", values_format="d")
        plt.title(f"Confusion Matrix (Threshold: {best_f1:.2f})")
        if save:
            plt.savefig(os.path.join(self.report_path, "confusion_matrix.png"))
        if show:
            plt.show()
        plt.close()

    def plot_classification_report(
        self, save: bool = False, show: bool = False
    ) -> None:
        """
        Plots the classification report as a heatmap using the best F1-score
        threshold.

        The classification report includes precision, recall
        and F1-score for each class.
        The best threshold for the F1 score is automatically selected using the
        `get_best_f1_threshold` method.

        Args:
            save (bool): If True, saves the plot as 'classification_report.png'
                in the report path. Default is False.
            show (bool): If True, displays the plot immediately. Default is False.

        Returns:
            None
        """
        # Get the best threshold for F1 score
        best_f1_threshold = self.get_best_f1_threshold()
        preds = (self.probs_test >= best_f1_threshold).astype(int)

        # Generate classification report as DataFrame
        report_dict = classification_report(self.y_test, preds, output_dict=True)
        report_df = pd.DataFrame(report_dict).transpose()

        # Plot the heatmap
        plt.figure(figsize=(10, 4))
        sns.heatmap(
            report_df.iloc[:, :-1],
            annot=True,
            cmap="Blues",
            fmt=".2f",
            cbar=False,
            linewidths=0.5,
            linecolor="black",
        )
        plt.title(f"Classification Report (Threshold: {best_f1_threshold:.2f})")
        plt.tight_layout()

        # Save or show the plot
        if save:
            plt.savefig(os.path.join(self.report_path, "classification_report.png"))
        if show:
            plt.show()
        plt.close()

    def plot_score_distribution(
        self, bins: int = 20, save: bool = False, show: bool = False
    ) -> None:
        """
        Plots the score distribution with different colors per class.

        Args:
            bins (int): Number of bins for histogram.
            save (bool): If True, saves the plot to the report path. Default is False.
            show (bool): If True, displays the plot. Default is False.
        """
        test_data = pd.DataFrame({"score": self.probs_test, "target": self.y_test})

        plt.figure(figsize=(8, 6))
        sns.histplot(
            data=test_data,
            x="score",
            hue="target",
            bins=bins,
            kde=True,
            stat="density",
            common_norm=False,
            palette={0: "blue", 1: "red"},
        )
        plt.title("Score Distribution by Class")
        plt.xlabel("Predicted Probability")
        plt.ylabel("Density")
        if save:
            plt.savefig(os.path.join(self.report_path, "score_distribution.png"))
        if show:
            plt.show()
        plt.close()

    def pred_plot(
        self,
        xmin: float = 0,
        xmax: float = 1,
        bins: int = 50,
        save: bool = False,
        show: bool = False,
    ) -> None:
        """
        Generates a histogram of the predicted probabilities.

        Args:
            xmin (float): Minimum x-axis limit.
            xmax (float): Maximum x-axis limit.
            bins (int): Number of bins for histogram.
            save (bool): If True, saves the plot to the report path. Default is False.
            show (bool): If True, displays the plot. Default is False.
        """
        plt.figure(figsize=(8, 6))
        plt.hist(self.probs_test, bins=bins, edgecolor="black")
        plt.xlim(left=xmin, right=xmax)
        plt.xlabel("Predicted Probability")
        plt.ylabel("Frequency")
        plt.title("Distribution of Predicted Probabilities")
        if save:
            plt.savefig(os.path.join(self.report_path, "pred_plot.png"))
        if show:
            plt.show()
        plt.close()

    def show_shap_summary(self, save: bool = False, show: bool = False) -> None:
        """
        Generates a SHAP summary plot for feature importance.

        Args:
            save (bool): If True, saves the plot to the report path. Default is False.
            show (bool): If True, displays the plot. Default is False.
        """
        explainer = shap.Explainer(self.model)
        shap_values = explainer(self.X_test)
        shap.summary_plot(shap_values, self.X_test, show=show)
        if save:
            plt.savefig(os.path.join(self.report_path, "shap_summary.png"))
        plt.close()

    def show_calibration_curve(
        self, n_bins: int = 10, save: bool = False, show: bool = False
    ) -> None:
        """
        Plots a calibration curve for model probability calibration.

        Args:
            n_bins (int): Number of bins for the curve. Default is 10.
            save (bool): If True, saves the plot to the report path. Default is False.
            show (bool): If True, displays the plot. Default is False.
        """
        plt.figure(figsize=(8, 6))
        fop, mpv = calibration_curve(self.y_test, self.probs_test, n_bins=n_bins)
        plt.plot([0, 1], [0, 1], linestyle="--", label="Perfectly calibrated")
        plt.plot(mpv, fop, marker=".", label="Model")
        plt.xlabel("Mean predicted probability")
        plt.ylabel("Fraction of positives")
        plt.title("Calibration Curve")
        plt.legend()
        if save:
            plt.savefig(os.path.join(self.report_path, "calibration_curve.png"))
        if show:
            plt.show()
        plt.close()

    def generate_general_df(
        self, original_columns: List[str], model_version: str
    ) -> pd.DataFrame:
        """
        Creates a general DataFrame with original columns and metadata.

        Args:
            original_columns (list): List of original columns to keep.
            model_version (str): Model version identifier.

        Returns:
            pd.DataFrame: General DataFrame with additional metadata.
        """
        df_general = self.X_test[original_columns].copy()
        df_general["predicted_at"] = pd.Timestamp.now()
        df_general["model_version"] = model_version
        return df_general

    def final_table(
        self,
        columns: Optional[List[str]] = None,
        model_version: str = None,
        save: bool = False,
    ) -> pd.DataFrame:
        """
        Generates the final evaluation table with probabilities and metadata.

        Args:
            columns (list, optional): Columns for the final table.
            model_version (str): Model version identifier.
            save (bool): If True, saves the table. Default is False.

        Returns:
            pd.DataFrame: Final evaluation table.
        """
        df_general = self.generate_general_df(
            original_columns=columns or [], model_version=model_version
        )

        if columns is None:
            df_general.reset_index(inplace=True)

        df_final = df_general.copy()
        df_final["probability"] = self.probs_test
        df_final["actual"] = self.y_test.values

        if save:
            df_final.to_csv(
                os.path.join(self.report_path, "final_evaluation_table.csv"),
                index=False,
            )

        return df_final

    def generate_report(self, metrics: dict) -> None:
        """
        Generates and saves a JSON report with calculated metrics.

        Args:
            metrics (dict): Dictionary with calculated metrics.
        """
        report = {
            "AUC PR": metrics["aucpr"],
            "ROC AUC": metrics["roc_auc"],
            "Gini Coefficient": metrics["gini"],
        }
        with open(
            os.path.join(self.report_path, "evaluation_report.json"),
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(report, file, indent=4)

    def check_overfitting(self, metrics_test: dict, metrics_train: dict) -> None:
        """
        Checks for overfitting or underfitting by comparing train and test metrics.

        This method calculates the difference between train and test scores for key
        metrics (AUC PR and ROC AUC). If the train score is more than 5%
        higher than the test score, it signals potential overfitting. Conversely, if
        the test score is more than 5% higher than the train score, it indicates
        potential underfitting.

        Args:
            metrics_test (dict): Dictionary of evaluation metrics for the test set.
            metrics_train (dict): Dictionary of evaluation metrics for the train set.

        Prints:
            str: Message indicating potential overfitting or underfitting if the
            train-test difference exceeds 5%.
        """
        for metric in ["aucpr", "roc_auc"]:
            test_score = metrics_test[metric]
            train_score = metrics_train[metric]
            diff = (train_score - test_score) / test_score
            if diff > 0.05:
                print(f"Overfitting alert: Train-Test {metric} diff is {diff:.2%}")
            elif diff < -0.05:
                print(f"Underfitting alert: Train-Test {metric} diff is {diff:.2%}")

    def evaluate(
        self,
        model_version: str,
        save_plots: bool = False,
        show_plots: bool = False,
        columns: Optional[List[str]] = None,
    ) -> pd.DataFrame:
        """
        Runs full evaluation, including metrics, visualizations, and report generation.

        Args:
            model_version (str): Model version identifier.
            save_plots (bool): If True, saves all plots and final table.
            show_plots (bool): If True, displays all plots. Default is False.
            columns (list, optional): Columns for final evaluation table.

        Returns:
            pd.DataFrame: Final evaluation table.
        """
        metrics_test = self.calculate_metrics(y=self.y_test, probs=self.probs_test)
        metrics_train = self.calculate_metrics(y=self.y_train, probs=self.probs_train)
        self.plot_pr_auc_curve(metrics_test, save=save_plots, show=show_plots)
        self.plot_roc_curve(metrics_test, save=save_plots, show=show_plots)
        self.plot_confusion_matrix(save=save_plots, show=show_plots)
        self.plot_classification_report(save=save_plots, show=show_plots)
        self.plot_score_distribution(save=save_plots, show=show_plots)
        self.pred_plot(save=save_plots, show=show_plots)
        self.show_shap_summary(save=save_plots, show=show_plots)
        self.show_calibration_curve(save=save_plots, show=show_plots)
        self.generate_report(metrics_test)
        final_table_df = self.final_table(
            columns=columns, model_version=model_version, save=save_plots
        )
        self.check_overfitting(metrics_test=metrics_test, metrics_train=metrics_train)

        return final_table_df
