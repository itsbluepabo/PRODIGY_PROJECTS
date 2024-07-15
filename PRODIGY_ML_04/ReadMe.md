# Hand Gesture Recognition using LeapGestRecog Dataset

This project is the 4th task of my Prodigy Infotech internship. It involves building a convolutional neural network (CNN) to recognize hand gestures using the LeapGestRecog dataset.


## Project Structure

- **data_path**: The root directory where the dataset is stored.
- **image_data**: List containing images and their corresponding labels.
- **input_data**: Array of normalized images.
- **label**: One-hot encoded labels of the images.

## Model Architecture

The CNN model consists of the following layers:
- Convolutional Layers: 2 layers with filters of size 16 and 32, kernel size (3, 3), followed by Batch Normalization and ReLU activation.
- Max Pooling Layer: Pool size (2, 2) with Dropout (0.25).
- Fully Connected Layers: A dense layer with 128 units, followed by Batch Normalization and ReLU activation.
- Output Layer: Dense layer with 10 units and softmax activation.

## Training

The model is compiled with the Adam optimizer and categorical crossentropy loss. It is trained for 7 epochs with a batch size of 32.


## Usage

To run this project, follow these steps:

1. Install necessary libraries:
    ```bash
    pip install -q kaggle
    pip install numpy pandas matplotlib opencv-python keras scikit-learn
    ```

2. Download the dataset using Kaggle API:
    ```bash
    kaggle datasets download -d gti-upm/leapgestrecog
    unzip leapgestrecog.zip
    ```

3. Run the provided script to train the model.

## Conclusion

This project successfully demonstrates hand gesture recognition using a CNN model. It is a part of my Prodigy Infotech internship.



by Dipika Nikam

