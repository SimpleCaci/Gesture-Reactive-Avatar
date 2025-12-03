def get_face_state(lm_list, FL):
    # --------------------------------------
    # MOUTH OPEN
    # --------------------------------------
    upper_lip = lm_list[FL.UpperInnerLipLandmarkId].y
    lower_lip = lm_list[FL.LowerInnerLipLandmarkId].y
    mouth_open_value = abs(lower_lip - upper_lip)
    isMouthOpen = mouth_open_value > 0.03

    # --------------------------------------
    # SMILE
    # --------------------------------------
    mouth_width = abs(
        lm_list[FL.MouthRightCornerLandmarkId].x -
        lm_list[FL.MouthLeftCornerLandmarkId].x
    )
    isSmiling = mouth_width > 0.22

    # --------------------------------------
    # O-MOUTH
    # --------------------------------------
    isOMouth = (mouth_open_value > 0.04) and (mouth_width < 0.18)

    # --------------------------------------
    # FROWN
    # --------------------------------------
    left_corner_y = lm_list[FL.MouthLeftCornerLandmarkId].y
    right_corner_y = lm_list[FL.MouthRightCornerLandmarkId].y
    upper_lip_y = lm_list[FL.UpperLipLandmarkId].y

    isFrowning = (left_corner_y < upper_lip_y - 0.01) and \
                 (right_corner_y < upper_lip_y - 0.01)

    # --------------------------------------
    # BLINKS
    # --------------------------------------
    left_eye_open = abs(
        lm_list[FL.LeftEyeUpperLidLandmarkId].y -
        lm_list[FL.LeftEyeLowerLidLandmarkId].y
    )
    right_eye_open = abs(
        lm_list[FL.RightEyeUpperLidLandmarkId].y -
        lm_list[FL.RightEyeLowerLidLandmarkId].y
    )

    isLeftBlink = left_eye_open < 0.011
    isRightBlink = right_eye_open < 0.011
    isBlink = isLeftBlink and isRightBlink
    isLeftWink = isLeftBlink and not isRightBlink
    isRightWink = isRightBlink and not isLeftBlink

    # --------------------------------------
    # EYEBROWS
    # --------------------------------------
    left_brow = lm_list[FL.LeftEyebrowInnerLandmarkId].y
    left_eye_top = lm_list[FL.LeftEyeUpperLidLandmarkId].y
    right_brow = lm_list[FL.RightEyebrowInnerLandmarkId].y
    right_eye_top = lm_list[FL.RightEyeUpperLidLandmarkId].y

    isLeftEyebrowRaised = (left_brow - left_eye_top) < -0.03
    isRightEyebrowRaised = (right_brow - right_eye_top) < -0.03
    isEyebrowRaised = isLeftEyebrowRaised and isRightEyebrowRaised

    isEyebrowLowered = (left_brow - left_eye_top) > -0.015 and \
                       (right_brow - right_eye_top) > -0.015

    # --------------------------------------
    # SURPRISED
    # --------------------------------------
    isSurprised = (left_eye_open > 0.018 and right_eye_open > 0.018) and isMouthOpen

    # --------------------------------------
    # HEAD TILT
    # --------------------------------------
    left_cheek = lm_list[FL.LeftCheekLandmarkId].y
    right_cheek = lm_list[FL.RightCheekLandmarkId].y
    tilt_value = right_cheek - left_cheek

    isHeadTiltRight = tilt_value > 0.02
    isHeadTiltLeft  = tilt_value < -0.02

    # --------------------------------------
    # HEAD TURN
    # --------------------------------------
    left_face_side = lm_list[FL.LeftFaceSideLandmarkId].x
    right_face_side = lm_list[FL.RightFaceSideLandmarkId].x

    isHeadTurnRight = right_face_side < 0.35
    isHeadTurnLeft  = left_face_side > 0.65

    # --------------------------------------
    # RETURN A SINGLE STATE OBJECT
    # --------------------------------------
    return {
        "mouth_open": isMouthOpen,
        "smile": isSmiling,
        "o_mouth": isOMouth,
        "frown": isFrowning,

        "left_blink": isLeftBlink,
        "right_blink": isRightBlink,
        "blink": isBlink,
        "left_wink": isLeftWink,
        "right_wink": isRightWink,

        "eyebrow_raised": isEyebrowRaised,
        "eyebrow_lowered": isEyebrowLowered,

        "head_tilt_left": isHeadTiltLeft,
        "head_tilt_right": isHeadTiltRight,
        "head_turn_left": isHeadTurnLeft,
        "head_turn_right": isHeadTurnRight,

        "surprised": isSurprised
    }
