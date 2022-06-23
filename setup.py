from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='tfa-python-sdk',
    packages=find_packages(),
    version='1.0.0',
    author='Amirhossein Mohammadi',
    license='MIT',
    author_email="amirhosseinmohammadi1380@yahoo.com",
    description="Telegram Factor Authentication python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tele-fa/tfa-python-sdk",
    install_requires="requests"
)