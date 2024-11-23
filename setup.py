import os
from setuptools import setup, find_packages

# Function to read the version from the __init__.py file
def read_version():
    version_file = os.path.join(os.path.dirname(__file__), 'cameo', '__init__.py')
    with open(version_file) as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip("'")

# function to create desktop file with proper icon path
def create_desktop_file():
    desktop_entry = """[Desktop Entry]
Name=Cameo
Comment=Display webcam as circular overlay on top of other windows
Exec="cameo --webcam 0"
Icon={icon_path}
Terminal=false
Type=Application
Categories=Utility;
"""
    with open('cameo.desktop', 'w') as f:
        f.write(desktop_entry.format(icon_path=os.path.expanduser('~/.local/share/icons/cameo.png')))

# setup precedure
create_desktop_file()

setup(
    name='Cameo',
    version=read_version(),
    author='Gerson J. Ferreira',
    author_email='gersonjferreira@ufu.br',
    description='Display webcam as circular overlay on top of other windows',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gersonjferreira/Cameo',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'PyQT5',
        'opencv-python',
    ],
    entry_points={
        'console_scripts': [
            'cameo=cameo.cameo:main',
        ],
    },
    data_files=[
        ('share/applications', ['cameo.desktop']),
        ('share/icons', ['cameo.png']),
    ],
)
