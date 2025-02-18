import setuptools

setuptools.setup(
    name="argconf",  # Replace with your own username
    version="0.3.0",
    author="Norman Müller",
    author_email="norman.mueller@tum.de",
    description="Simple config and argument parsing with nested conf structure",
    long_description_content_type="text/markdown",
    url="",
    install_requires=[
        "pyhocon",
        "python-box",
        "omegaconf",
    ],  # @ git+https://github.com/omry/omegaconf.git'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
