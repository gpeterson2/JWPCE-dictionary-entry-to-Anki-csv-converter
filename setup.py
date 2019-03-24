import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jwpce_convert",
    version="0.0.1",
    description="Converts jwcp files to csv.",
    author="Greg Peterson",
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pyside2'],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'jwpce_convert = jwpce_convert.cli:main',
        ],
        'gui_scripts': [
            'jwpce_convert_gui = jwpce_convert.gui:main',
        ],
    },
)
