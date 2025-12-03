#learning.py
#to learn each part of the base code

# -- library importations --
import cv2 #OpenCV for webcam, images, drawing, and windows (like displaying)
import mediapipe as mp #Googl'e ML tracking library for facial landmarks

mp_draw = mp.solutions.drawing_utils # for processing how to draw the landmarkswhat
mp_face = mp.solutions.face_mesh # to produce all the 486 landmarks on your face


#mp.soltuions contain --
'''
Drawing+Styling Tools:
-drawing_utils
-drawing_styles

Face:
-face_mesh
    (full 468 point landmark tracking)
-face_detection
    (simple bounding box detection)
-iris 
    (eye tracking for fine-grain iris position)

Hand:
-hands
    (21 landparks per hand)

Body/Pose:
-pose:
    (33 body landmarks - for full skeleton)
-holisitic:
    (face + hands + pose, synchronized)

Hair + Style Transfer:
-selfie_segmentation
    (removes background)  
-hair_segmentation
    (hair masking)
-objectron:
    (object detection like for shoes or cups or cameras)

Image/Video Processing
    image_segmentation
    image_classifier
    image_embedder
    image_segmenter
    gesture_recognizer
    hand_gesture

others:
    vision
    audio
    text
'''

cap = cv2.VideoCapture(0) #for video capturing (starts camera) 0 = default camera
#cap.read gives you the frame

with mp_face.FaceMesh(
    max_num_faces=1, #how many face you track
    refine_landmarks=True, #Enables iris tracking and sharper face landmarks
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5
) as face_mesh:

    while True:
        ret, frame = cap.read() #ret tests if the capture is successful 
                                #frame is the actual capture
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #conversion to rgb since OpenCV use BGR while MediaPipe use RGB


        result = face_mesh.process(rgb)
        #runs the face tracking
        #if there's a face, return the 468 3d landmarks
        #if no face, then return none 

        if result.multi_face_landmarks: #if there is landmarks, draw it
            for face_landmarks in result.multi_face_landmarks:
                mp_draw.draw_landmarks( 
                    frame,
                    face_landmarks,
                    mp_face.FACEMESH_TESSELATION
                )

        cv2.imshow("Face Tracking", frame) #show it in a window
        if cv2.waitKey(1) & 0xFF == 27: #close on esc key
            break
#with... as... (cleans up the item afterward)

cap.release() #releases the camera
cv2.destroyAllWindows() #destroys the cv2 capturing 

