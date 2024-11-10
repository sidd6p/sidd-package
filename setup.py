import setuptools

# Read the README file for long description
with open("README.md", "r") as fh:
    long_description = fh.read()

# Read the requirements from the requirements.txt file
with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

# Setup function for the package
setuptools.setup(
    name="SiddP6",                     # This is the name of the package
    version="0.1.0",                        # The initial release version
    author="Siddhartha Purwar",                     # Full name of the author
    description="Siddhartha Purwar portfolio pip package",
    long_description=long_description,      # Long description read from the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all Python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["sidd"],             # Name of the python package
    package_dir={'': '.'},     # Directory of the source code of the package
    install_requires=install_requires                     # Install other dependencies from requirements.txt
)
