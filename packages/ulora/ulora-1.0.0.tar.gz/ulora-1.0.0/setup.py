from setuptools import setup, find_packages
import os


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ulora",  
    version="1.0.0",  
    description="ULoRa - ULoRa is a MicroPython library for SX127x LoRa modules (e.g., SX1276, SX1278) on embedded systems like ESP32, ESP8266, and ARM, enabling low-power, long-range communication for IoT applications.",
    long_description=long_description,  
    long_description_content_type="text/markdown", 
    author="Arman Ghobadi",  
    author_email="arman.ghobadi.ag@gmai.com",  
    url="https://github.com/armanghobadi/ulora",  
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
)
