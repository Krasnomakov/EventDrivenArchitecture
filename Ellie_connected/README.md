# 🚀 Ellie Connected: User Recognition & Game Launcher

This project uses real-time user detection to automatically launch a game. It uses the MobileNetSSD model to detect a person, which triggers a Brick Pong game controlled by hand gestures via MediaPipe.

<p align="center">
  <a href="https://drive.google.com/file/d/1wkesS2F_0U0m1K3RxaZood4mVLbymh6d/view?usp=sharing"><img src="https://img.shields.io/badge/Watch-Demo-4285F4?style=for-the-badge&logo=google-drive&logoColor=white" alt="Demo"/></a>
</p>

## ✨ Features

- **Automatic Game Launch**: The system listens for a person to be detected and automatically launches a game.
- **User Detection**: Utilizes the lightweight MobileNetSSD model for efficient, real-time person detection.
- **Gesture Control**: Implements a MediaPipe-based hand controller for playing the Brick Pong game.
- **Event-Driven**: The components communicate through a simple file-based event system (`labels.txt`).

## 📂 Key Scripts

-   `real_time_object_detection_autoquit.py`: The core detection script. It runs continuously, and upon detecting a person, it writes the label to `labels.txt` and automatically terminates.
-   `contourWallAI_blocksNRows_eventDriven.py`: The game launcher. It monitors `labels.txt` and, upon detecting the "person" label, it launches a Brick Pong game with a MediaPipe hand controller.
-   `real_time_object_detection.py`: A testing script to verify that the MobileNet object detection is working correctly with your webcam.

## 🛠️ How to Run

This system requires running two scripts in parallel. Follow these steps:

1.  **Prepare the Camera**: Initially, ensure the camera is covered or pointing away so it does not detect a person.

2.  **Start the Game Listener**: In your first terminal, launch the game script. It will wait for the detection event.
    ```bash
    python contourWallAI_blocksNRows_eventDriven.py
    ```

3.  **Start the Person Detector**: In a second terminal, launch the person detection script.
    ```bash
    py -3.11 real_time_object_detection_autoquit.py --prototxt .\model\MobileNetSSD_deploy.prototxt.txt --model .\model\MobileNetSSD_deploy.caffemodel
    ```

4.  **Trigger the Event**: Uncover the camera. The detection script will see a person, write to `labels.txt`, and quit. The game script will then detect this event and launch Brick Pong.

## 💻 Technologies Used

<p align="center">
  <a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/></a>
  <a href="https://developers.google.com/mediapipe" target="_blank"><img src="https://img.shields.io/badge/MediaPipe-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="MediaPipe"/></a>
  <a href="https://opencv.org/" target="_blank"><img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/></a>
</p>

-   **MobileNetSSD**: The core model for object detection.
-   **Caffe Model**: The format used for the pre-trained MobileNetSSD.

