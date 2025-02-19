from setuptools import setup, find_packages

setup(
    name="CBOD",
    version="0.2.0",
    author="Seffi Cohen",
    author_email="seffi@post.bgu.ac.il",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SeffiCohen/CBOD",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
install_requires=[
    "torch>=1.10.0",
    "transformers>=4.25.0",
    "tqdm>=4.60.0",
    "requests>=2.25.0",
    "datasets>=2.0.0",
],

)
