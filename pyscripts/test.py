import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

try:
    result = DeepFace.analyze(
        img_path=rgb_frame,
        actions=['emotion'],
        enforce_detection=False,
        silent=True,
        detector_backend = "retinaface"
    )
    dominant_emotion = result[0]['dominant_emotion']
    print(dominant_emotion, end='')
except Exception as e:
    emotion_text = f"Error: {e}"
    

cap.release()
cv2.destroyAllWindows()
    
