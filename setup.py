from setuptools import setup

long_description = open("README.md").read()

setup(
    name="matplotlib-colors",
    version="1.0.15",
    author="Tom Draper",
    author_email="tomjdraper1@gmail.com",
    license="MIT",
    description="A collection of curated colors and colormaps for matplotlib.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tom-draper/matplotlib-colors",
    key_words="visualization color colormap colorset matplotlib",
    install_requires=['matplotlib'],
    packages=["matplotlib_colors"],
    python_requires=">=3.6",
)