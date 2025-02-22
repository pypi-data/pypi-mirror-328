from setuptools import setup, find_packages

setup(
    name="translib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "googletrans==4.0.0-rc1"
    ],
    author="Phillip",
    author_email="tranquanganhminh25313@gmail.com",
    description="A simple translation library",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url=" ",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

