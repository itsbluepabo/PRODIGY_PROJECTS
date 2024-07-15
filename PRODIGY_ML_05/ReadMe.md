# FoodCaloriesEstimation

This project is the 5th task of my Prodigy Infotech internship. It involves fine-tuning a ResNet50 model on the Food-101 dataset to recognize various food classes.

## Dataset

The Food-101 dataset consists of 101 food categories with 1000 images each. In this project, we first work with a subset of 3 classes and later extend it to 11 classes.

## Project Structure

- **data_path**: The root directory where the dataset is stored.
- **image_data**: List containing images and their corresponding labels.
- **input_data**: Array of normalized images.
- **label**: One-hot encoded labels of the images.

## Model Architecture

We use the ResNet50 model pretrained on ImageNet and fine-tune it for the Food-101 dataset. The model architecture includes:
- Convolutional Layers: Pretrained ResNet50 layers.
- Global Average Pooling Layer.
- Fully Connected Layers: A dense layer with 128 units and ReLU activation, followed by Dropout (0.2).
- Output Layer: Dense layer with the number of units equal to the number of classes (3 or 11) and softmax activation.

## Training

The model is compiled with the SGD optimizer and categorical crossentropy loss. The training is performed for 30 epochs with a batch size of 16.

## Results

The model achieves good accuracy on the test set. The training and validation accuracy plots are shown below:

![Model Accuracy](accuracy_plot.png)
![Model Loss](loss_plot.png)

## Usage

To run this project, follow these steps:

1. Install necessary libraries:
    ```bash
    pip install tensorflow keras numpy matplotlib opencv-python
    ```

2. Download the dataset:
    ```bash
    wget http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz
    tar xzvf food-101.tar.gz
    ```

3. Run the provided script to train the model.

## Conclusion

This project demonstrates fine-tuning a pretrained ResNet50 model on the Food-101 dataset to recognize various food classes. It is a part of my Prodigy Infotech internship.

## Author

[Your Name]

