# FootAP

FootAP (FOOTball Analysis Package) is a Python package for analyzing ball touches in football videos.

## Installation

```bash
pip install footap
```

## Usage

You can use FootAP in two ways:

### 1. Command Line Interface

The simplest way to use FootAP is through the command line:

```bash
# Basic analysis (generates only results file)
footap video.mp4

# Analysis with real-time display
footap video.mp4 --display

# Analysis with video output
footap video.mp4 --save-video

# Full analysis with all options
footap video.mp4 --save-video -o output.mp4 -r results.txt --orientation 90 --display

# Display version
footap -v
# or
footap --version
```

Available options:
- `--save-video`: Generate an annotated output video
- `--display`: Show real-time processing
- `-o, --output`: Specify output video name (only with --save-video)
- `-r, --results`: Specify results file name
- `--orientation`: Video orientation in degrees (0, 90, 180, 270)
- `-v, --version`: Display version

### 2. Python API

```python
from footap import analyze_ball_touch

# Basic analysis
analyze_ball_touch("video.mp4")

# Full analysis with all options
analyze_ball_touch(
    input_video_path="video.mp4",
    display_processing=True,    # Show real-time processing
    generate_video=True,        # Generate output video
    video_orientation=90        # Rotate video if needed
)

# Get version
from footap import __version__
print(__version__)
```

## Output

The program generates two files:

1. Results file (always generated):
   ```
   Left Foot Touches: 5
   Right Foot Touches: 12
   ```

2. Details file (CSV format):
   ```csv
   Time,Touch
   00:00:01.233,Left Foot
   00:00:02.567,Right Foot
   00:00:03.100,Right Foot
   ```

3. Annotated video (optional, with --save-video):
   - Ball detection
   - Feet tracking
   - Real-time touch counter
  
## Dependencies

- OpenCV (opencv-contrib-python)
- MediaPipe
- NumPy
- Ultralytics (YOLO)
- Pillow

## License

This project is licensed under the MIT License.
