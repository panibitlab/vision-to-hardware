# 🔆 Hand Controlled LED Brightness

<p align="center">
   control LED brightness using the distance between the thumb and index finger.
</p>

## ✨ Overview
A computer vision project but Instead of simply detecting whether a finger is open or closed, this project uses the actual position of MediaPipe landmarks.

## ❓ How It Works

Camera
   ↓
MediaPipe
   ↓
Thumb + Index Landmarks
   ↓
Distance Calculation
   ↓
Mapping
   ↓
PWM Value
   ↓
Serial
   ↓
ESP32
   ↓
LED Brightness

The distance between the thumb tip and index finger tip is mapped to a PWM value between 0 and 255. like this:
👌  →  Low brightness
🤚  →  High brightness

## 🛠️ Hardware

- ESP32
- a LED
- Current-limiting resistor (i've used 330Ω one)
- Laptop camera
  
## 💻 Python Libraries

OpenCV (to control camera) 
MediaPipe (handmarker model)
PySerial (for communicating with esp32)

## 📐 Main Concept

The distance between two landmarks is calculated using their pixel coordinates. The resulting value is then mapped to:
0 → 255
where: 
- 0   → LED OFF
- 255 → Maximum brightness

## 💻 Source Code

> PYTHON `main.py`
> Microcontroller `esp32/main.ino`
