# setup.py - for packaging gitq as an installable Python CLI tool

from setuptools import setup, find_packages

setup(
    name='gitq',
    version='1.0.0',
    py_modules=['gitq'],
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'gitq = gitq:main',
        ],
    },
    author='M. Hemanth Reddy',
    description='Enhanced Git Navigation using Deques and Smart Queues for Undo/Redo Commit Traversal',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/gitq',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
