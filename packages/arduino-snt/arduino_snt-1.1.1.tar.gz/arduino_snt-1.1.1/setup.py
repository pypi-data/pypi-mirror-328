from setuptools import setup, find_packages

setup(
    name="arduino-snt",
    version='1.1.1',
    url="https://github.com/Amzu-bzh/arduino-snt",

    author="Amaury GODOT",

    description="Python package to easily control an arduino using Python.",
    long_description=open("README.md").read(),
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