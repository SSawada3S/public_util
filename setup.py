# https://zenn.dev/kotai/articles/49bd8b550fefca
from setuptools import setup, find_packages

setup(
    name="report_writing_tools",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
