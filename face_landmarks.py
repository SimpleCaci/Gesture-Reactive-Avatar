# ============================================
#  FACE MESH LANDMARK REFERENCE
# ============================================

# ===== MOUTH LANDMARKS =====
UpperLipLandmarkId = 13
LowerLipLandmarkId = 14
MouthLeftCornerLandmarkId = 61
MouthRightCornerLandmarkId = 291

UpperInnerLipLandmarkId = 0
LowerInnerLipLandmarkId = 17

MouthUpperOuterLandmarkId = 37
MouthLowerOuterLandmarkId = 84
MouthUpperInnerLandmarkId = 13
MouthLowerInnerLandmarkId = 14

SmileLeftLandmarkId = 78
SmileRightLandmarkId = 308

# ===== LEFT EYE LANDMARKS =====
LeftEyeUpperLidLandmarkId = 159
LeftEyeLowerLidLandmarkId = 145

LeftEyeLeftCornerLandmarkId = 33
LeftEyeRightCornerLandmarkId = 133

LeftEyeUpperInnerLandmarkId = 158
LeftEyeLowerInnerLandmarkId = 153
LeftEyeUpperOuterLandmarkId = 160
LeftEyeLowerOuterLandmarkId = 144

# ===== RIGHT EYE LANDMARKS =====
RightEyeUpperLidLandmarkId = 386
RightEyeLowerLidLandmarkId = 374

RightEyeLeftCornerLandmarkId = 362
RightEyeRightCornerLandmarkId = 263

RightEyeUpperInnerLandmarkId = 385
RightEyeLowerInnerLandmarkId = 380
RightEyeUpperOuterLandmarkId = 387
RightEyeLowerOuterLandmarkId = 373

# ===== IRIS (GAZE TRACKING) =====
LeftIrisCenterLandmarkId = 468
LeftIrisRightLandmarkId = 469
LeftIrisLeftLandmarkId = 470
LeftIrisUpLandmarkId = 471
LeftIrisDownLandmarkId = 472

RightIrisCenterLandmarkId = 473
RightIrisRightLandmarkId = 474
RightIrisLeftLandmarkId = 475
RightIrisUpLandmarkId = 476
RightIrisDownLandmarkId = 477

# ===== EYEBROWS =====
LeftEyebrowInnerLandmarkId = 70
LeftEyebrowCenterLandmarkId = 105
LeftEyebrowOuterLandmarkId = 107

RightEyebrowInnerLandmarkId = 336
RightEyebrowCenterLandmarkId = 334
RightEyebrowOuterLandmarkId = 300

# ===== NOSE =====
NoseTipLandmarkId = 1
NoseBridgeTopLandmarkId = 168
NoseBridgeMiddleLandmarkId = 197
NoseLowerMidLandmarkId = 2

NoseLeftLandmarkId = 98
NoseRightLandmarkId = 327

# ===== CHEEKS (HEAD TILT / HEAD ROTATION) =====
LeftCheekLandmarkId = 234
RightCheekLandmarkId = 454

LeftFaceSideLandmarkId = 127
RightFaceSideLandmarkId = 356

# ===== FACE OUTLINE / JAWLINE =====
ChinLandmarkId = 152

JawlineLeftUpperId = 172
JawlineLeftLowerId = 136

JawlineRightUpperId = 397
JawlineRightLowerId = 365

JawlineCenterId = 152
JawlineUpperMidId = 9
JawlineLowerMidId = 200

# ===== FOREHEAD (APPROX REGION) =====
ForeheadLeftLandmarkId = 10
ForeheadCenterLandmarkId = 151
ForeheadRightLandmarkId = 338


# GROUPED LIST

MouthLandmarks = [
    UpperLipLandmarkId, LowerLipLandmarkId,
    MouthLeftCornerLandmarkId, MouthRightCornerLandmarkId,
    UpperInnerLipLandmarkId, LowerInnerLipLandmarkId,
    MouthUpperOuterLandmarkId, MouthLowerOuterLandmarkId,
    SmileLeftLandmarkId, SmileRightLandmarkId
]

LeftEyeLandmarks = [
    LeftEyeUpperLidLandmarkId, LeftEyeLowerLidLandmarkId,
    LeftEyeLeftCornerLandmarkId, LeftEyeRightCornerLandmarkId,
    LeftEyeUpperInnerLandmarkId, LeftEyeLowerInnerLandmarkId,
    LeftEyeUpperOuterLandmarkId, LeftEyeLowerOuterLandmarkId
]

RightEyeLandmarks = [
    RightEyeUpperLidLandmarkId, RightEyeLowerLidLandmarkId,
    RightEyeLeftCornerLandmarkId, RightEyeRightCornerLandmarkId,
    RightEyeUpperInnerLandmarkId, RightEyeLowerInnerLandmarkId,
    RightEyeUpperOuterLandmarkId, RightEyeLowerOuterLandmarkId
]

IrisLeftLandmarks = [
    LeftIrisCenterLandmarkId, LeftIrisRightLandmarkId,
    LeftIrisLeftLandmarkId, LeftIrisUpLandmarkId,
    LeftIrisDownLandmarkId
]

IrisRightLandmarks = [
    RightIrisCenterLandmarkId, RightIrisRightLandmarkId,
    RightIrisLeftLandmarkId, RightIrisUpLandmarkId,
    RightIrisDownLandmarkId
]

CheekLandmarks = [
    LeftCheekLandmarkId, RightCheekLandmarkId
]

JawlineLandmarks = [
    ChinLandmarkId, JawlineLeftUpperId, JawlineLeftLowerId,
    JawlineRightUpperId, JawlineRightLowerId,
    JawlineUpperMidId, JawlineLowerMidId
]

ForeheadLandmarks = [
    ForeheadLeftLandmarkId, ForeheadCenterLandmarkId, ForeheadRightLandmarkId
]
