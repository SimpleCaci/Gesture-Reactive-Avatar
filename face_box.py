def get_face_box(lm_list, frame):
    # Nose = center reference
    nose = lm_list[1]

    # Face width: distance between cheeks
    left_cheek = lm_list[234]
    right_cheek = lm_list[454]

    # Face height: chin to eyebrows
    chin = lm_list[152]
    eyebrow = lm_list[168]

    h, w = frame.shape[:2]

    nose_x = int(nose.x * w)
    nose_y = int(nose.y * h)

    face_width = int(abs(left_cheek.x - right_cheek.x) * w)
    face_height = int(abs(chin.y - eyebrow.y) * h)

    return nose_x, nose_y, face_width, face_height
