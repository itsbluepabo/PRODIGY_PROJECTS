# Prodigy Infotech Internship Task 02

This repository contains the implementation of the second task for the Prodigy Infotech internship. The task is to perform customer segmentation using the KMeans clustering algorithm.

## Task Description

The goal is to segment customers into distinct groups based on their purchasing behavior and other relevant features. This segmentation helps in understanding the different types of customers and targeting them with personalized marketing strategies.

## Implementation

The implementation involves the following steps:

1. **Import Libraries**: Import necessary libraries for data manipulation, model training, evaluation, and visualization.
2. **Load Data**: Read the dataset from a CSV file named `customer_data.csv`.
3. **Select Features**: Specify the columns to use for clustering.
4. **Scale Features**: Normalize the features using `StandardScaler`.
5. **Determine Optimal Number of Clusters**: Use the Elbow method to find the optimal number of clusters.
6. **Train Model**: Create and train a KMeans model using the optimal number of clusters.
7. **Make Predictions**: Predict cluster labels for each customer.
8. **Evaluate Model**: Use metrics like inertia and silhouette score to evaluate the model's performance.
9. **Visualize Results**: Create scatter plots to visualize the clusters and their characteristics.

## Results

The model's performance is evaluated using inertia and silhouette score. The scatter plots visually represent the clusters and provide insights into the characteristics of each segment.

### Example Segments

Based on the clustering results, customers are segmented into different groups. Each group represents customers with similar purchasing behaviors and characteristics. This information can be used for targeted marketing and improving customer satisfaction.

## Conclusion

This project demonstrates the use of the KMeans clustering algorithm for customer segmentation. The resulting segments provide valuable insights into customer behavior, enabling more effective marketing strategies and improved customer relationship management.

---

*This is the second task of the Prodigy Infotech internship.*
