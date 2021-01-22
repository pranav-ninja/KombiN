import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KombiN",
    version="1.0.1",
    author="Pranavkumar Patel",
    author_email="pranavkvp@theyei.com",
    description="Indexing combinations from two finite sets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pranav-ninja.github.io/KombiN/",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)