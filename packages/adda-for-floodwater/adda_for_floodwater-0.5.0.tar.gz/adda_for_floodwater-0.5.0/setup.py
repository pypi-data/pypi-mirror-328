from setuptools import setup

setup(
    name='adda_for_floodwater',
    version='0.5.0',    
    description='ADCIRC Data Assimilator for Floodwater',
    url='https://github.com/RENCI/adda_for_floodwater',
    author='Brian Blanton',
    author_email='bblanton@renci.org',
    license='MIT',
    packages=['adda_for_floodwater'],
    install_requires=[
        'pandas',
        'numpy',
        'netCDF4',
        'matplotlib',
        'pyyaml',
        'scipy',
        'scikit-learn',
        'lxml',
        'xmltodict',
        'xarray',
        'matplotlib',
        'siphon',
        'noaa-coops',
        'utide' ],

    classifiers=[
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
    ],
)
