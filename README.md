# News Headline Classification

This project demonstrates how to classify news headlines into predefined categories using a machine learning pipeline built with Scikit-learn.

## 📄 Overview

The pipeline:
- Loads a dataset of news headlines
- Preprocesses the text data using TF-IDF vectorization
- Trains a Logistic Regression classifier
- Evaluates the model using accuracy and classification metrics

## 📁 Dataset

Expected input: News_Category_Dataset_v3.json  
- The dataset should contain at least two columns: headline and category.
- Format: JSON (one object per line) or a CSV file with the same structure.

## ⚙ Dependencies

Install the required libraries with:

```bash
pip install pandas scikit-learn
