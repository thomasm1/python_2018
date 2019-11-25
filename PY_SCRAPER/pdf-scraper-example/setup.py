import setuptools


setuptools.setup(
    name="imrscrape",
    version="1.0.0",
    author="Russ Biggs",
    author_email="russbiggs@gmail.com",
    description="utility to scrape compliance data from APD IMRs",
    url="https://github.com/apd-forward/imr-scrape",
    packages=setuptools.find_packages(),
    install_requires=[
        "pypdf2",
        "halo"
    ],
    python_requires='>=3.7.0',
    classifiers=[
    ],
    entry_points={
        'console_scripts': [
            'imrscrape=imrscrape.cli:main_cli',
        ],
    },
)