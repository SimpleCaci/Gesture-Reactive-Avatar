def get_face_state(lm_list, FL, base):

    # ----- MOUTH OPEN -----
    mouth_open = abs(
        lm_list[FL.UpperInnerLipLandmarkId].y -
        lm_list[FL.LowerInnerLipLandmarkId].y
    )
    isMouthOpen = mouth_open > base["mouth_open"] * 1.8

    # ----- SMILE -----
    mouth_width = abs(
        lm_list[FL.MouthRightCornerLandmarkId].x -
        lm_list[FL.MouthLeftCornerLandmarkId].x
    )
    isSmiling = mouth_width > base["mouth_width"] * 1.25

    # ----- O-MOUTH (small width + open) -----
    isOMouth = (mouth_open > base["mouth_open"] * 2.0) and \
               (mouth_width < base["mouth_width"] * 0.95)

    # ----- BLINKS -----
    left_eye = abs(
        lm_list[FL.LeftEyeUpperLidLandmarkId].y -
        lm_list[FL.LeftEyeLowerLidLandmarkId].y
    )
    right_eye = abs(
        lm_list[FL.RightEyeUpperLidLandmarkId].y -
        lm_list[FL.RightEyeLowerLidLandmarkId].y
    )

    isLeftBlink = left_eye < base["left_eye"] * 0.45
    isRightBlink = right_eye < base["right_eye"] * 0.45
    isBlink = isLeftBlink and isRightBlink
    isLeftWink = isLeftBlink and not isRightBlink
    isRightWink = isRightBlink and not isLeftBlink

    # ----- EYEBROWS -----
    left_brow_dist = (lm_list[FL.LeftEyebrowInnerLandmarkId].y -
                      lm_list[FL.LeftEyeUpperLidLandmarkId].y)
    right_brow_dist = (lm_list[FL.RightEyebrowInnerLandmarkId].y -
                       lm_list[FL.RightEyeUpperLidLandmarkId].y)

    isEyebrowRaised = (left_brow_dist < base["left_brow_dist"] * 0.85) and \
                      (right_brow_dist < base["right_brow_dist"] * 0.85)

    isEyebrowLowered = (left_brow_dist > base["left_brow_dist"] * 1.15) and \
                       (right_brow_dist > base["right_brow_dist"] * 1.15)

    # ----- FROWN -------
    upper_lip = lm_list[FL.UpperLipLandmarkId].y
    left_corner = lm_list[FL.MouthLeftCornerLandmarkId].y
    right_corner = lm_list[FL.MouthRightCornerLandmarkId].y
    isFrowning = (left_corner < upper_lip - 0.008) and \
                 (right_corner < upper_lip - 0.008)

    # ----- SURPRISED -----
    isSurprised = (left_eye > base["left_eye"] * 1.25 and
                   right_eye > base["right_eye"] * 1.25) and isMouthOpen

    # (tilt & turn unchanged)

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

        "surprised": isSurprised
    }
