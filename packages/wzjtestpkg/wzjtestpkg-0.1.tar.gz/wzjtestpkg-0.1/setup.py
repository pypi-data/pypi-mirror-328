from setuptools import setup, find_packages

setup(
    name='wzjtestpkg',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='wzj',
    author_email='wusir666666@163.com',
    description='A simple example package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mypackage',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)