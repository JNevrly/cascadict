.. CascaDict documentation master file, created by
   sphinx-quickstart on Mon Sep 07 22:03:14 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CascaDict - cascading dictionary for Python
===========================================

This little class aims to solve just another almost nonexistent problem
- handling of cascading properties. To describe it simply, CascaDict
implements something like class inheritance, but on dictionary-key
level. See the code:

.. code:: python

    from cascadict import CascaDict
    
    fruit_properties = CascaDict({'type':'fruit', 'taste':'sweet', 'color':"I don't have any color, I'm an abstract concept!"})
    blueberry = fruit_properties.cascade({'name': 'blueberry', 'color':'blue'})
    
    print(blueberry['color'])
    print(blueberry['taste'])

.. parsed-literal::

    blue
    sweet
    

Internally, it's not just copy and append, one can also access all the
cascaded values:

.. code:: python

    print(blueberry.get_cascaded('color'))

.. parsed-literal::

    ['blue', "I don't have any color, I'm an abstract concept!"]
    

Cascaded ancestors are referenced, not copied:

.. code:: python

    fruit_properties['taste'] = 'bittersweet'
    blueberry['taste']



.. parsed-literal::

    'bittersweet'



CascaDicts can be nested, and any dict element put into CascaDict is
also nested as CascaDict:

.. code:: python

    fruit_properties['classification'] = {'kingdom': 'Plantae',}
    blueberry['classification'] = {'Order': 'Ericales', 'Family': 'Ericaceae', 'Genus': 'Vaccinium', 'Section': 'Cyanococcus'}
    
    blueberry['classification']['kingdom']



.. parsed-literal::

    'Plantae'



CascaDicts are of course iterable...

.. code:: python

    for key, value in blueberry.items():
        print(key,value)

.. parsed-literal::

    ('color', 'blue')
    ('name', 'blueberry')
    ('classification', <{'Section': 'Cyanococcus', 'Genus': 'Vaccinium', 'Order': 'Ericales', 'Family': 'Ericaceae'}, Ancestor: <{}, Ancestor: <{'kingdom': 'Plantae'}, Ancestor: None>>>)
    ('taste', 'bittersweet')
    ('type', 'fruit')
    

... and picklable

.. code:: python

    import pickle
    blueberry_jam = pickle.loads(pickle.dumps(blueberry))
    for key, value in blueberry_jam.items():
        print(key,value)

.. parsed-literal::

    ('color', 'blue')
    ('name', 'blueberry')
    ('classification', <{'Section': 'Cyanococcus', 'Genus': 'Vaccinium', 'Order': 'Ericales', 'Family': 'Ericaceae'}, Ancestor: <{}, Ancestor: <{'kingdom': 'Plantae'}, Ancestor: None>>>)
    ('taste', 'bittersweet')
    ('type', 'fruit')
    

If needed, CascaDict can be "flattened" into normal (nested) dict:

.. code:: python

    blueberry.copy_flat()



.. parsed-literal::

    {'classification': {'Family': 'Ericaceae',
      'Genus': 'Vaccinium',
      'Order': 'Ericales',
      'Section': 'Cyanococcus',
      'kingdom': 'Plantae'},
     'color': 'blue',
     'name': 'blueberry',
     'taste': 'bittersweet',
     'type': 'fruit'}



Or only the top (final) level of CascaDict, without any ancestor
properties, can be copied:

.. code:: python

    blueberry.copy_flat(level='skim')



.. parsed-literal::

    {'classification': {'Family': 'Ericaceae',
      'Genus': 'Vaccinium',
      'Order': 'Ericales',
      'Section': 'Cyanococcus'},
     'color': 'blue',
     'name': 'blueberry'}



Combined with (e.g.) yaml, it makes any configuration processing a
breeze:

.. code:: python

    import yaml
    
    config = '''
    defaults:
        port: 5556
        login_required: True
        logging: 
            level: DEBUG
            handler: stream
            
    process_1:
        max_runtime: 100
        login_required: False
        logging:
            handler: file
        
    process_2:
        port: 6005
        halt_on_error: True
        logging:
            level: ERROR
    
    '''
    
    raw_config = yaml.load(config)
    defaults = CascaDict(raw_config.pop('defaults'))
    properties = {} #no dict comprehension, remember Python 2.7 folk
    for k,v in raw_config.items():
        properties[k] = CascaDict(v, ancestor=defaults)
        
    for k,v in properties.items():
        print("{0}: {1}".format(k, v.copy_flat()))

.. parsed-literal::

    process_2: {'login_required': True, 'logging': {'handler': 'stream', 'level': 'ERROR'}, 'port': 6005, 'halt_on_error': True}
    process_1: {'logging': {'handler': 'file', 'level': 'DEBUG'}, 'login_required': False, 'max_runtime': 100, 'port': 5556}
    

That's it
---------

This whole thing is just one small file, works in both Python 2.7 and
3.x and is released under `MIT
License <https://opensource.org/licenses/MIT>`__. Now, cascade!

Class documentation
------------------

.. automodule:: cascadict
 
.. autoclass:: CascaDict
    :members:
	
.. automethod:: cascadict.CascaDict.__flatten__

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

