from setuptools import setup,find_packages
setup(
name="Folder_Trees",
version="1.0.0",
packages=find_packages(),
entry_points={"console_scripts":["trees = tree.core:main",],},
)