import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BingeWatch_Saranoja",
    version="1.0.1",
    author="Calin Irina",
    author_email="contact@irinacalin.codes",
    description="A tool to monitor the favourite TV shows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Saranoja/Binge_Watch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
