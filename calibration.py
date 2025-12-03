class Calibration:
    def __init__(self):
        self.samples = []
        self.ready = False
        self.baseline = {}

    def add_sample(self, lm_list, FL):
        if self.ready: return

        # Collect ~60 samples (2 seconds at 30FPS)
        self.samples.append({
            "mouth_open": abs(lm_list[FL.UpperInnerLipLandmarkId].y -
                              lm_list[FL.LowerInnerLipLandmarkId].y),

            "mouth_width": abs(lm_list[FL.MouthRightCornerLandmarkId].x -
                               lm_list[FL.MouthLeftCornerLandmarkId].x),

            "left_eye": abs(lm_list[FL.LeftEyeUpperLidLandmarkId].y -
                            lm_list[FL.LeftEyeLowerLidLandmarkId].y),

            "right_eye": abs(lm_list[FL.RightEyeUpperLidLandmarkId].y -
                             lm_list[FL.RightEyeLowerLidLandmarkId].y),

            "left_brow_dist": (lm_list[FL.LeftEyebrowInnerLandmarkId].y -
                               lm_list[FL.LeftEyeUpperLidLandmarkId].y),

            "right_brow_dist": (lm_list[FL.RightEyebrowInnerLandmarkId].y -
                                lm_list[FL.RightEyeUpperLidLandmarkId].y)
        })

        if len(self.samples) >= 60:
            self.ready = True
            # Compute baselines (mean values)
            self.baseline = {
                key: sum(s[key] for s in self.samples) / len(self.samples)
                for key in self.samples[0]
            }
            print("Calibration complete!")
