# Virtual Mouse Using OpenCV and Mediapipe

## Overview

This project implements a virtual mouse using Python, OpenCV, and Mediapipe. The virtual mouse allows you to control your computer's mouse pointer using hand gestures detected by a webcam. The project includes features such as left click, right click, double click, and screenshot capture.

## Features

- **Move Mouse:** Control the mouse pointer by moving your index finger.
- **Left Click:** Perform a left click by making a specific gesture.
- **Right Click:** Perform a right click with another gesture.
- **Double Click:** Perform a double click with a different gesture.
- **Screenshot:** Take a screenshot with a specific hand gesture.

## Dependencies

The project requires the following Python packages:

opencv-python

mediapipe

pyautogui

pynput

These can be installed via requirements.txt.
## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Virtual-Mouse-Using-OpenCV-and-Mediapipe.git
   cd Virtual-Mouse-Using-OpenCV-and-Mediapipe
## Usage/Examples

Run the script:

python main.py

Hand Gestures:

Move Mouse: Move your index finger to control the pointer.

Left Click: Perform a left click gesture (index finger straight, thumb and middle finger close).

Right Click: Perform a right click gesture (middle finger bent, index finger straight).

Double Click: Perform a double click gesture (both index and middle fingers bent).

Screenshot: Perform a screenshot gesture (index and middle fingers close together).

Exit the application: Press q to quit.





## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements
OpenCV

Mediapipe

PyAutoGUI

Pynput

### `requirements.txt`

This file should list the dependencies required for your project:

```plaintext
opencv-python
mediapipe
pyautogui
pynput