from importlib.metadata import entry_points
from setuptools import find_packages
from setuptools import setup

setup(
    name="movie_readed",
    version="1.0.0",
    description="The package contains python code reading and fetching data from specific data set given by the instructor",
    author="Sofia Vasileva",
    author_email="sofiyavv98@gmail.com",
    url="",
    packages=find_packages(exclude="movie_reader_unittests")
    # entry_points={
    #     "console_scripts": [
    #         "movie-reader-cli" : ""
    #     ]
    # }
)