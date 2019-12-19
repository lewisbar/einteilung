import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="einteilung",
    version="0.0.1",
    author="Lennart Wisbar",
    author_email="lewisbar.git@gmail.com",
    description="Makes a plan which volunteer musicians/sound guys are in charge at which date in our church service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lewisbar/einteilung",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)