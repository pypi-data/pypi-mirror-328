from setuptools import setup, find_packages

VERSION = "1.0.0"

with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="uuv_webrtc",
    version=VERSION,
    author="FEITENG",
    license="MIT License",
    url="https://github.com/FEITENG-0828/uuv_webrtc",
    description="UUV WebRTC Video Transmission System",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages("uuv_webrtc"),
    package_dir={"": "uuv_webrtc"},
    python_requires=">=3.11",
    install_requires=[
        "aiortc==1.10.1",
        "opencv-python==4.11.0.86"
    ]
)