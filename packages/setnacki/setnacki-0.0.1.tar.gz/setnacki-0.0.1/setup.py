from setuptools import find_packages, setup

with open("src/README.md", "r") as f:
    long_description = f.read()

setup(
    name="setnacki",
    version="0.0.1",
    description="The card game Setback",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bernackimark/setback",
    author="Bernacki",
    author_email="bernackimark@gmail.com",
    extras_require={"dev": "twine>=4.0.2"},
    python_requires=">=3.10",
)
