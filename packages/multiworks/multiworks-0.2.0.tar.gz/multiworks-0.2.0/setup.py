from setuptools import setup, find_packages


setup(
    name="multiworks",
    version="0.2.0",
    packages=find_packages(),
    author="Mohammad Sabbir Hosen",
    author_email='hellowsabbir@gmail.com',
    description="Encrypts/decrypts messages and includes games of Rock, Paper, Scissors (RPS) and Snake, Water, Gun (SWG).",
    long_description=open("README.md").read(),
    license='MIT',
    long_description_content_type="text/markdown",
)

