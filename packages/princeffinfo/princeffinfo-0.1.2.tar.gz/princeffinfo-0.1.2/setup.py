from setuptools import setup, find_packages

setup(
    name="princeffinfo",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    description="A package to fetch Free Fire account info.",
    author="PRINCE-LK",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)