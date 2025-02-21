from setuptools import find_packages, setup

setup(
    name="hbs",
    version="0.1.3",
    author="Lin Chenran",
    author_email="chenranlin.17@gmail.com",
    description="Python library for computing Harmonic Beltrami Signature(HBS)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ChanceAroundYou/hbs_python",
    packages=find_packages(),
    install_requires=[
        "numpy==2.2.3",
        "scipy==1.15.2",
        "matplotlib==3.10.0",
        "opencv-python==4.11.0.86",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
