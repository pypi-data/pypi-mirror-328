from setuptools import setup, find_packages

# Read the README file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="flow_monitor",  # Name of your package
    version="0.2.0",      # Version number
    author="Rishabh",   # Your name
    author_email="rishabh@kritsnam.com",  # Your email
    description="A real-time flow data monitoring tool with a GUI.",  # Short description
    long_description=long_description,  # Long description from README
    long_description_content_type="text/markdown",  # Format of the long description
    url="https://github.com/KritsnamSoftware/DhaaraLive2.0",  # Project URL
    packages=find_packages(),  # Automatically find packages
    install_requires=[         # List of dependencies
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "pyserial>=3.5",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose a license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Python version requirement
    entry_points={
        "console_scripts": [
            "flow_monitor=flow_monitor.flow_monitor:main",  # Command-line entry point
        ],
    },
)