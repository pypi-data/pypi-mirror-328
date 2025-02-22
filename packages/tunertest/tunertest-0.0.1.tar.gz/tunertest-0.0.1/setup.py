from setuptools import setup, find_packages

setup(
    name="tunertest",
    version="0.0.1",
    author="Tuner",
    author_email="chenjianpeng97@outlook.com",
    description="a test framework based on behave",
    # long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chenjianpeng97/Tuner",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)