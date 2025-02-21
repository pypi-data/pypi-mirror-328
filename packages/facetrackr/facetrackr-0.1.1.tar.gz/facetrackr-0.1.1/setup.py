from setuptools import setup, find_packages

with open("README2.md", "r") as f:
    description = f.read()
    
    
setup(
    name="facetrackr",
    version="0.1.1",
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
    },
    long_description=description,
    long_description_content_type="text/markdown",
)
