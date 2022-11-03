from setuptools import setup, find_packages

long_description = open("README.md").read()
required = ['matplotlib']

setup(
    name="matplotlib-colors",
    version="1.0.0", # eg:1.0.0
    author="Tom Draper",
    author_email="tomjdraper1@gmail.com",
    license="MIT License",
    description="A collection of curated colors and colormaps for matplotlib.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tom-draper/matplotlib-colors",
    key_words="color style matplotlib colormap",
    install_requires=required,
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)