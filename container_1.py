import cv2
import requests

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Dummy example: just send every 10th frame
    resized = cv2.resize(frame, (320, 240))
    _, img_encoded = cv2.imencode('.jpg', resized)
    requests.post("http://web:8080/upload", files={"image": img_encoded.tobytes()})
