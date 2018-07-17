try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'This is a Udemy tutorial flask api',
	'author': 'David Julian',
	'url': 'git location',
	'download_url': 'git download location',
	'author_email': 'david.julian@asu.edu',
	'version': '0.1',
	'install_requires': ['flask'],
	'packages': ['flask'],
	'scripts': [],
	'name': 'another_api'
}

setup(**config)

# below is the source of the section flask app
# https://github.com/schoolofcode-me/rest-api-sections/tree/master/section3
# https://github.com/schoolofcode-me/rest-api-sections/tree/master/section4
# https://github.com/schoolofcode-me/rest-api-sections/tree/master/section5

