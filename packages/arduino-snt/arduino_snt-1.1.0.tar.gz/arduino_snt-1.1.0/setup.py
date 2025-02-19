from setuptools import setup, find_packages

setup(
    name="arduino-snt",
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        "pyfirmata>=1.1.0"
    ],
)