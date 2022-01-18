from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Converting sql to dbf files'
LONG_DESCRIPTION = 'A package that allows to convert sql to dbf files.'

# Setting up
setup(
    name="sql2dbf",
    version=VERSION,
    author="NurlanEmilbekuulu (Nurlan Emilbek uulu)",
    author_email="<nurlan.emilbekuulu96@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'sql', 'dbf', 'conversion'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)