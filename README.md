# Cameo

Display webcam as circular overlay on top of other windows. Radius and zoom can be controlled with the mouse. Check the youtube video to see it working.

[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://youtu.be/B5YFOsQF_Pg)

## Install

Here I assume you are using conda or miniconda. To install the latest version directly from the github repository:

```bash
# Create a dedicated environment if needed:
conda create -n cameo_env

# Activate the environment
conda activate cameo_env

# Install requirements
conda install conda-forge::opencv pyqt

# Install the package from GitHub
pip install --user git+https://github.com/gersonjferreira/Cameo.git

# Deactivate the environment
conda deactivate
```

Above, the `--user` flag on the installation command is necessary to make the command `cameo` available even when the environment is not activated.

## Usage

The installation already creates a desktop file `~/.local/share/applications/cameo.desktop` such that you can open it from the menus of your DE. By default, it runs with `--webcam 0` to call the main webcam, but if you need to change webcams, please edit this file accordingly.

If you prefer to run from command line, here are the options:

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

## FAQ, support and contributions

> It runs fine on my computer.

I wrote this code for myself, it runs fine on Manjaro + KDE + X11.

> Does not work with Wayland.

I had problems with Wayland, but since I don't plan to move to Wayland any time soon, I will not touch this issue for a while.

> Contributors and forks are welcome.

If you like the app and want to improve it, please feel free to contact me, raise issues, fork and make merge requests. But keep in mind that I'm not a professional software developer and I did this code only to satisfy my needs.
