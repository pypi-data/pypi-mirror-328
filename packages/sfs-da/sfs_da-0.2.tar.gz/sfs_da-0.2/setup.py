from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='sfs-da', 
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'mpmath',
        'scipy',
        'scikit-learn'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Nguyen Thang Loi',
)