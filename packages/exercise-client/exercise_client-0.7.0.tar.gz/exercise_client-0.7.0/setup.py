import setuptools
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="exercise-client",
    version="0.7.0",
    author="Kasper Munch",
    author_email="kaspermunch@birc.au.dk",
    description="Tool for launching jupyter from docker containers", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/kaspermunch/geneinfo",
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    entry_points = {
        'console_scripts': [
            'franklin-jupyter=exercise_client:jupyter',
            'franklin=exercise_client:franklin',
            ]
    },    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'requests>=2.32',
          'colorama>=0.4',
          'readchar>=4.0',
          'click'
    ])
