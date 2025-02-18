from setuptools import setup, find_packages

setup(
    name="quickdiscord",
    version="1.0.2",
    author="Ibrahim Mohsin",
    author_email="codingstudentbruh@gmail.com",
    description="A simple Quick discord bot generator that will make all the necessary starter files.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ibrahims-main/QuickDiscord",
    packages=find_packages(),
    install_requires=["InquirerPy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)