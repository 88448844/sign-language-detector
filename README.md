# Sign Language Detector

This is a Python based sign language detector that uses computer vision and machine learning to recognize and classify sign language gestures in real-time.

## Features

*   **Real-time gesture recognition:** The application uses your webcam to detect and classify sign language gestures in real-time.
*   **26-letter alphabet support:** The model is trained to recognize all 26 letters of the American Sign Language (ASL) alphabet.
*   **Easy to use:** The application is easy to set up and use. Simply run the `inference_classifier.py` script to start detecting gestures.
*   **Customizable:** You can easily retrain the model on your own custom gestures by following the data collection and training instructions below.

## Requirements

*   Python 3.10
*   OpenCV
*   MediaPipe
*   Scikit-learn

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/88448844/sign-language-detector.git
    cd sign-language-detector
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```
3.  **Install the requirements:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Collect Image Data

This is the most important step for creating an accurate model. You will need to collect a few hundred images for each sign language gesture you want to recognize.

Run the `collect_imgs.py` script to start the data collection process.
```bash
python collect_imgs.py
```
The script will open your webcam and guide you through the process. For each letter of the alphabet (A-Z), you will be prompted to press 'Q' to start collecting images. Make sure to move your hand around and show the gesture from different angles to create a robust dataset. The script will collect 200 images for each letter.

### 2. Create the Dataset

Once you have collected the images, run the `create_dataset.py` script to process them and create a dataset file (`data.pickle`). This script will extract the hand landmarks from the images and save them in a format that can be used for training the model.
```bash
python create_dataset.py
```

### 3. Train the Model

Run the `train_classifier.py` script to train a machine learning model on the dataset you created. This script will create a `model.p` file, which contains the trained model.
```bash
python train_classifier.py
```

### 4. Run the Sign Language Detector

Finally, run the `inference_classifier.py` script to see the sign language detector in action! The script will use your webcam to recognize and classify the gestures you trained it on.
```bash
python inference_classifier.py
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
