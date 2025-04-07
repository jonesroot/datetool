from setuptools import setup, find_packages

setup(
    name="datetool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "jsonargparse",
        "pytz",
        "sphinx",
        "sphinx-argparse"
    ],
    entry_points={
        'console_scripts': [
            'datetools = datetools.py:main',
        ],
    },
)
