# 👁️ Vision to Hardware

A collection of small projects that connect computer vision with physical hardware.
These projects use a laptop camera to detect hand gestures and movements with Python and MediaPipe, then communicate the results to an ESP32 over Serial to control different electronic components.
The goal is to explore how computer vision can be turned into real-world hardware interaction.

## ❓ How It Works

The basic architecture behind these projects is:

Camera → Computer Vision → Python → Serial → ESP32 → Hardware

Python handles the image processing and hand tracking, while the ESP32 handles the hardware and real-time control.

## 🛠️ Technologies

- Python
- OpenCV
- MediaPipe
- PySerial
- ESP32
- Arduino IDE
- PWM
- Serial Communication
- Multiplexing

## 📂 Projects

### 01 — Hand Controlled LEDs 💡

Control a row of LEDs using the number of fingers detected by the camera. Each finger corresponds to one LED.

---

### 02 — Hand Controlled LED Brightness 🔆

Control the brightness of an LED using the distance between the thumb and index finger. The distance between the two landmarks is mapped to a PWM value from `0` to `255`.

---

### 03 — Two-Hand 7-Segment 🔢

Count the fingers on both hands, add them together, and display the result on a 4-digit 7-segment display. For example:
- Left hand:  ✌️  → 2
- Right hand: 🖐️  → 5
then 2 + 5 = 7
The project can also display 10 using two digits.

---
Each project contains its own code, hardware information, and documentation. Demos GIFs are included inside each project folder.

### ⚠️ Notes
1) Most projects use a laptop camera for computer vision and an ESP32 for hardware control.
2) A MediaPipe model file may be required for the hand tracking projects. 
3) Run the `download.py` code to get the model in your working directory!
