import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yolo_auto", # Replace with your own username
    version="0.0.2",
    author="Arjun Pandey",
    author_email="apandey@jpischool.com",
    description="Train custom YOLOv3 object detectors in two lines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pandeajrun242",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = ['GitPython']
)
