# Gesture-Reactive Avatar

A local computer-vision avatar that reacts to facial expressions in real time.

The project uses a webcam and MediaPipe Face Mesh to classify expressions, smooth rapid changes, and select a matching cat reaction image. It is an early step toward a lightweight, non-pixel avatar for streaming, recording, and playful desktop interaction.

> **Status:** working prototype. The expression pipeline is implemented, but setup, calibration quality, and camera behavior still require validation across different faces, lighting, and devices.

## Capabilities

- captures a local webcam feed with OpenCV
- tracks one face with refined MediaPipe landmarks
- calibrates expression measurements to the current user
- recognizes eye, eyebrow, and mouth state combinations
- smooths rapid expression changes to reduce avatar flicker
- maps expression rules to a library of reaction images
- displays the landmark view and avatar in separate windows

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

Look toward the camera while calibration collects its baseline. Press **Escape** to close the application.

## Demo

The current reaction-image set is under `images/`. A privacy-safe screen recording showing calibration and several expression transitions is still needed.

## Validation status

No automated tests or CI workflow currently exist. Before calling this production-ready, verify camera failure handling, calibration completion, expression transitions, Escape shutdown, and behavior when no face is visible.

## Known limitations

- thresholds are rule-based rather than learned from a diverse dataset
- calibration feedback is not yet visible to the user
- camera selection is fixed to device 0
- the raw landmark window is intended for debugging
- reaction images have inconsistent source styles and dimensions
- accessibility and headless operation have not been evaluated

## High-value next steps

- add visible calibration progress and retry controls
- normalize avatar assets into one coherent visual set
- separate camera/landmark logic from UI for unit testing
- add a transparent-background avatar window for streaming
- create a small expression-debug overlay and recorded demo

## License and authorship

Created by [SimpleCaci](https://github.com/SimpleCaci) and released under the [MIT License](LICENSE).
