from setuptools import setup, find_packages

setup(
    name='MYPACKAGE',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='This is an example of a  python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Sumbati10',
    author='<Lindah Sumbati>',
    author_email='<sumbatilinda@gmail.com>'
)