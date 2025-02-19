from setuptools import find_packages, setup

setup(
    name="SciPipe",
    version="0.1.2",
    description="A data science and machine learning library that wraps and extends popular tools",  # noqa: E501
    author="Ron Snir",
    author_email="ronsnirmail@gmail.com",
    url="https://github.com/ronsnir/SciPipe",
    packages=find_packages(),
    install_requires=[
        "numpy>=2.0.2",
        "pandas>=2.2.3",
        "scikit-learn>=1.5.2",
        "matplotlib>=3.9.2",
        "seaborn>=0.13.2",
        "xgboost>=2.1.2",
        "joblib>=1.4.2",
        "feature-engine>=1.8.1",
        "shap>=0.46.0",
        "dataframe-image>=0.2.6",
        "Jinja2>=3.1.4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
