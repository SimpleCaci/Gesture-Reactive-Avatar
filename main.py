import cv2
import mediapipe as mp

mp_selfie = mp.solutions.selfie_segmentation

cap = cv2.VideoCapture(0)

with mp_selfie.SelfieSegmentation(model_selection=1) as selfie_seg:
    while True:
        _, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = selfie_seg.process(rgb)
        
        mask = result.segmentation_mask > 0.5  # person vs background
        frame[~mask] = (0, 255, 0)  # make background green

        cv2.imshow("Segmentation", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
