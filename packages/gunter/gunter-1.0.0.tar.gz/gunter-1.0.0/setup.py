from setuptools import setup, find_packages

setup(
    name="gunter",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'gunter=gunter:main',
        ],
    },
    author="saperoi",
    description="Program to turn any image of glyphs (with a consistent height and width) into a (Roman Czyborra) .hex-like format, and that into a .bdf",
    url="https://git.icosahedr.online/sapero/gunter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
