from setuptools import setup, find_packages

setup(
    name="multiworks",
    version="0.2.1",
    packages=find_packages(),  # Ensure it detects multiworks/
    include_package_data=True,  # Ensures non-Python files inside package are included
    install_requires=[],  # Add any dependencies here
    author="Mohammad Sabbir Hosen",
    author_email="hellowsabbir@gmail.com",
    description="Encrypts/decrypts messages and includes games of Rock, Paper, Scissors (RPS) and Snake, Water, Gun (SWG).",
    long_description=open("README.md", encoding="utf-8").read(),  # Encoding fix
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://pypi.org/project/multiworks/",  # Link to PyPI or GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify minimum Python version
)
