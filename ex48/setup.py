try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project47',
    'author': 'joyc',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'rockbee@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'script': [],
    'name': 'ex47'
}

setup(**config)