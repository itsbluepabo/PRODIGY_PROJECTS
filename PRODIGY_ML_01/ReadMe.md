# Prodigy Infotech Internship Task 01

This repository contains the implementation of the first task for the Prodigy Infotech internship. The task is to implement a linear regression model to predict the prices of houses based on their square footage, number of bedrooms, and number of bathrooms.

## Task Description

The goal is to create a linear regression model that can predict house prices using the following features:
- GrLivArea: Above ground living area in square feet
- BedroomAbvGr: Number of bedrooms above ground
- FullBath: Number of full bathrooms

## Implementation

The implementation involves the following steps:

1. **Import Libraries**: Import necessary libraries for data manipulation, model training, evaluation, and visualization.
2. **Load Data**: Read the dataset from a CSV file named `train.csv`.
3. **Select Features and Target**: Specify the columns to use as features and the target column.
4. **Scale Features**: Normalize the features using `StandardScaler`.
5. **Split Data**: Split the data into training and testing sets.
6. **Train Model**: Create and train a linear regression model using the training data.
7. **Make Predictions**: Predict house prices on the test set.
8. **Evaluate Model**: Calculate mean squared error (MSE) and R-squared (R²) to evaluate the model's performance.
9. **Plot Results**: Create a scatter plot comparing actual prices vs. predicted prices.
10. **Predict New Data**: Predict the price of a new house with specific features.

## Results

The model's performance is evaluated using Mean Squared Error (MSE) and R-squared (R²) metrics. The scatter plot visually compares the actual prices with the predicted prices, giving an indication of the model's accuracy.

### Example Predictions

For a house with:
- 1000 square feet, 3 bedrooms, and 2 full bathrooms:
  - Predicted Price: \$X (replace X with actual value)
  
For a house with:
- 2000 square feet, 3 bedrooms, and 2 full bathrooms:
  - Predicted Price: \$Y (replace Y with actual value)

## Conclusion

This project demonstrates a simple yet effective implementation of a linear regression model for predicting house prices based on specific features. The model provides a good starting point for more advanced analyses and improvements.

---

*This is the first task of the Prodigy Infotech internship.*


