# setup.py

from setuptools import setup, find_packages

setup(
    name='aion_xtensions_chronos',  # Package name (use hyphens for PyPI)
    version='0.2',
    description='Aion Xtensions Chronos to generate AX mappings based on modules and use cases.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aion',
    author_email='aion@hcl.com',
    url='https://github.com/yourusername/aion-xtensions-chronos',  # Update with your actual URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[],  # Add any dependencies here
    python_requires='>=3.6',
)
