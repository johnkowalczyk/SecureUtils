from setuptools import setup, find_packages

setup(
    name="secureutils",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",      # For CLI
        "commons-codec",  # For encoding and hashing utilities
    ],
    entry_points={
        "console_scripts": [
            "secureutils=secureutils.cli:main",
        ],
    },
)
