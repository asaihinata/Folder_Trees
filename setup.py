from setuptools import setup,find_packages
setup(
name="Folder_Trees",
version="1.0.1",
packages=find_packages(),
entry_points={"console_scripts":["trees=tree.core:main",],},
)