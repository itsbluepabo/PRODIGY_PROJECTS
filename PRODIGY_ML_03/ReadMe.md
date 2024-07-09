# Cat vs Dog Image Classification

This project is the third task of the Prodigy Infotech internship. It involves building an image classification model to distinguish between images of cats and dogs using a dataset from Kaggle. The project includes the following steps:

## Introduction

The goal is to create a machine learning model that can classify images of cats and dogs. The dataset used for this project is the Microsoft Cats vs. Dogs dataset, which contains images of cats and dogs in separate folders.

## Steps

### 1. Dataset Preparation

1. **Install Kaggle and upload the Kaggle API key.**
2. **Download the dataset from Kaggle.**
3. **Extract the dataset into a directory.**

### 2. Data Loading and Preprocessing

1. **Load images from the dataset.** 
   - Convert images to RGB.
   - Resize images to a fixed size of 64x64 pixels.
2. **Normalize the images.**
3. **Encode labels.** 
   - 0 for cats, 1 for dogs.
4. **Flatten the images for processing.**
5. **Split data into training and test sets.**

### 3. Data Visualization

1. **Display a grid of sample images** from the dataset to get an overview of the data.

### 4. Principal Component Analysis (PCA)

1. **Apply PCA to reduce the dimensionality** of the image data.

### 5. Subset Selection

1. **Select a subset of the data** for training the SVM model to improve computational efficiency.

### 6. Model Training

1. **Train an SVM model** with a linear kernel on the subset of the training data.

### 7. Model Evaluation

1. **Evaluate the model** using the test set.
2. **Print classification report** and accuracy score.

## Results

The trained SVM model is evaluated based on its accuracy and classification report, providing insights into the model's performance on the test dataset.

## Conclusion

This project demonstrates the process of building an image classification model from scratch, including data preprocessing, dimensionality reduction using PCA, and training a machine learning model using SVM. The evaluation results indicate the effectiveness of the model in distinguishing between cat and dog images.

## References

- [Microsoft Cats vs. Dogs Dataset on Kaggle](https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset)

This project is a part of the Prodigy Infotech internship.


