from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="realsense_depth_detector",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyrealsense2",
        "numpy",
        "opencv-python",
        "ultralytics",
    ],
    author="Harikrishna U Kamath",
    author_email="ekts00243@gmail.com",
    description="A package for object detection with depth using RealSense cameras",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ekts00243/realsense_depth.git",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    keywords="realsense, depth detection, computer vision, yolo, object detection",
)
