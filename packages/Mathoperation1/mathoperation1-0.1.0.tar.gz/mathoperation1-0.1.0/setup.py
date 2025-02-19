from setuptools import setup, find_packages

setup(
    name="Mathoperation1",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple math operations package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)



# To generate library file=> 'python setup.py sdist bdist_wheel' creats ".tar.gz, .whl" files
# Install Twine using 'pip install twine'
# Upload your package to PyPi=>'twine upload dist/* -u __token__ -p your API key'
# My Api Key of PyPi is => pypi-AgEIcHlwaS5vcmcCJGMxOWVjYjcyLWJlMDEtNGMxMi1hNDY2LTQ2OGUzZjFlZjRhNgACKlszLCJmZTExZThkMC1kYTFlLTQ0YmQtYjY4Ny01ZGNmMTYxNTBiZGMiXQAABiCRtYd5gu7ky4Z2yE08WKkWwuDu94pk_9G7ZWLUyPv8GQ
