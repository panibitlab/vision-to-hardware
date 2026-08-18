#Use this code to download the model :)

import requests

url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"

response = requests.get(url)

if response.status_code == 200:
    with open("hand_landmarker.task", "wb") as f:
        f.write(response.content)

    print("Model downloaded successfully!")
else:
    print("Download failed:", response.status_code)
