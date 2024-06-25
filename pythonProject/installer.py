from cx_Freeze import Executable
from setuptools import setup
import sys
import os

if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['tkinter', 'pytube'],
    }
}

setup(
    name="YouTube Downloader",
    version="1.0",
    description="YouTube Video Downloader",
    options=options,
    executables=[Executable("main3.py", base=base)]
)
