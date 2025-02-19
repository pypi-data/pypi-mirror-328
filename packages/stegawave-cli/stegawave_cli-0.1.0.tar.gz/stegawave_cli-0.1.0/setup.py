# setup.py
from setuptools import setup, find_packages

setup(
    name="stegawave-cli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer>=0.9.0",
        "requests>=2.31.0",
        "python-dateutil>=2.8.2",
        "rich>=13.3.5",  
        "pydantic>=2.4.2" 
    ],
    entry_points={
        "console_scripts": [
            "stegawave=stegawave.cli:app",
        ],
    },
)