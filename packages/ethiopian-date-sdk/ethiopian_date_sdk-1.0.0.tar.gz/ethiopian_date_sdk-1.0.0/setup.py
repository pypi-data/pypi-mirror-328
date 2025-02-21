from setuptools import setup, find_packages

setup(
    name="ethiopian_date_sdk",
    version="1.0.0",
    description="A Python SDK for converting dates between the Ethiopian and Gregorian calendars.",
    author="Zelalem Tamrie",
    author_email="zelalem.t8@gmail.com",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)