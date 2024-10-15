# Motion Detector

This repository contains a simple motion detection system implemented in Python using OpenCV. The motion detector captures video from your webcam, detects motion, and logs the time periods during which motion was detected. Additionally, it provides a visualization of the detected motion periods.

## Files

- `motion_detector.py`: The main script for detecting motion and recording the time intervals of detected motion.
- `plotting.py`: A script for visualizing the detected motion periods using Bokeh.

## Requirements

To run the motion detector, you'll need to install the required packages listed in `requirements.txt`. You can do this using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. <b>Run the motion detector:</b> Open a terminal and run the plotting.py script:

```bash
python plotting.py
```

The script will open your webcam and start detecting motion. Press 'q' to stop the detection.

2. <b>View the logged motion times:</b> After stopping the script, a CSV file named times.csv will be created in the same directory. This file contains the start and end times of detected motion periods.

3. <b>Visualize the motion periods:</b> The plotting.py script will create an HTML file named graph.html which displays a graphical representation of the detected motion periods.
