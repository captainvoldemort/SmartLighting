# Smart Lighting System

Create an intelligent lighting system using Raspberry Pi, a PIR motion sensor, and computer vision techniques. This system enhances energy efficiency by automatically turning on lights when motion is detected and analyzing captured images to determine the presence of humans. The lights are turned off when no humans are detected, contributing to a smarter and more energy-conscious home.

## Features

- Motion-based lighting control using the PIR sensor.
- Detects humans using Histogram of Oriented Gradients (HOG) and OpenCV.
- Energy-efficient lighting management.
- Clear algorithm flow for easy understanding.

## Prerequisites

- Raspberry Pi with GPIO support.
- PIR sensor wired to GPIO (update `pir_pin` in the code if needed).
- OpenCV library installed (`pip install opencv-python`).
- Haar cascade XML file for face detection.

## Setup

1. Clone this repository to your Raspberry Pi.
2. Wire up the PIR sensor to the specified GPIO pin.
3. Download the Haar cascade XML file for face detection and place it in the project directory.
4. Create a folder named `CAPTURED_IMAGES` to store images.

## Usage

1. Run the main script: `python LightingSys.py`
2. The system monitors for motion using the PIR sensor.
3. Upon motion detection, lights are automatically turned on.
4. Images are captured and analyzed for human presence.
5. If humans are present, lights remain on. Otherwise, lights are turned off.

## Configuration

- Adjust the `capture_interval` (in seconds) to control capture frequency.
- Calibrate the PIR sensor for accurate motion detection.
- Customize GPIO pin assignments and settings as needed.

## Notes

- This project showcases a basic smart lighting concept.
- Consider expanding it with remote control or time-based features.
