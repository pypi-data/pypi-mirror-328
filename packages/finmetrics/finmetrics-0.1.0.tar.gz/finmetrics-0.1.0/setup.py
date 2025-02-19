from setuptools import setup, find_packages

setup(
    name="finmetrics",  # Replace with your package name
    version="0.1.0",
    author="Mihir Gajjar",
    description="A Python Package to Perform common financial operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",  # Replace with your repo URL if applicable
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.6'
)
