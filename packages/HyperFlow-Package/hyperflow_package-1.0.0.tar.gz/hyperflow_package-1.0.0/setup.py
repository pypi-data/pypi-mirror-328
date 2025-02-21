from setuptools import setup, find_packages

with open("app/Readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="HyperFlow_Package",
    version="1.0.0",
    description="HyperFlow: Next-Generation Computational Framework for Machine Learning & Deep Learning",
    long_description=long_description,
    license_files=['LICENSE'],
    long_description_content_type="text/markdown",
    packages=find_packages(where="app"),  
    package_dir={"": "app"},
    package_data={"": ["Readme.md"]},
    include_package_data=True,
    url="https://github.com/Shyanil/HyperFlow/tree/main/The%20HyperFlow/HyperFlow",
    author="Shyanil Mishra",
    author_email="shyanilmishra94@gmail.com",
    install_requires=[
        "numpy>=1.26, <2.1"
    ],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.8",
)
