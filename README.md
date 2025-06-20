# 🤖 AI Event-Driven 8-bit LED Screen

An interactive art & gaming project using event-driven architecture to control an 8-bit LED screen simulation.

## 🚀 Overview

This repository contains prototypes and components of an AI event-driven architecture for controlling an 8-bit LED screen simulation. The project includes several modes such as animations, drawing, games, and interaction with large language models (LLM).

## ✨ Features

- **Real-time Animations**: Dynamic animations on an 8-bit LED screen.
- **Gesture Control**: Hand and pose recognition for interactive experiences.
- **Game Integrations**: Classic games like Snake and Brick Pong controlled by gestures.
- **User Recognition**: Detects and recognizes users to personalize experiences.
- **Object Detection**: Uses YOLOv9 for video effects based on detected objects.
- **Sound Detection**: Reacts to sound levels in the environment.

## 📦 Components & Demos

Here's a breakdown of the different components in this repository and links to their demos.

| Component | Description | Demo |
|---|---|---|
| `C/` | Various animations, movement detection, and pose/hand recognition on Jetson Nano. Includes snake and brick pong games implemented in C/C++. | <ul><li>[🎬 Event-Driven Architecture](https://drive.google.com/file/d/1IVOBHTk2JU5LjdZWM55VMYE9VPgmm1oh/view?usp=sharing)</li><li>[🧱 Brick Pong](https://drive.google.com/file/d/15immDvVE9rzHjOSAga4jwyM3pBoCWAVq/view?usp=sharing)</li><li>[🐍 Snake](https://drive.google.com/file/d/13E9lRFCfXW6GLsjpQeqEjfcrZtrPX8RK/view?usp=sharing)</li></ul> |
| `Ellie_connected/` | MobileNet for user recognition, Mediapipe for BrickPong hand controller, autolaunch when user is detected. | [▶️ Watch Demo](https://drive.google.com/file/d/1wkesS2F_0U0m1K3RxaZood4mVLbymh6d/view?usp=sharing) |
| `Ellie_connected_v2/` | A more robust version with resting animation, OpenCV movement detection, hand gesture mode selection, and a hand-controlled Brick Pong. It relaunches when no movement is detected. | [▶️ Watch Demo](https://drive.google.com/file/d/14VgP01R4UeSrjxccz6_b1pInGMkk3tBn/view?usp=sharing) |
| `flaskServerWith3DEffects/` | YOLOv9 object detection integrated to create video effects and animations. | [▶️ Watch Demo](https://vimeo.com/929837304/6112b0460f?share=copy) |
| `soundAndPersonRecognition/` | Scripts for detecting sound levels and recognizing persons using a simple OpenCV model. | *No demo available* |

## 🛠️ Technologies Used

This project utilizes a variety of technologies to bring the interactive experience to life:

<p align="center">
  <a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/></a>
  <a href="https://isocpp.org/" target="_blank"><img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c-plus-plus&logoColor=white" alt="C++"/></a>
  <a href="https://opencv.org/" target="_blank"><img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/></a>
  <a href="https://developers.google.com/mediapipe" target="_blank"><img src="https://img.shields.io/badge/MediaPipe-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="MediaPipe"/></a>
  <a href="https://www.pygame.org/" target="_blank"><img src="https://img.shields.io/badge/PyGame-1E6F5C?style=for-the-badge&logo=pygame&logoColor=white" alt="PyGame"/></a>
  <a href="https://numpy.org/" target="_blank"><img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/></a>
  <a href="https://matplotlib.org/" target="_blank"><img src="https://img.shields.io/badge/Matplotlib-3175A2?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib"/></a>
  <a href="https://developer.nvidia.com/embedded/jetson-nano-developer-kit" target="_blank"><img src="https://img.shields.io/badge/Jetson_Nano-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="Jetson Nano"/></a>
</p>

**Core Models & Libraries:**
- **YOLOv9**: For state-of-the-art object detection.
- **MobileNet**: For efficient on-device user recognition.
- **whisper**: For speech-to-text capabilities.

---
*Feel free to explore the folders and dive into the code!*


