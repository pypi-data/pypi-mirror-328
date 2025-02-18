from setuptools import setup, find_packages

setup(
    name="dlview",
    version="0.1.0",
    packages=find_packages(),
    description="A data print helper for deep learning projects",
    install_requires=[],
    author="Lihao Wang",
    author_email="lihaowang@yahoo.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

