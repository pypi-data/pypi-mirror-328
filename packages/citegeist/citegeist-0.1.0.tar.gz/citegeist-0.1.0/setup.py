from setuptools import setup, find_packages

setup(
    name='citegeist',
    version='0.1.0',
    description='A spatial transcriptomics deconvolution tool for cell type identification and gene expression analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Alexander Chang, Brent T. Schlegel',
    author_email='acc383@cornell.edu',
    url='https://github.com/acc383/CITEgeist',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.20.0',
        'pandas>=1.3.0',
        'scanpy>=1.9.0',
        'scipy>=1.7.0',
        'pyarrow>=5.0.0',
        'gurobipy>=9.5.0',
        'squidpy>=1.6.2',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=3.0.0',
            'black>=22.0.0',
            'isort>=5.10.0',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    python_requires='>=3.8',
) 