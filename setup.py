from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='example-pkg-theacodesKozan',
  version='0.0.1',
  description='This module help you check large chains or sequences',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Cherilus Sam Bracley',
  author_email='cherilussambracley@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='search', 
  packages=find_packages(),
  install_requires=[''] 
)
