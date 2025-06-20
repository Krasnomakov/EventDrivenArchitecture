# 🚀 Ellie Connected v2: Advanced Interaction

This folder contains a more advanced and robust implementation of the event-driven architecture, featuring multiple interaction modes, enhanced gesture control, and a more modular structure.

<p align="center">
  <a href="https://drive.google.com/file/d/14VgP01R4UeSrjxccz6_b1pInGMkk3tBn/view?usp=sharing"><img src="https://img.shields.io/badge/Watch-Demo-4285F4?style=for-the-badge&logo=google-drive&logoColor=white" alt="Demo"/></a>
</p>

## ✨ Key Features

- **Multi-Mode System**: Seamlessly switch between different modes:
  - **Resting Animation**: An idle-state animation.
  - **Mode Selection**: Use hand gestures (number of fingers) to select the active mode.
  - **Brick Pong**: A fully playable game with a MediaPipe hand controller.
- **Movement Detection**: Uses OpenCV to detect movement and can relaunch the system if no activity is detected.
- **LLM Integration**: Includes a prototype (`ollamaToPixelatedLetters`) for interacting with a small language model using a hand controller.
- **Drawing Mode**: Allows users to draw on a simulated pixel LED wall.

## 📂 Core Components

-   `modeSelection/`: The main, event-driven master script that orchestrates the different modes. It handles the animation, mode selection via finger counting, and the Brick Pong game.

## 🧪 Experimental & Partial Implementations

This directory also contains various prototypes and components that explore different aspects of the architecture:

-   `brickPongVersions/`: Contains various attempts to optimize Python code with CuPy, Numba, and other methods to improve performance on the Jetson Nano.
-   `versions/`: Partial implementations of the event-driven architecture, including individual components like counters, detectors, and controllers.
-   `Flask server to handle events/`: A simple Flask server implementation designed to receive requests and trigger events in the system.
-   `ollamaToPixelatedLetters/`: A prototype that runs a small LLM (Ollama) with an AI hand controller and pixelated text output.
-   `drawing mode/`: Different animation and video projection experiments for drawing on the simulated LED wall.

## 💻 Technologies Used

<p align="center">
  <a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/></a>
  <a href="https://developers.google.com/mediapipe" target="_blank"><img src="https://img.shields.io/badge/MediaPipe-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="MediaPipe"/></a>
  <a href="https://opencv.org/" target="_blank"><img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/></a>
  <a href="https://flask.palletsprojects.com/" target="_blank"><img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/></a>
</p>
