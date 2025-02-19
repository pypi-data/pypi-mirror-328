from setuptools import setup, find_packages

setup(
    name="cxlop",
    version="0.1.0",
    author="runtime-erop",
    description="desc",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/runtime-erop",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
