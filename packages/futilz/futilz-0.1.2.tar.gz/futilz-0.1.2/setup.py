from setuptools import setup, find_packages

setup(
    name                          = "futilz",  # Unique name on PyPI
    version                       = "0.1.2",
    packages                      = find_packages(),
    install_requires              = [],  # Dependencies (e.g., ["requests", "numpy"])
    author                        = "Abdelmathin Habachi",
    author_email                  = "abdelmathinhabachi@gmail.com" ,
    description                   = "A brief description of futilz",
    long_description              = open("README.md").read(),
    long_description_content_type = "text/markdown",
    url                           = "https://github.com/Abdelmathin/futilz",
    classifiers                   = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7",
)
