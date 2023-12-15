from distutils.core import setup

history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
  name = 'cascadict',
  packages = ['cascadict'], # this must be the same as the name above
  version = '0.8.5',
  description = (
    'Cascading dictionary - CascaDict implements something like class inheritance, but on dictionary-key level.'
    ' Ideal for representing cascading properties, e.g. configurations with default parameters etc.'
    ),
  long_description = """
  See full documentation on `ReadTheDocs <http://cascadict.readthedocs.org>`_.

  """ + '\n\n' + history,
  author = 'Josef Nevrly',
  author_email = 'josef.nevrly@gmail.com',
  url = 'https://github.com/JNevrly/cascadict', # use the URL to the github repo
  download_url = 'https://github.com/JNevrly/cascadict/archive/v0.8.4.zip',
  keywords = ['dictionary', 'inheritance', 'cascading', 'nesting', 'configuration'], # arbitrary keywords
  license = 'MIT License',
  classifiers = ['Development Status :: 4 - Beta',
  'License :: OSI Approved :: MIT License',
  'Operating System :: OS Independent',
  'Programming Language :: Python :: 2.7',
  'Programming Language :: Python :: 3',
  'Topic :: Software Development :: Libraries'],
)
