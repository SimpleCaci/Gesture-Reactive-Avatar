from pathlib import Path

import cv2
import mediapipe as mp

from calibration import Calibration
from face_animator import ExpressionSmoother, FaceAnimator
import face_landmarks as fl
from face_state import get_face_state
from face_state_to_image import ExpressionRules
from show_avatar import show_avatar

WINDOW_PREVIEW = "Camera & controls"
WINDOW_AVATAR = "Avatar"
EXPRESSION_LABELS = {
    "catLeftWink": "Left wink",
    "catRightWink": "Right wink",
    "mmCry": "Crying",
    "catLaugh": "Laughing",
    "catSmirk": "Smirking",
    "catSad": "Sad",
    "catStareCute": "Curious",
    "catStare": "Neutral",
}


def draw_hud(frame, calibration, expression, face_found):
    """Draw a compact calibration and expression control panel."""
    overlay = frame.copy()
    cv2.rectangle(overlay, (16, 16), (430, 128), (25, 22, 34), -1)
    cv2.addWeighted(overlay, 0.82, frame, 0.18, 0, frame)

    if not face_found:
        status = "Find a face to begin"
        accent = (120, 170, 255)
    elif not calibration.ready:
        percent = round(calibration.progress * 100)
        status = f"Calibrating neutral face · {percent}%"
        accent = (130, 210, 255)
        bar_width = int(380 * calibration.progress)
        cv2.rectangle(frame, (32, 74), (412, 88), (74, 69, 86), -1)
        cv2.rectangle(frame, (32, 74), (32 + bar_width, 88), accent, -1)
    else:
        status = f"Expression · {expression}"
        accent = (124, 235, 166)

    cv2.putText(
        frame,
        status,
        (32, 50),
        cv2.FONT_HERSHEY_DUPLEX,
        0.65,
        accent,
        1,
        cv2.LINE_AA,
    )
    cv2.putText(
        frame,
        "R recalibrate   V clean avatar view   Esc quit",
        (32, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.48,
        (230, 226, 235),
        1,
        cv2.LINE_AA,
    )


def close_preview_window():
    try:
        cv2.destroyWindow(WINDOW_PREVIEW)
    except cv2.error:
        pass


def main():
    mp_face = mp.solutions.face_mesh
    mp_draw = mp.solutions.drawing_utils

    calibration = Calibration()
    animator = FaceAnimator(image_folder="images", rules=ExpressionRules)
    smoother = ExpressionSmoother(hold_time=0.06)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not open camera 0. Check camera access and device availability.")
        return 1

    preview_visible = True
    expression = "Neutral"
    last_announced_expression = None

    try:
        with mp_face.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        ) as face:
            while True:
                ok, frame = cap.read()
                if not ok:
                    print("Camera stopped returning frames.")
                    break

                result = face.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                face_found = bool(result.multi_face_landmarks)

                if face_found:
                    landmarks = result.multi_face_landmarks[0]
                    mp_draw.draw_landmarks(
                        frame,
                        landmarks,
                        mp_face.FACEMESH_TESSELATION,
                    )
                    lm_list = landmarks.landmark
                    calibration.add_sample(lm_list, fl)

                    state = {}
                    if calibration.ready:
                        state = smoother.smooth(
                            get_face_state(lm_list, fl, calibration.baseline)
                        )

                    current_image_path = animator.select_image(state)
                    if current_image_path:
                        expression = EXPRESSION_LABELS.get(
                            Path(current_image_path).stem,
                            Path(current_image_path).stem,
                        )
                        avatar_img = show_avatar(current_image_path)
                        if avatar_img is not None:
                            cv2.imshow(WINDOW_AVATAR, avatar_img)

                    if calibration.ready and expression != last_announced_expression:
                        print(f"Expression: {expression}")
                        last_announced_expression = expression

                    for group in [
                        fl.LeftEyeLandmarks,
                        fl.RightEyeLandmarks,
                        [
                            fl.MouthUpperInnerLandmarkId,
                            fl.MouthLowerInnerLandmarkId,
                        ],
                    ]:
                        for index in group:
                            x = int(lm_list[index].x * frame.shape[1])
                            y = int(lm_list[index].y * frame.shape[0])
                            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

                draw_hud(frame, calibration, expression, face_found)
                if preview_visible:
                    cv2.imshow(WINDOW_PREVIEW, frame)

                key = cv2.waitKey(1) & 0xFF
                if key == 27:
                    break
                if key in (ord("r"), ord("R")):
                    calibration.reset()
                    smoother.reset()
                    expression = "Neutral"
                    last_announced_expression = None
                    print("Calibration restarted. Hold a neutral expression.")
                if key in (ord("v"), ord("V")):
                    preview_visible = not preview_visible
                    if not preview_visible:
                        close_preview_window()
                        print("Clean avatar view enabled.")
                    else:
                        print("Camera and controls view enabled.")
    finally:
        cap.release()
        cv2.destroyAllWindows()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
