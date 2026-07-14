import unittest

from calibration import Calibration
from face_animator import ExpressionSmoother


class FakeLandmarks:
    UpperInnerLipLandmarkId = 0
    LowerInnerLipLandmarkId = 1
    MouthRightCornerLandmarkId = 2
    MouthLeftCornerLandmarkId = 3
    LeftEyeUpperLidLandmarkId = 4
    LeftEyeLowerLidLandmarkId = 5
    RightEyeUpperLidLandmarkId = 6
    RightEyeLowerLidLandmarkId = 7
    LeftEyebrowInnerLandmarkId = 8
    RightEyebrowInnerLandmarkId = 9


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def sample_landmarks():
    return [
        Point(0.5, 0.40),
        Point(0.5, 0.45),
        Point(0.7, 0.5),
        Point(0.3, 0.5),
        Point(0.4, 0.30),
        Point(0.4, 0.34),
        Point(0.6, 0.30),
        Point(0.6, 0.34),
        Point(0.4, 0.24),
        Point(0.6, 0.24),
    ]


class CalibrationTests(unittest.TestCase):
    def test_progress_completion_and_reset(self):
        calibration = Calibration(sample_target=2)
        calibration.add_sample(sample_landmarks(), FakeLandmarks)

        self.assertEqual(calibration.progress, 0.5)
        self.assertFalse(calibration.ready)

        calibration.add_sample(sample_landmarks(), FakeLandmarks)

        self.assertTrue(calibration.ready)
        self.assertEqual(calibration.progress, 1.0)
        self.assertAlmostEqual(calibration.baseline["mouth_width"], 0.4)

        calibration.reset()

        self.assertEqual(calibration.progress, 0)
        self.assertFalse(calibration.ready)
        self.assertEqual(calibration.baseline, {})

    def test_rejects_empty_calibration(self):
        with self.assertRaises(ValueError):
            Calibration(sample_target=0)


class ExpressionSmootherTests(unittest.TestCase):
    def test_first_state_is_available_immediately(self):
        smoother = ExpressionSmoother(hold_time=0)
        neutral = {"smile": False}
        smile = {"smile": True}

        self.assertEqual(smoother.smooth(neutral), neutral)
        self.assertEqual(smoother.smooth(smile), smile)

        smoother.reset()
        self.assertIsNone(smoother.last_state)


if __name__ == "__main__":
    unittest.main()
