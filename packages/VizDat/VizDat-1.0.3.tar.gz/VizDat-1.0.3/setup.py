from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='VizDat',
    version='1.0.3',
    author='Mustafa FarajAllah',
    author_email='mustafa.farajallah99@gmail.com',
    description='A fast and simple data visualization library for tabular data.',
    url='https://github.com/MustafaFarajAllah/VizDat',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'pandas',
        'numpy',
        'scipy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    long_description=long_description,
    long_description_content_type="text/markdown",
)