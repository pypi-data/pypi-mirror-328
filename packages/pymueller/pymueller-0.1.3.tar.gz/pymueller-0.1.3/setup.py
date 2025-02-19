from setuptools import setup, find_packages

setup(
    name="pymueller",  # The name of your package
    version="0.1.3",   # Your current version
    description="Tools and functions for 4x4 Mueller matrices",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Chae chae",
    author_email="a40075@outlook.com",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.20",
        "opencv-python>=4.11"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
