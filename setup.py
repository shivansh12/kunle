from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in kunle/__init__.py
from kunle import __version__ as version

setup(
	name="kunle",
	version=version,
	description="customizations",
	author="kunle",
	author_email="kunle1@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
