# setup.py
from setuptools import setup,find_packages
from pathlib import Path

setup(
    name="Arkenspy",
    version="1.0.2",
    packages=find_packages(),
    install_requires=[
        "github"
    ],
    author="as2rofy",
    author_email="a28092452@gmail.com",
    description="Arkenspy is a token manager library",
    long_description= "README.md",
    long_description_content_type="text/markdown",
    license="MIT",
    project_urls={
        "Source Repository" : "https://github.com/anigamer101/Arkens"
    }
)