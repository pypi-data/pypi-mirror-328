import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opengrad",
    version="0.0.1",
    author="Priya Aryav",
    author_email="priya.aryav@gmail.com",
    description="A small autograd engine and neural net library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamaryav/opengrad",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)