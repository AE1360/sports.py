from distutils.core import setup

setup(
    name='sports.py',
    packages=['sports_py'],
    version='1.1.1',
    description='A simple Python package to gather live sports scores',
    author='Evan Sloan',
    author_email='evansloan082@gmail.com',
    url='https://github.com/evansloan082/sports.py',
    download_url='https://github.com/evansloan082/sports.py/archive/v1.1.1.tar.gz',
    keywords=['sports', 'scores', 'live scores', 'hockey', 'basketball', 'baseball', 'football'],
    classifiers=[],
    install_requires=['requests'],
)