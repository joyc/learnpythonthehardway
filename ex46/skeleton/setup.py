try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'joyc',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.'
    'author_email': 'rockbee@gmail.com',
    'version': '0.1'
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'script': [],
    'name': 'projectname'
}

setup(**config)