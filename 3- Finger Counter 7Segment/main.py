import cv2
import mediapipe as mp
import serial
import time

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# serial with esp32
esp32 = serial.Serial(port='COM7', baudrate=9600, timeout=1)
time.sleep(2)

# mediaPipe
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)


def detect_fingers(hand_landmarks, handedness):
    finger_tips = [8, 12, 16, 20]
    finger_states = [0, 0, 0, 0, 0]

    # Thumb
    if handedness == "Right":
        if hand_landmarks[4].x > hand_landmarks[3].x:
            finger_states[0] = 1

    else:
        if hand_landmarks[4].x < hand_landmarks[3].x:
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

    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)
    result = detector.detect(mp_image)

    total_fingers = 0
    if result.hand_landmarks:
        for hand_landmarks, handedness in zip(result.hand_landmarks, result.handedness):

            handedness_label = handedness[0].category_name
            fingers_state = detect_fingers(hand_landmarks, handedness_label)

            fingers_count = sum(fingers_state)
            total_fingers += fingers_count

            # Draw landmarks
            for landmark in hand_landmarks:
                x = int(landmark.x * image.shape[1])
                y = int(landmark.y * image.shape[0])

                cv2.line(image, (x - 5, y), (x + 5, y), (250, 5, 152), 1)
                cv2.line(image, (x, y - 5), (x, y + 5), (250, 5, 152), 1)

    esp32.write(bytes([total_fingers]))

    cv2.imshow('Two Hand Counter', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()

esp32.close()
detector.close()
