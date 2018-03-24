from setuptools import setup

setup(name = 'world_python',
      version = '0.1.1',
      description = 'A demo package for Python',
      url = 'https://github.com/markjeee/world_python',
      author = 'Mark John Buenconsejo',
      author_email = 'hi@markjeee.com',
      license = 'MIT',
      packages = [ 'world_python', 'world_python/tests' ],
      test_suite = 'nose.collector',
      tests_require = [ 'nose' ],
      entry_points = {
          'console_scripts': ['world_python=world_python.command_line:main']
      },
      zip_safe = False)
