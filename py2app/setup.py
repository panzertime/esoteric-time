"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['myApp.py']
DATA_FILES = ['esoteric_time/aquarius.mp3']
OPTIONS = {
    'iconfile': 'digital-clock.icns'
}

setup(
    name="Esoteric Time",
    packages = ['esoteric_time'],
    app = APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)