# 💡 Hand Controlled LEDs

<p align="center">
  A simple computer vision project that controls a row of LEDs using hand gestures.
</p>

## ✨ Overview
The laptop camera detects the hand using MediaPipe, counts the fingers, and sends their states to an ESP32 over Serial. Each finger controls one LED.

## ❓ How It Works

Camera 
   ↓
MediaPipe
   ↓
Hand Landmarks
   ↓
Finger Detection
   ↓
Python
   ↓
Serial
   ↓
ESP32
   ↓
LEDs

For example if you hold your hand like this ☝️, these information is going to be received:
Finger 1 → ON
Finger 2 → OFF
Finger 3 → OFF
Finger 4 → OFF
Finger 5 → OFF
so the first led in the row will turn on!

## 🛠️ Hardware

ESP32
5 × LEDs
5 × current-limiting resistors (i've used 330Ω ones)
Laptop camera

## 💻 Python Libraries
OpenCV (to control camera) 
MediaPipe (handmarker model)
PySerial (for communicating with esp32)

## 📡 Communication

Python sends five bytes to the ESP32. Each byte represents the state of one finger: 0 for "OFF" and 1 for "ON".
or example: 
[1, 1, 0, 0, 0] means that the first two LEDs are ON.


## 📼 Demo

<p align="center">
  <img src="demo.gif" width="50%">
</p>

## 💻 Source Code
> PYTHON `main.py`
> Microcontroller `esp32/main.ino`
