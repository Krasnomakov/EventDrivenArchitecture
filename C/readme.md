# 🚀 C/C++ for Jetson Nano

A collection of C/C++ programs for the Jetson Nano, focusing on animations, gesture control, and gaming for an 8-bit LED screen.

<p align="center">
  <a href="https://drive.google.com/file/d/1IVOBHTk2JU5LjdZWM55VMYE9VPgmm1oh/view?usp=sharing"><img src="https://img.shields.io/badge/Demo-Event--Driven_Architecture-4285F4?style=for-the-badge&logo=google-drive&logoColor=white" alt="Event-Driven Architecture Demo"/></a>
  <a href="https://drive.google.com/file/d/15immDvVE9rzHjOSAga4jwyM3pBoCWAVq/view?usp=sharing"><img src="https://img.shields.io/badge/Demo-Brick_Pong-4285F4?style=for-the-badge&logo=google-drive&logoColor=white" alt="Brick Pong Demo"/></a>
  <a href="https://drive.google.com/file/d/13E9lRFCfXW6GLsjpQeqEjfcrZtrPX8RK/view?usp=sharing"><img src="https://img.shields.io/badge/Demo-Snake-4285F4?style=for-the-badge&logo=google-drive&logoColor=white" alt="Snake Demo"/></a>
</p>

## ✨ Overview

This folder contains various C/C++ programs developed for the Jetson Nano. These programs control animations, detect movement, recognize poses and hands, and implement simple games like Snake and Brick Pong. The code is optimized for performance on the embedded platform.

## 📂 Folder Contents

-   `basics/`: Beginner-level examples with C/C++.
-   `eventDriven/`: Implementation of a simple event-driven architecture using named pipes for inter-process communication and user presence/movement recognition.
-   `openCVexamples/`: Examples of projecting video to a pixel wall, featuring animation effects and CUDA utilization for acceleration.
-   `posenet/`: C++ implementation of games with AI-powered hand recognition for controls.
-   `wrapper/`: An implementation of a C++ wrapper designed to interact with a Rust library.

## 🛠️ Technologies & Requirements

These projects are designed to run on a specific hardware and software setup.

**Hardware:**
-   **NVIDIA Jetson Nano**

**Software:**
-   **Ubuntu 18.04**
-   **SDL2**: For graphics and input.
-   **OpenCV**: For computer vision tasks.
-   *Additional libraries may be specified in each subfolder's README or source code.*

<p align="center">
  <a href="https://isocpp.org/" target="_blank"><img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c-plus-plus&logoColor=white" alt="C++"/></a>
  <a href="https://developer.nvidia.com/embedded/jetson-nano-developer-kit" target="_blank"><img src="https://img.shields.io/badge/Jetson_Nano-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="Jetson Nano"/></a>
  <a href="https://ubuntu.com/" target="_blank"><img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Ubuntu"/></a>
  <a href="https://www.libsdl.org/" target="_blank"><img src="https://img.shields.io/badge/SDL2-1B2C3D?style=for-the-badge&logo=sdl&logoColor=white" alt="SDL2"/></a>
  <a href="https://opencv.org/" target="_blank"><img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/></a>
</p>
