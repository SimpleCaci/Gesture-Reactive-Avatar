# Gesture-Reactive Avatar

A local computer-vision avatar that reacts to facial expressions in real time.

The project uses a webcam and MediaPipe Face Mesh to classify expressions, smooth rapid changes, and select a matching cat reaction image. It is an early step toward a lightweight, non-pixel avatar for streaming, recording, and playful desktop interaction.

> **Status:** working prototype. The expression pipeline is implemented, but setup, calibration quality, and camera behavior still require validation across different faces, lighting, and devices.

## Capabilities

- captures a local webcam feed with OpenCV
- tracks one face with refined MediaPipe landmarks
- calibrates expression measurements to the current user with visible progress
- supports one-key recalibration when lighting or position changes
- recognizes eye, eyebrow, and mouth state combinations
- smooths rapid expression changes to reduce avatar flicker
- maps expression rules to a library of reaction images
- displays the landmark view and avatar in separate windows
- can hide the camera preview for a clean avatar-only capture window

## Technology

- Python
- OpenCV
- MediaPipe Face Mesh
- rule-based expression classification
- local image assets

## How it works

```text
webcam frame
    -> face landmarks
    -> personal calibration baseline
    -> expression measurements
    -> temporal smoothing
    -> reaction rule
    -> avatar image
```

Camera frames are processed locally and are not uploaded by this project.

## Setup

```bash
python -m venv .venv
```

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r dependencies.txt
```

macOS/Linux:

```bash
source .venv/bin/activate
python -m pip install -r dependencies.txt
```

A working webcam is required.

## Run

```bash
python main.py
```

Look toward the camera with a neutral expression while the on-screen calibration bar fills.

| Key | Action |
|---|---|
| **R** | Restart personal calibration |
| **V** | Toggle the camera/control preview for clean avatar capture |
| **Escape** | Close the application |

The avatar window intentionally stays free of debug overlays so it can be captured separately in OBS or recording software.

## Demo

The current reaction-image set is under `images/`. A privacy-safe screen recording showing calibration and several expression transitions is still needed.

## Validation status

Deterministic unit tests cover calibration progress/reset and initial expression smoothing. Camera-dependent behavior still requires a webcam: verify calibration completion, expression transitions, the clean capture toggle, Escape shutdown, and behavior when no face is visible.

## Known limitations

- thresholds are rule-based rather than learned from a diverse dataset
- camera selection is fixed to device 0
- the raw landmark window is intended for debugging
- reaction images have inconsistent source styles and dimensions
- accessibility and headless operation have not been evaluated

## High-value next steps

- normalize avatar assets into one coherent visual set
- add camera selection and saved calibration profiles
- separate camera/landmark logic from UI for unit testing
- explore a true transparent-background window with purpose-built PNG assets
- record a privacy-safe calibration and expression demo

## License and authorship

Created by [SimpleCaci](https://github.com/SimpleCaci) and released under the [MIT License](LICENSE).
