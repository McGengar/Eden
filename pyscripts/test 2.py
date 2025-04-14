import cv2
from deepface import DeepFace
import time

cap = cv2.VideoCapture(0)

last_analysis_time = 0
analysis_interval = 5 

emotion_text = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    current_time = time.time()
    if current_time - last_analysis_time > analysis_interval:
        try:
            result = DeepFace.analyze(
                img_path=rgb_frame,
                actions=['emotion'],
                enforce_detection=False,
                silent=True,
                detector_backend = "retinaface"
            )
            dominant_emotion = result[0]['dominant_emotion']
            emotion_text = f"Emotion: {dominant_emotion}"
            print(dominant_emotion)
        except Exception as e:
            emotion_text = f"Błąd: {e}"
        
        last_analysis_time = current_time

    cv2.putText(frame, emotion_text, (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
