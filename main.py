import math
import cv2
import mediapipe as mp
import face_landmarks as fl #for easier view of the ID
from face_state import get_face_state #to process the state of the face
from face_animator import FaceAnimator, ExpressionSmoother
from face_state_to_image import ExpressionRules
from face_box import get_face_box
from show_avatar import show_avatar

mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

animator = FaceAnimator(
    image_folder="images",
    rules=ExpressionRules
)

smoother = ExpressionSmoother(hold_time=0.06)

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
            for lm in result.multi_face_landmarks: #for multiple faces
                
                #draw all landmarks
                '''
                mp_draw.draw_landmarks(
                    frame,
                    lm,
                    mp_face.FACEMESH_TESSELATION
                )
                '''
                lm_list = lm.landmark

                rawFaceState = get_face_state(lm_list, fl)
                stableFaceState = smoother.smooth(rawFaceState)

                current_image_path = animator.select_image(stableFaceState)

                avatar_img = show_avatar(current_image_path)
                if avatar_img is not None:
                    cv2.imshow("Avatar", avatar_img)

                for group in [fl.LeftEyeLandmarks, fl.RightEyeLandmarks, [fl.MouthUpperInnerLandmarkId, fl.MouthLowerInnerLandmarkId]]:
                    for index in group:
                        x = int(lm_list[index].x * frame.shape[1])
                        y = int(lm_list[index].y * frame.shape[0])
                        cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
                

        cv2.imshow("FaceMesh", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
