from setuptools import setup, find_packages

setup(
    name="depgeist",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": ["depgeist=depgeist.cli:main"],
    },
    author="Your Name",
    description="A smart dependency checker for Python projects.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourname/DepGeist",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)