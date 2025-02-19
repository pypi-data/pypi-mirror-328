from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="boxabar",
    version="0.1.0",
    author="Jaloliddin SWE",
    author_email="jaloliddinswe@gmail.com",
    description="Turli xil xabar yuborish usullarini qo'llab-quvvatlovchi Python kutubxonasi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaloliddinswe/boxabar",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
