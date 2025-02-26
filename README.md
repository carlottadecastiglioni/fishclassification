# fishclassification


# Project Overview

This project focuses on classifying different fish species using machine learning techniques. The dataset consists of various fish species with imbalanced class distributions. The goal is to build an effective classification model that can accurately identify fish species from the given features.

# Dataset

Source: The dataset consists of 10,000 samples.

Classes: 10 fish species (Tuna, Catfish, Snapper, Trout, Swordfish, Bass, Shark, Goldfish, Salmon, Clownfish).

Imbalance: Some classes have significantly fewer samples than others.

File format: The dataset is stored in an Excel file (fish_classification_dataset.xlsx).

# Preprocessing:

Data cleaning and handling missing values.

Feature scaling and transformation.

Addressing class imbalance using SMOTE.

# Modeling:

Logistic Regression was used initially.

Experimented with different classifiers using a randomized grid search.

Hyperparameter tuning using validation curves (max_depth parameter).

# Evaluation:

Metrics: F1-macro, accuracy, and precision-recall analysis.

# Repository Structure

├── fish_classification.ipynb \
├── fish_classification_dataset.xlsx \
├── README.md \ 
└── requirements.txt
