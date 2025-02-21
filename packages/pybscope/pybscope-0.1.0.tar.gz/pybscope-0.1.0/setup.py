from setuptools import setup, find_packages

setup(
    name="pybscope",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pylgbst",
        "pybricksdev"
    ],
    author="Nogeese",
    author_email="leoszen@aol.com",
    description="A Python module for LEGO BOOST, SPIKE Prime, and RI communication.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/leon8326-nogeese/pybscope",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",  # PyPI doesn't support NPL 1.0 officially
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="NPL 1.0",
    license_files=["LICENSE"],
)
