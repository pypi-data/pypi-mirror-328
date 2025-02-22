from setuptools import setup, find_packages

setup(
    name='sfs-da', 
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'mpmath',
        'scipy',
        'scikit-learn'
    ]
)