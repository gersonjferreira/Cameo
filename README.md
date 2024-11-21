# Cameo

Display webcam as circular overlay on top of other windows. Radius and zoom can be controlled with the mouse.

## Install

Install the latest version directly from the github repository:

```bash
pip install git+https://github.com/gersonjferreira/Cameo.git
```

## Usage

Run from command line as:

```bash
Usage: $ cameo [options]
Options:
  --help       Display this information
  --webcam     Set webcam index (default 0), usually even numbers only: 0, 2, 4...
```

The overlay can be controlled with the mouse:

- Click and drag to move the overlay around.
- Mouse scroll to change the circle radius.
- Shift + scroll to change the webcam zoom.
- Right click to quit.
