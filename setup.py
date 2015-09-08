from distutils.core import setup
setup(
  name = 'cascadict',
  packages = ['cascadict'], # this must be the same as the name above
  version = '0.8.2',
  description = 'Cascading dictionary - CascaDict implements something like class inheritance, but on dictionary-key level. Ideal for representing cascading properties, e.g. configurations with default parameters etc.',
  author = 'Josef Nevrly',
  author_email = 'josef.nevrly@gmail.com',
  url = 'https://github.com/JNevrly/cascadict', # use the URL to the github repo
  download_url = 'https://github.com/JNevrly/cascadict/archive/v0.8.2.zip', 
  keywords = ['dictionary', 'inheritance', 'cascading', 'nesting', 'configuration'], # arbitrary keywords
  license = 'MIT License',
  classifiers = ['Development Status :: 4 - Beta',
  'License :: OSI Approved :: MIT License',
  'Operating System :: OS Independent',
  'Programming Language :: Python :: 2.7',
  'Programming Language :: Python :: 3',
  'Topic :: Software Development :: Libraries'],
)