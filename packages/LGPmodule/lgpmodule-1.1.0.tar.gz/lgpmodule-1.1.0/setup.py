from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="LGPmodule",
    version="1.1.0",
    packages=find_packages(),
    description="Just a small package used in little guy's projects.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Grumm"
)