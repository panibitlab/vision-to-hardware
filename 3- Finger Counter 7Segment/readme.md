# 🔢 Two-Hand 7-Segment

<p align="center">
  A computer vision project that counts the fingers on both hands, adds them together,
  and displays the result on a 4-digit 7-segment display.
</p>

## ❓ How It Works

Camera
   ↓
MediaPipe
   ↓
Two-Hand Detection
   ↓
Finger Counting
   ↓
Addition
   ↓
Serial
   ↓
ESP32
   ↓
7-Segment Display

For example if you hold your hands like:
- Left hand:  ✌️ → 2
- Right hand: 🖐️ → 5
The result (2 + 5 = 7) is then displayed on the 7-segment display.

## 🔢 Multi-Hand Detection

MediaPipe is configured to detect up to two hands. Each hand is processed separately:
- Hand 1 → Finger Count
- Hand 2 → Finger Count
          ↓
        Addition
          ↓
        Result

The project also uses MediaPipe's handedness information to correctly detect the thumb on both the left and right hands.

## 🔌 Display 

The project uses multiplexing to control multiple digits of the 7-segment display.
Only one digit is activated at a time, while the digits are refreshed rapidly enough to appear continuously lit.
The display is controlled using non-blocking timing with millis().

## 🛠️ Hardware

- ESP32
- 4 digit seven segment
- Laptop camera

## 💻 Python Libraries
OpenCV (to control camera) 
MediaPipe (handmarker model)
PySerial (for communicating with esp32)

## 📼 Demo

<p align="center">
  <img src="demo.gif" width="50%">
</p>

p.s. credit to my brother for participating in demo video. :)

## 💻 Source Code
> PYTHON `main.py`
> Microcontroller `esp32/main.ino`
