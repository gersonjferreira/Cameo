import os
from setuptools import setup, find_packages

# Function to read the version from the __init__.py file
def read_version():
    version_file = os.path.join(os.path.dirname(__file__), 'cameo', '__init__.py')
    with open(version_file) as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip("'")

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
)
