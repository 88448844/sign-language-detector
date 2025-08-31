import os
import pickle

import mediapipe as mp
import cv2
import matplotlib.pyplot as plt


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.1)

DATA_DIR = './data'

if not os.path.exists(DATA_DIR) or not os.listdir(DATA_DIR):
    print(f"Error: Data directory '{DATA_DIR}' is empty or does not exist.")
    print("Please run collect_imgs.py to collect images first.")
    exit()

data = []
labels = []
for dir_ in os.listdir(DATA_DIR):
    dir_path = os.path.join(DATA_DIR, dir_)
    if not os.path.isdir(dir_path):
        continue
    if not os.listdir(dir_path):
        print(f"Warning: Directory '{dir_}' is empty, skipping.")
        continue
    for img_path in os.listdir(dir_path):
        data_aux = []

        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(dir_path, img_path))
        if img is None:
            print(f"Warning: Could not read image {img_path}, skipping.")
            continue
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            data.append(data_aux)
            labels.append(dir_)
        else:
            print(f"Warning: No landmarks detected for image {img_path} in directory {dir_}.")

with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)
