from setuptools import setup, find_packages

VERSION = "0.1.1"

setup(
    name="pykitten",
    version=VERSION,
    packages=find_packages(include=["pykitten", "pykitten.*"]),
    include_package_data=True,
    install_requires=[],
    author="Agra Bima Yuda",
    author_email="agra.bima.ab@gmail.com",
    description="A versatile Python toolkit for various utilities",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/grabim09/SnakeTools",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)