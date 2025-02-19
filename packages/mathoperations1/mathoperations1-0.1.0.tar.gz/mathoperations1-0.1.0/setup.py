from setuptools import setup, find_packages

setup(
    name="mathoperations1",
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



# To generate library file=> 'python setup.py sdist bdist_wheel' creats ".whl, .tar.gz" files
# Install Twine using 'pip install twine'
# Upload your package to PyPi=>'twine upload dist/* -u __token__ -p your API key'
# My Api Key of PyPi is => pypi-AgEIcHlwaS5vcmcCJDA0YmQ0MTM4LWJjY2ItNGFkNy1iNTYyLThkZWZiODFhNTNlNgACKlszLCJmZTExZThkMC1kYTFlLTQ0YmQtYjY4Ny01ZGNmMTYxNTBiZGMiXQAABiDNA2jvUrHn1sYhI6fMtgBqWianZHWuw7dZjfl1FkErFQ
