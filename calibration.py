class Calibration:
    """Collect a short neutral-expression baseline for one user."""

    def __init__(self, sample_target=60):
        if sample_target < 1:
            raise ValueError("sample_target must be at least 1")
        self.sample_target = sample_target
        self.reset()

    @property
    def progress(self):
        """Return calibration completion as a value between 0 and 1."""
        return min(len(self.samples) / self.sample_target, 1.0)

    def reset(self):
        """Discard the current baseline and begin calibration again."""
        self.samples = []
        self.ready = False
        self.baseline = {}

    def add_sample(self, lm_list, FL):
        if self.ready:
            return

        self.samples.append(
            {
                "mouth_open": abs(
                    lm_list[FL.UpperInnerLipLandmarkId].y
                    - lm_list[FL.LowerInnerLipLandmarkId].y
                ),
                "mouth_width": abs(
                    lm_list[FL.MouthRightCornerLandmarkId].x
                    - lm_list[FL.MouthLeftCornerLandmarkId].x
                ),
                "left_eye": abs(
                    lm_list[FL.LeftEyeUpperLidLandmarkId].y
                    - lm_list[FL.LeftEyeLowerLidLandmarkId].y
                ),
                "right_eye": abs(
                    lm_list[FL.RightEyeUpperLidLandmarkId].y
                    - lm_list[FL.RightEyeLowerLidLandmarkId].y
                ),
                "left_brow_dist": (
                    lm_list[FL.LeftEyebrowInnerLandmarkId].y
                    - lm_list[FL.LeftEyeUpperLidLandmarkId].y
                ),
                "right_brow_dist": (
                    lm_list[FL.RightEyebrowInnerLandmarkId].y
                    - lm_list[FL.RightEyeUpperLidLandmarkId].y
                ),
            }
        )

        if len(self.samples) >= self.sample_target:
            self.ready = True
            self.baseline = {
                key: sum(sample[key] for sample in self.samples) / len(self.samples)
                for key in self.samples[0]
            }
            print("Calibration complete!")
