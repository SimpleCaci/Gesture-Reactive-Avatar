import cv2
import mediapipe as mp
import face_landmarks #for easier view of the ID

mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

#FaceMesh Landmark IDing
UpperLipLandmarkId = 13


with mp_face.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face:

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face.process(rgb)

        if result.multi_face_landmarks:
            for lm in result.multi_face_landmarks:
                
                #draw all landmarks
                '''
                mp_draw.draw_landmarks(
                    frame,
                    lm,
                    mp_face.FACEMESH_TESSELATION
                )
                '''
                for group in [face_landmarks.LeftEyeLandmarks, face_landmarks.RightEyeLandmarks]:
                    for index in group:
                        x = int(lm.landmark[index].x * frame.shape[1])
                        y = int(lm.landmark[index].y * frame.shape[0])
                        cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        cv2.imshow("FaceMesh", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
