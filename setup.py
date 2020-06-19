# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in prussian_frappe_theme/__init__.py
from prussian_frappe_theme import __version__ as version

setup(
	name='prussian_frappe_theme',
	version=version,
	description='Prussian Frappe Theme',
	author='Roy Irwan',
	author_email='roy.irwan@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
