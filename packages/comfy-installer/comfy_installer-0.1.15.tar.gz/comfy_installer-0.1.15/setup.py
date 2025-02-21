import os
from setuptools import setup, find_packages

def load_requirements():
    req_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(req_path):
        with open(req_path, "r") as f:
            return f.read().splitlines()
    return []

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="comfy-installer",
    version="0.1.15",
    description="A CLI tool to install custom nodes for ComfyUI using YAML configuration.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="khengyun",
    author_email="khaangnguyeen@gmail.com",
    packages=find_packages(),
    install_requires=load_requirements(),
    entry_points={
        "console_scripts": [
            "comfy-installer=comfy_installer.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
