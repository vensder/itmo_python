# наш главный файл
# точка входа в пакет


from setuptools import setup, find_packages
from os.path import join, dirname

setup(
	name = 'my_mod',
	version = '1.0',
	packages = find_packages(),
	long_description = open(join(dirname(__file__), 'README.txt')).read(),
)
