from setuptools import setup, find_packages

setup(
    name="facetrackr",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "opencv-python",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "facetrackr=facetrackr.main:main"
        ]
    }
)
