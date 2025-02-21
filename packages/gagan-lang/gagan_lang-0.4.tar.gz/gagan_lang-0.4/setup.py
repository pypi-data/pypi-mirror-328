from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gagan-lang",
    version="0.4",
    author="Gagan",
    author_email="imgaganhonor@gmail.com",
    description="The world's simplest programming language.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/higgn/gagan-lang",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        'console_scripts': [
            'ggn = gagan.interpreter:main',  # Changed from 'gagan' to 'ggn'
        ],
    },
    include_package_data=True,
)