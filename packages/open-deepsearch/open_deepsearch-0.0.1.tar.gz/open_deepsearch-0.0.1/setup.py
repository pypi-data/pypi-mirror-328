from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='open_deepsearch',
    version='0.0.1',
    author='Jason Chuang',
    author_email='chuangtcee@gmail.com',
    description='Open DeepResearch',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aidatatools/open-deepresearch',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    install_requires=[
        'setuptools>=70.0.0'
    ],
    entry_points={
        'console_scripts': [
            'open_deepresearch = open_deepresearch.main:main',
        ],
    },
    # This line enables editable installs
    # With 'pip install -e .' equivalent
    # to install your package in editable mode
    # so changes in your source code are immediately reflected
    # without needing to reinstall
    options={'bdist_wheel': {'universal': True}},
    setup_requires=['setuptools>=70.0.0', 'wheel'],
    editable=True
)