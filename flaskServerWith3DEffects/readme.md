# 🚀 Flask Server with 3D Effects

An implementation of a simple AI event-driven architecture with a Flask server to create real-time video effects based on object detection.

<p align="center">
  <a href="https://vimeo.com/929837304/6112b0460f?share=copy">
    <img src="https://img.shields.io/badge/Watch-Demo-181717?style=for-the-badge&logo=vimeo&logoColor=00ADEF" alt="Demo"/>
  </a>
</p>

## ✨ Features

- **Event-Driven Architecture**: Uses a Flask server to handle events triggered by an AI model.
- **Object Detection**: Leverages the YOLOv9 (GELAN) model to detect objects like cell phones and bottles in real-time.
- **Dynamic Video Effects**:
  - **Pixelation**: Changes the pixel size of the video output when a cell phone is detected.
  - **Wave Effect**: Applies a wave effect to the video when a bottle is detected.
- **Real-time Simulation**: Includes an optional browser-based simulation to visualize the output on a 20x20 pixelated array, mimicking an LED screen.

## 🛠️ How to Run

Follow these steps to get the project running. You will need multiple terminal sessions.

### Terminal 1: Object Detection

1.  Navigate to the YOLOv9 directory:
    ```bash
    cd yolov9-main
    ```

2.  Run the detection script. This will start capturing from your camera (`source 0`) and log the output to `output.txt`.
    ```bash
    python3.11 detect.py --weights gelan-c.pt --conf 0.5 --source 0 --device cpu &> ../output.txt
    ```

### Terminal 2: Event Listener

1.  From the `flaskServerWith3DEffects` root, run the event trigger script:
    ```bash
    python3.11 eventTrigArch2.py
    ```

### Terminal 3: Flask Application

1.  From the `flaskServerWith3DEffects` root, run the Flask app:
    ```bash
    python3.11 app.py
    ```

### Terminal 4: (Optional) Simulation

1.  To view the output on a simulated 20x20 LED grid in your browser, run the simulation script:
    ```bash
    python3.11 simulation.py
    ```

## 💻 Technologies Used

<p align="center">
  <a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/></a>
  <a href="https://flask.palletsprojects.com/" target="_blank"><img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/></a>
</p>

**Core Model:**
- **YOLOv9 (GELAN)**: For real-time object detection.

