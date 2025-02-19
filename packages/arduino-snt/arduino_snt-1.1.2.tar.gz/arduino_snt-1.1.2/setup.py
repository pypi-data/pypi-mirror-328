from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
readme_file = (this_directory / "README.md").read_text()

setup(
    name="arduino-snt",
    version='1.1.2',
    url="https://github.com/Amzu-bzh/arduino-snt",

    author="Amaury GODOT",

    description="Python package to easily control an arduino using Python.",
    long_description=readme_file,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pyfirmata>=1.1.0"
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12'
    ],
)