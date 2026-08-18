import cv2
import mediapipe as mp
import serial
import time

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# serial with esp32
eps32 = serial.Serial(port = 'COM7', baudrate = 9600, timeout = 1)
time.sleep(2)

# mediaPipe
base_options = python.BaseOptions(model_asset_path = 'hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options = base_options, num_hands = 1)
detector = vision.HandLandmarker.create_from_options(options)


# fingerDetection
def detect_fingers(hand_landmarks):
    finger_tips = [8, 12, 16, 20]
    thumb_tip = 4

    finger_states = [0, 0, 0, 0, 0]

    # Thumb
    if hand_landmarks[thumb_tip].x < hand_landmarks[thumb_tip - 1].x:
        finger_states[0] = 1
    # Other fingers
    for idx, tip in enumerate(finger_tips):
        if hand_landmarks[tip].y < hand_landmarks[tip - 2].y:
            finger_states[idx + 1] = 1
    return finger_states


# camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Mirror image
    image = cv2.flip(image, 1)
    # OpenCV BGR → RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Convert to MediaPipe Image
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)
    # Detect hand
    result = detector.detect(mp_image)

    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:
            # Detect fingers
            fingers_state = detect_fingers(hand_landmarks)
            # Send to ESP32
            eps32.write(bytes(fingers_state))
            print(f"Fingers State: {fingers_state}")
            # Draw landmarks
            for landmark in hand_landmarks:
                x = int(landmark.x * image.shape[1])
                y = int(landmark.y * image.shape[0])

                cv2.line(image, (x - 5, y), (x + 5, y), (250, 5, 152), 1)
                cv2.line(image, (x, y - 5), (x, y + 5), (250, 5, 152), 1)

    # Show camera
    cv2.imshow('Hand Control LEDs', image)

    # press ESC ro close app
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

eps32.close()
detector.close()
