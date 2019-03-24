from setuptools import setup
from pathlib import Path

HERE = Path(__file__)


def get_requirements():
    with HERE.with_name('requirements.txt').open(encoding='utf-8') as requirements:
        return requirements.read().split()


setup(
    name='log_analytics',
    version='0.1',
    py_modules=['cli'],
    install_requires=get_requirements(),
    entry_points='''
        [console_scripts]
        log_analytics=cli:main
    ''',
)
