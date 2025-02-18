from setuptools import setup, find_packages
import os

def get_version():
    return os.getenv("GITHUB_REF", "refs/tags/1.0.0").split("/")[-1]

setup(
    name = "beetmon",
    version = get_version(),
    packages = find_packages(),
    install_requires = ["watchdog","beet","pyyaml"],
    entry_points = {
        "console_scripts": [
            "beetmon=beetmon.beetmon:main",
        ],
    },
    author="Your Name",
    description="A file watcher that runs 'beet build' on file changes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/IconikoUlG/beetmon",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
