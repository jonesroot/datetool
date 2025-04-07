from setuptools import setup, find_packages

setup(
    name="datetools",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "jsonargparse",
        "pytz",
        "sphinx",
        "sphinx-argparse"
    ],
    entry_points={
        'console_scripts': [
            'datetools = datetools:main',
        ],
    },
)
