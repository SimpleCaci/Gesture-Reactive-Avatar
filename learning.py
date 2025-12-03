#learning.py
#to learn each part of the base code

# -- library importations --
import cv2 #OpenCV for webcam, images, drawing, and windows (like displaying)
import mediapipe as mp #Googl'e ML tracking library for facial landmarks

mp_draw = mp.solutions.drawing_utils
mp_face = mp.solutions.face_mesh

cap = cv2.VideoCapture(0)

with mp_face.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb)

        if result.multi_face_landmarks:
            for face_landmarks in result.multi_face_landmarks:
                mp_draw.draw_landmarks(
                    frame,
                    face_landmarks,
                    mp_face.FACEMESH_TESSELATION
                )

        cv2.imshow("Face Tracking", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
