from setuptools import setup, find_packages

setup(
    name="texttransformer",
    version="0.1.0",
    author="Policken",
    author_email="a.komlev.0612@gmail.com",
    description="A simple text transformation library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
