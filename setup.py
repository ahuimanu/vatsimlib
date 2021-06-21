from setuptools import setup, find_packages

setup(
    name="vatsimlib",
    version="0.1.0",
    description="The VATSIMLIB library consumes VATSIM REST services and will store fetched records in a data backend.",
    author="Jeffry Babb",
    author_email="ahuimanu@gmail.com",
    packages=find_packages(include=["vatsimlib", "vatsimlib.*"]),
    install_requires=[
        "requests",
    ],
)
