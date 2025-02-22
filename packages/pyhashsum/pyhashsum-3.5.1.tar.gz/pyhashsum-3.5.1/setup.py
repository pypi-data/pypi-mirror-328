from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='pyhashsum',
    version='3.5.1',
    author='oop7',
    author_email='oop7_support@proton.me', 
    description='Cross-platform file integrity verification tool with modern GUI',
    long_description=Path('README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    url='https://github.com/oop7/pyhashsum',
    packages=find_packages(),
    install_requires=[
        'PySide6',
        'Pillow',
        'packaging'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Security :: Cryptography',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'pyhashsum=pyhashsum.main:main',
        ],
    },
    include_package_data=True,
    project_urls={
        'Homepage': 'https://github.com/oop7/pyhashsum',
        'Bug Tracker': 'https://github.com/oop7/pyhashsum/issues',
        'Support': 'mailto:oop7_support@proton.me',
        'Reddit': 'https://www.reddit.com/r/NO-N_A_M_E/',
    },
)