from setuptools import setup, find_packages

setup(
    name="mec",  # Name of the tool/package
    version="0.1.0",  # Initial version
    description="Code for minimum-entropy coupling.",  # Short description
    url="https://github.com/user1342/WouldYouKindly",  # Replace with the project's GitHub URL
    packages=find_packages(),  # Automatically find package directories
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0",
        "Operating System :: Windows",
    ],
    python_requires=">=3.8",  # Minimum Python version required
)
