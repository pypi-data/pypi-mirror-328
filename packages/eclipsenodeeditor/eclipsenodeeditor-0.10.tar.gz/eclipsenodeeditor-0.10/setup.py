from setuptools import setup, find_packages
import os

# Read version from version.txt
with open('version.txt') as f:
    version = f.read().strip()

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Read long description from README.md
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='eclipsenodeeditor',
    version=version,
    description='A node-based editor built with PyQt6',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/eclipsenodeeditor',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'eclipsenodeeditor': [
            'static/*',
            'static/monaco/**/*',  # Include all Monaco files recursively
        ],
    },
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.8',
)
