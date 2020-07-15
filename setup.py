from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="manim_notebook",
    version="1.0.0",
    description="Integrates manim with jupyter notebook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AkashKarnatak/manim_notebook",
    author="Akash Karnatak",
    author_email="akashkarnatak.ak47@gmail.com",
    license="MIT",
    keywords = ["manim", "jupyter", "notebook", "jupyter notebook", "IPython"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["manim_notebook"],
    install_requires=[
        "IPython", 
        "manimlib",
        "notebook",
        "argparse"
        ],
    python_requires='>=3.6'
)
