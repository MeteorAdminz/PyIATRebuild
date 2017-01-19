from setuptools import setup
import os


setup(
    name='pyaitrebuild',
    version=0.2,
    url='https://github.com/OALabs/PyIATRebuild',
    author="OpenAnalysis",
    description="Import address rebuild and PE dump.",
    install_requires=['winappdbg','distorm3','elfesteem'],
    py_modules=['pyiatrebuild'],
    entry_points={'console_scripts': ['pyiatrebuild=pyiatrebuild:main']}
)
