"""
Character Library - Setup Configuration

Comprehensive personality modeling system for AI characters
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        return f.read()

setup(
    name='character-library',
    version='1.0.0',
    author='Luciddreamer Team',
    author_email='contact@luciddreamer.ai',
    description='Comprehensive personality modeling system for AI characters',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/luciddreamer/character-library',
    project_urls={
        'Bug Reports': 'https://github.com/luciddreamer/character-library/issues',
        'Source': 'https://github.com/luciddreamer/character-library',
        'Documentation': 'https://github.com/luciddreamer/character-library/docs',
    },

    packages=find_packages(exclude=['tests', 'tests.*', 'examples', 'docs']),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],

    python_requires='>=3.8',

    install_requires=[
        'numpy>=1.20.0',
    ],

    extras_require={
        # Full agent integration with memory system
        'agent': [
            'hierarchical-memory>=1.0.0',
        ],
        # Development dependencies
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=23.0.0',
            'flake8>=6.0.0',
            'mypy>=1.0.0',
        ],
        # Documentation dependencies
        'docs': [
            'sphinx>=5.0.0',
            'sphinx-rtd-theme>=1.0.0',
        ],
    },

    entry_points={
        'console_scripts': [
            'character-demo=character_library.examples.demo:main',
        ],
    },

    keywords=(
        'ai character personality psychology '
        'big-five enneagram mbti emotions '
        'agent simulation dialogue modeling'
    ),

    include_package_data=True,
    zip_safe=False,
)
