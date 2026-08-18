import cv2
import mediapipe as mp
import serial
import time
import math

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# serial with esp32
esp32 = serial.Serial(port = 'COM7', baudrate = 9600, timeout = 1)
time.sleep(2)

# mediaPipe
base_options = python.BaseOptions(model_asset_path = 'hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options = base_options, num_hands = 1)
detector = vision.HandLandmarker.create_from_options(options)


# camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Mirror image
    image = cv2.flip(image, 1)
    # BGR → RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Convert to MediaPipe Image
    mp_image = mp.Image(image_format = mp.ImageFormat.SRGB, data = rgb_image)
    # Detect hand
    result = detector.detect(mp_image)

    if result.hand_landmarks:
        hand_landmarks = result.hand_landmarks[0]
        # Thumb tip = 4
        thumb = hand_landmarks[4]
        # Index finger tip = 8
        index = hand_landmarks[8]

        # Convert normalized coordinates to pixels
        thumb_x = int(thumb.x * image.shape[1])
        thumb_y = int(thumb.y * image.shape[0])

        index_x = int(index.x * image.shape[1])
        index_y = int(index.y * image.shape[0])

        # distance
        distance = math.sqrt((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2)
        # map to pwm
        brightness = int(max(0, min(255, (distance - 5) * 255 / 200)))

        esp32.write(bytes([brightness]))

        # Thumb
        cv2.circle(image,(thumb_x, thumb_y), 8, (0, 0, 255), -1)
        # Index
        cv2.circle(image, (index_x, index_y), 8, (0, 255, 0), -1)
        # Line between thumb and index
        cv2.line(image, (thumb_x, thumb_y), (index_x, index_y), (255, 0, 0), 3)

    # Show camera
    cv2.imshow('Hand LED Brightness Control', image)

    # press ESC ro close app
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

esp32.close()
detector.close()
